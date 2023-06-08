# project-openstack-ansible
first update the deployment machine.
install update version of python3,
install ansible latest version,
install openstack-client,
there are three files instal operate and cleanup
each file should extend with openstack.rc file, tagname, pubkey file 
example: install <openrc> <tag> <ssh_key>
first Run install file,
 it creates a keypair,router,subnet,network and servers(the no of servers to be created is given in the server.conf), 
after running the install now run operate.
operate runs in loops for infinite times. In every step it checks for the server.conf file and deletes servers or build servers according to teh file.
the last step run the cleanup file for deleting servers,routers,floating_ip,subnet,network,keypair.

