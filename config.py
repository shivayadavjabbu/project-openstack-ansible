import sys
host_name = sys.argv[1]
file1=open('./temp/publickeyfile')
pkeyfile = file1.readline()
file1.close()
pkeyfile = pkeyfile.rstrip()
file2=open('./temp/config')
op_file = file2.readline()
file2.close()
file3=open('./server.conf')
no_ofservers = file3.readline()
file3.close()
file4=open('./temp/bastionfloating')
bastion_ip = file4.readline()
file4.close()

def config_write(pkeyfile,ip,h_name,bast_ip):
        f.write(f"host {h_name}\n")
        f.write("port 22\n")
        f.write("user ubuntu\n")
        f.write(f"UserKnownHostsFile=~/dev/null\n")
        f.write(f"IdentityFile {pkeyfile}\n") # changes as per user
        f.write(f"hostname {ip}\n")
        if h_name!=bast_ip:
            f.write(f"proxyjump {bast_ip}\n")
        f.write("\n")

f = open(f"./{op_file}".replace("\n",""), "w")
f.write("PasswordAuthentication no\n")
f.write("StrictHostKeyChecking no\n\n")
ip = bastion_ip
h_name = host_name+"_bastion"
bast_ip  = h_name
config_write(pkeyfile,ip,h_name,bast_ip)
ip = "192.168.0.11"
h_name = host_name+"_haproxy"
config_write(pkeyfile,ip,h_name,bast_ip)
h_name = host_name+"_backuphaproxy"
ip = "192.168.0.12"
config_write(pkeyfile,ip,h_name,bast_ip)

for i in range(int(no_ofservers)):
        h_name=host_name+"_dev"+str(1+i)
        ip = "192.168.0."+str(21+i)
        config_write(pkeyfile,ip,h_name,bast_ip)
f.close()
