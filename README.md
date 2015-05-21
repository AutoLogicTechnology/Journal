# Journal

Autologic Journal is a simple RESTful API for receiving Playbook and Runner information from [Journal Callback](https://github.com/AutoLogicTechnology/Journal-Callback), an [Ansible](http://www.ansible.com/) callback plugin. It acts as a central point of truth for your Ansible auditing, allowing your team complete visibility of what's taking place on the network. It currently works with [ElasticSearch](http://www.elastic.co/), using it as a distributed document store.

ElasticSearch was selected due to its ease of use, Python library, RESTful API interface, easy clustering, and general acceptance and use within the community, not to mention the ELK stack. Other databases, such as MongoDB, could easily be supported, but for the time being ElasticSearch serves our needs.

## Warning

**Please note**: this code is not suitable for production use. It's currently under heavy, active development and needs a lot of attention before it should be used in production, or anything ressembling production. Assume **all data will be lost**.

## Version

0.4.3

## Filters

Filtering is done on a per Journal basis. As a Journal comes into the API, it is filtered and cleaned up. This is done so that the Journal Callback doesn't have to do it, thus allowing for a faster invocation on the client-side. 

These filters are simple Yapsy plugins, and Journal currently ships with two:

- Yum
- Default

The Yum module will work with the incoming Journal data and filter out the crap, resulting in a clean response object that can be indexed nicely in ElasticSearch.

The Default module simply applies to everything else.

### Naming

Filters are called for dynamically from the ```filters/``` directory. If an incoming Journal has a task which used the Ansible module ```apt```, for example, then a filter plugin called ```apt``` will be looked for.

This does mean that each Ansible module can only have one filter plugin applied to it, but the minimal work done in Journal allows for the user to easily swap out filters or write their own, without having to delve into Journal's code.

### Raw Results

If there is no filter name to match the Ansible module name, the ```default``` filter will be used and data will simply be stored in a ```raw``` key.

### Writing Filters

Please note that writing a filter requires two files:

- filter.py
- filter.yapsy-plugin

The former is the actual filter it's self, and it must follow this design pattern:

```python
from yapsy.IPlugin import IPlugin

class filter(IPlugin):

  def parse_task(self, task):
    pass
```

Essentially, you need a class that inherits from ```IPlugin``` and contains a ```parse_task()``` method. That's all. Anything else you write into the class will be considered internal and go untouched by the filter system.

The ```.yapsy-plugin``` file allows the Yapsy Plugin Manager to actually find the filters. It should look like this:

```ini
[Core]
Name = filter
Module = filter

[Documentation]
Author = Your Name
Version = 0.1.0
Website = http://mysuperfilter.com
Description = It finds things and licks them.
```

## Development

The ```/development``` directory contains everything you would need to run a local copy of the service, accessible via the ```http://localhost:5000/journal``` URL.

### Requirements

You will need a few things before you can utilise this Vagrantfile:

1. [Vagrant](http://www.vagrantup.com/);
1. A supported provided. VirtualBox is assumed by the Vagrantfile - you may have to edit it;
1. Ansible (```pip install ansible``` or ```easy_install ansible```);
1. A decent machine with the capability of running the VM. An SSD is recommended;

Once you're confident you have everything in place, you can install the required Ansible roles and bring the VM up:

1. ```ansible-galaxy install -r Ansible.yaml```
1. ```vagrant up```

If you make changes to the code, the application will automatically reload inside the VM (Flask is in debug mode.) If you want to edit the ```site.yaml``` file and alter how the VM is provisioned, you can re-provision the VM:

```vagrant provision```

### Vagrant SSH Bug

I'm not sure if it's something I've done wrong or whether it's a big in Vagrant, but if you try to issue a ```vagrant reload``` command (which you might want to do if you alter the networking settings or add a new shared folder), you'll get an SSH access issue. To resolve this issue, do the following:

1. ```vagrant ssh```
1. ```chmod 0600 ~/.ssh/authorized_keys```
1. Logout and ```vagrant reload``` again.

### Reload Bug

Because the development environment uses supervisord, there seems to be a bug which prevents changes to the ```supervisord.conf``` from taking effect without a ```vagrant reload```. If you find your vchanges aren't happening, such as supervisord is trying to access a file you no longer consider in play, then reload the VM. 

## Todo List

Our "todo" list can be found in [this Trello Kanban board](https://trello.com/b/3dnkMTOG).

## Author Information

- Michael Crilly
- Autologic Technology Ltd
- http://www.mcrilly.me/
