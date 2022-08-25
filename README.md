# project-openstack-ansible
first update the deployment machine.
install the required packages from requirements.txt,, cmd: xargs -a requirements.txt sudo apt-get install -y
generate new ssh-key with cmd ssh-keygen -t rsa 
there are three files instal operate and cleanup
each file should extend with openstack.rc file, tagname, pubkey file 
example: install <openrc> <tag> <ssh_key> example: ./install openstack.sh tag ~/.ssh/id_rsa.pub
first Run install file,
 it creates a keypair,router,subnet,network and servers(the no of servers to be created is given in the server.conf), 
after running the install now run operate.
operate runs in loops for infinite times. In every step it checks for the server.conf file and deletes servers or build servers according to teh file.
the last step run the cleanup file for deleting servers,routers,floating_ip,subnet,network,keypair.

