# Journal

Autologic Journal is a simple RESTful API for receiving Playbook and Runner information from [Journal Callback](https://github.com/AutoLogicTechnology/Journal-Callback), an [Ansible](http://www.ansible.com/) callback plugin. It acts as a central point of truth for your Ansible auditing, allowing your team complete visibility of what's taking place on the network. It currently works with [ElasticSearch](http://www.elastic.co/), using it as a distributed document store.

ElasticSearch was selected due to its ease of use, Python library, RESTful API interface, easy clustering, and general acceptance and use within the community, not to mention the ELK stack. Other databases, such as MongoDB, could easily be supported, but for the time being ElasticSearch serves our needs.

## Warning

**Please note**: this code is not suitable for production use. It's currently under heavy, active development and needs a lot of attention before it should be used in production, or anything ressembling production. Assume **all data will be lost**.

## Version

0.1.2

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

## Todo List

Our "todo" list can be found in [this Trello Kanban board](https://trello.com/b/3dnkMTOG).

## Author Information

- Michael Crilly
- Autologic Technology Ltd
- http://www.mcrilly.me/
