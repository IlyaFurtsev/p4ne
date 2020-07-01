from pysnmp.hlapi import *
communityname='public'
ipaddr='10.31.70.107'
snmpport=161
SE=SnmpEngine()
CD=CommunityData(communityname,mpModel=0)
UTT=UdpTransportTarget((ipaddr,snmpport))
CDt=ContextData()
OT1=ObjectType(ObjectIdentity('SNMPv2-MIB','sysDescr',0))
OT2=ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2'))

result1=getCmd(SE,CD,UTT,CDt,OT1)
swident=result1
result2=nextCmd(SE,CD,UTT,CDt,OT2,lexicographicMode=False)
swint=result2
print('\n')
print('System descriprion:')
for i in swident:
    for j in i[3]:
        print(j)
print('\n')
print('Interfaces:')
for i in swint:
    for j in i[3]:
        print(j)
