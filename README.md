# project-openstack-ansible
--> Update the deployment machine by installing the latest version of Python 3, Ansible, and the OpenStack client.\
--> The deployment involves three files: install, operate, and cleanup. Each file should be extended with the OpenStack RC file, tag name, and public key file. For example: install <openrc> <tag> <ssh_key>.\
--> Start by running the install file. It will create a keypair, router, subnet, network, and Security group. The number of servers to be created is specified in the server.conf file \
--> After running the install file, proceed to run the operate file. This file runs in a loop indefinitely. In each iteration, it checks the server.conf file and either deletes existing servers or builds new servers based on the file's content.
--> Finally, run the cleanup file to delete servers, routers, floating IPs, subnets, networks, and the keypair.
