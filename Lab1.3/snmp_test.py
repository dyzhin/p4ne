from pysnmp.hlapi import * 
from pprint import pprint
result = getCmd(SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

result2 = nextCmd(SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
    lexicographicMode=False)

mycort = result
for i in mycort:
    for j in i[3]:
        print(j)
    
myint = result2
for i in myint:
    for j in i[3]:
        print(j)