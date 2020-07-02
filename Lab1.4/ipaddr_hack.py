from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, mask_range_start, mask_range_stop):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000,0xDF000000), random.randint(mask_range_start, mask_range_stop)),
                             strict=False)

def key_funk(addr):
    #ip_address = addr.network_address
    #net_mask = addr.netmask
    #print(ip_address, net_mask, sep='/')
    ip_address = int(addr.network_address)
    net_mask = int(addr.netmask)
    return net_mask * 2**32 + ip_address

fake_nets = []
for i in range(20):
    fake_nets.append(IPv4RandomNetwork(8,24))

sorted_fake_nets_list = sorted(fake_nets, key=key_funk)
for i in sorted_fake_nets_list:
    print(i)