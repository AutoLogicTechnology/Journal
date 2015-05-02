# Journal

Autologic Journal is a simple RESTful API for receiving Playbook and Runner information from [Journal Callback](), an [Ansible]() callback plugin. It acts as a central point of truth for your Ansible auditing, allowing your team complete visibility of what's taking place on the network. It currently works with [ElasticSearch](), using it as a distributed document store.

ElasticSearch was selected due to its ease of use, Python library, RESTful API interface, easy clustering, and general acceptance and use within the community, not to mention the ELK stack. Other databases, such as MongoDB, could easily be supported, but for the time being ElasticSearch serves our needs.

## Version

0.1.0