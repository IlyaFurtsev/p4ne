import glob
import re
import json
import pprint

from flask import Flask
from ipaddress import IPv4Interface


filelist=glob.glob("C:\\Users\\io.furtsev\\Seafile\\p4ne_training\\config_files\\*.txt")
file=[]
hosts={}







site=Flask(__name__)

@site.route('/')
def titlepage():
    return 'Вы видите краткую справку об использовании данного сайта. Зайдите на /configs для получения списка всех хостов, конфиги которых хранятся в папке config_files'
@site.route('/configs')
def viewhosts():
    page1 = 'Список хостов:'
    n = 0
    for i in filelist:
        with open(i) as file:
            for l in file:
                value = re.match("^hostname +(.+)", l)
                if value:
                    name = value.group(1)
                    n += 1
                    hos = 'host ' + str(n) + ' -'
                    u = {hos: name}
                    hosts.update(u)
                else:
                    continue
    hosts.update({'Enter hostname in address bar after configs/':'!'})
    return hosts
@site.route('/configs/<namehost>')
def findinterfaces(namehost):
    ipaddr = {}
    for i in filelist:
        with open(i) as file:
            for l in file:
                value = re.match("^hostname +(.+)", l)
                if value:
                    if value.group(1) == namehost:
                        n1=0
                        for k in file:
                            value1 = re.match(
                                ".*ip address ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) *([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*",
                                k)
                            if value1:
                                address = value1.group(1)
                                mask = value1.group(2)
                                n1 += 1
                                ip = namehost + ' interface num ' + str(n1) + ' ='
                                u1 = {ip: str(IPv4Interface((address, mask)))}
                                ipaddr.update(u1)
                    else: break
    return ipaddr




if __name__ == '__main__':
    site.run(debug=True)