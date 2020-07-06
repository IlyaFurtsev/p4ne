import glob
import re
import ipaddress
from ipaddress import IPv4Interface, IPv4Address

filelist=glob.glob("C:\\Users\\io.furtsev\\Seafile\\p4ne_training\\config_files\\*.txt")
file=[]
ipaddr={}
interf={}
hosts={}

for i in filelist:
    with open(i) as file:
        n = 0
        for l in file:
            value = re.match(".*ip address ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) *([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*", l)
            if value:
                address = value.group(1)
                mask = value.group(2)
                n += 1
                ip= 'ip address '+str(n)+' ='
                u={ip:str(IPv4Interface((address,mask)))}
                ipaddr.update(u)
            else:
                continue

for i in filelist:
    with open(i) as file:
        n = 0
        for l in file:
            value = re.match("^interface +([A-Za-z0-9\/\.\-]+)", l)
            if value:
                name = value.group(1)
                n += 1
                int= 'interface '+str(n)+' ='
                u={int:name}
                interf.update(u)
            else:
                continue

for i in filelist:
    with open(i) as file:
        n = 0
        for l in file:
            value = re.match("^hostname +([A-Za-z0-9\/\.\-]+)", l)
            if value:
                name = value.group(1)
                n += 1
                hos= 'hostname '+str(n)+' ='
                u={hos:name}
                hosts.update(u)
            else:
                continue

for i in ipaddr:
    print(i,ipaddr[i])
for i in interf:
    print(i, interf[i])
for i in hosts:
    print(i, hosts[i])
