import sys

h_name = sys.argv[1]

hostnames = []

with open('./temp/hostnames') as file2:
    for line in file2:
        hostnames.append(line.rstrip())

with open('./hosts', 'w') as f:
    f.write('[Bastionhost]\n')
    hostname = h_name + '_bastion'
    f.write(f'{hostname}\n')
    f.write('[haproxy]\n')
    hostname = h_name + '_haproxy'
    f.write(f'{hostname}\n')
    hostname = h_name + '_backuphaproxy'
    f.write(f'{hostname}\n')
    f.write('\n')
    f.write('[webservers]\n')
    for hostname in hostnames:
        f.write(f'{hostname}\n')
    f.write('\n')
    f.write('[all:vars]\n')
    f.write('ansible_user=ubuntu\n')

