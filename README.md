PROJECT-OPENSTACK ANSIBLE
This project automates the deployment, operation, and cleanup of OpenStack using Ansible. It provides a set of scripts that allow for easy setup and management of OpenStack infrastructure.
The deployment machine needs to be updated with the latest version before proceeding.

#####PREREQUISITES######### \
Before running the scripts, ensure that the following components are installed and up to date:
Latest version of Python 3 
Latest version of Ansible 
Latest version of OpenStack client 


#######File Structure### \
The project consists of three main files:
install: This file is responsible for setting up the initial OpenStack infrastructure. It creates a keypair, router, subnet, network, and a specified number of servers (as defined in server.conf). The file should be executed with the following command: \
install <openrc> <tag> <ssh_key>  \ 
<openrc> refers to the OpenStack RC file, <tag> is a tag name for identification purposes, and <ssh_key> is the public key file used for server access.

operate: Once the initial infrastructure is set up, the operate file manages the continuous operation of the OpenStack environment. It runs in an infinite loop and periodically checks the server.conf file for any updates. If the number of servers is modified, it either deletes or builds the required servers accordingly. Additionally, if servers are added or removed, it installs Flask and updates the HAProxy configuration. If only servers are down, it updates the HAProxy configuration without making any changes to the infrastructure.

cleanup: The cleanup file is responsible for removing the OpenStack infrastructure created during the deployment. It deletes servers, routers, floating IPs, subnets, networks, and key pairs.


###########Usage###### \
Ensure that the deployment machine is updated with the latest version.

Install the latest version of Python 3, Ansible, and the OpenStack client.

Execute the install file with the appropriate arguments:

After the installation is complete, run the operate file to start the continuous operation of the OpenStack environment:
Modify the server.conf file to add or remove servers as needed. The operate script will automatically handle the changes and update the infrastructure accordingly.

When finished, use the cleanup file to remove the OpenStack infrastructure:
####Conclusion### \
The OpenStack-Ansible project automates the deployment, operation, and cleanup of OpenStack infrastructure. By utilizing the provided scripts, users can easily set up, manage, and remove OpenStack resources, saving time and effort in the process.
