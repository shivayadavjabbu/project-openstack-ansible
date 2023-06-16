import sys
import re
host_name = sys.argv[1]

file1=open('./temp/publickeyfile')
pkeyfile = file1.readline()
file1.close()
pkeyfile = pkeyfile.rstrip()

hostnames_file = open('./temp/hostnames', 'r')
hostnames = hostnames_file.read().splitlines()
hostnames_file.close()

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
op_file = host_name+"_SSHconfig"
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

for hostname in hostnames:
        device_number = int(re.findall(r'\d+', hostname)[-1])
        ip = "192.168.0."+str(20+device_number)
        config_write(pkeyfile,ip,hostname,bast_ip)
f.close()
