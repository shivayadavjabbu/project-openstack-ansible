file1 = open('./temp/requiredhosts')
new = []
for line in file1:
    new.append(line)
file1.close()
file2=open('./temp/publickeyfile')
pkeyfile = file2.readline()
file2.close()
file4=open('./temp/config')
op_file = file4.readline()
file4.close()
f = open(f"./{op_file}".replace("\n",""), "w")
f.write("PasswordAuthentication no\n")
f.write("StrictHostKeyChecking no\n\n")
for i in new:
    if len(i) > 5:
        new_line = i.split(" ")
        if len(new_line[1]) > 7:
            #print(new_line[1][-7:])
            if (new_line[1][-7:]) == 'bastion':
                bast_ip = new_line[1]
                #print(bast_ip)
for line in new:
    if len(line)>5:
        linesplit = line.split(" ")
        f.write("host ")
        f.write(linesplit[1])
        f.write("\n")
        if len(linesplit) == 10:

            ip = linesplit[3].split("=")
            ip = ip[1]
            #print(ip)
        elif len(linesplit)==12:
            if linesplit[1][-7:]=='bastion':
                ip = linesplit[5].strip("[',]}")
            else:
                ip = linesplit[4].strip("[',]}")

        else:
            if linesplit[1][-7:]=='haproxy':
                ip=linesplit[3].split("=")
                ip=ip[1].strip(",")
                #print(ip)
            elif linesplit[1][-7:]=='bastion':
                ip = linesplit[4]
            else:
                ip = linesplit[4].strip("[',]}")

        f.write("port 22\n")
        f.write("user ubuntu\n")
        f.write(f"UserKnownHostsFile=~/dev/null\n")
        f.write(f"IdentityFile {pkeyfile}") # changes as per user
        f.write("hostname ")
        #print(new_line[1][-7:])
        f.write(ip)
        f.write("\n")
        if linesplit[1] != bast_ip:
            f.write(f"proxyjump {bast_ip}\n")
        
    f.write("\n")

f.close()
