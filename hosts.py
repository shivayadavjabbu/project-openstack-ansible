import sys
h_name = sys.argv[1]
file1=open('./server.conf')
no_servers = file1.readline()
no_servers = no_servers.rstrip()
file1.close()
f = open("./hosts", "w")
f.write("[Bastionhost]\n")
hostname = h_name+"_bastion"
f.write(f"{hostname}\n")
f.write("[haproxy]\n")
hostname = h_name+"_haproxy"
f.write(f"{hostname}\n")
hostname=h_name+"_backuphaproxy"
f.write(f"{hostname}\n")
f.write("\n")
f.write("[webservers]")
f.write("\n")
for i in range(int(no_servers)):
    hostname = h_name+"_dev"+str(1+i)
    f.write(f"{hostname}\n")
f.write("\n")
f.write("[all:vars]\n")
f.write("ansible_user=ubuntu")
f.write("\n")
f.close()
