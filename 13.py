from ipaddress import *
net = ip_network('120.168.0.0/24', 1)
cnt=0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') %3 == 0:
        cnt += 1
print(cnt)

ip=ip_address('137.219.220.63')
for mask in range(32, 0, -1):
    net = ip_network(f'137.219.220.63/{mask}', 0)
    # 0 ибо узел
    if net.broadcast_address != ip:
        print(mask)
        break

for mask in range(32, 0, -1):
    net1 = ip_network(f'121.171.5.70/{mask}', 0)
    net2 = ip_network(f'121.171.5.107/{mask}', 0)
    if net2.network_address == net1.network_address:
        print(len(list(net1)))
        break

from ipaddress import ip_network
for mask in range(32,0,-1):
    k=0
    net1 = ip_network(f'157.220.185.237/{mask}', 0)
    net2 = ip_network(f'157.220.184.230/{mask}', 0)
    if net1.network_address == net2.network_address:
        for ip in net1:
            ip=f'{ip:b}'
            if ip.count('1') == 15:
                k+=1
        print(k)
        break










