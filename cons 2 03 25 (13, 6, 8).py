'''from turtle import *
tracer(0,0)
screensize(3000,3000)
up()
k = 40
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(2,'red')
home()
lt(90)
down()
rt(60)
for _ in range(2):
    fd(7 * k)
    rt(120)
rt(300)
fd(7 * k)
for i in range(2):
    rt(60)
    fd(7 * k)
    rt(60)
update()
done()
'''


#в левых двух байтах больше единиц чем в правых двух
#[:16] [16:]
from ipaddress import *
k=0
net = ip_network('101.157.240.0/255.255.252.0', 1)
#по сетевому адресу - 1
for ip in net:
    if f'{ip:b}'[:16].count('1') > f'{ip:b}'[16:].count('1'):
        k+=1
print(k)


#по узлу - 0
for mask in range(33):
    net = ip_network(f'222.190.122.24/{mask}',0)
    if str(net.network_address) == '222.190.120.0':
        print(len(list(net.hosts()))-1)
#в хостах нет широковещательного и сетевого

ip1=ip_address('216.54.187.235')
ip2=ip_address('216.54.174.128')
for mask in range(33):
    net1 = ip_network(f'216.54.187.235/{mask}',0)
    net2 = ip_network(f'216.54.174.128/{mask}',0)
    if net1.network_address != net2.network_address:
        if ip1!=net1[0] and ip1!=net1[-1] and ip2!=net2[0] and ip2!=net2[-1]:
            print(mask)



cnt=0
from itertools import *
alf = '0123456'
for i in product(alf,repeat=5):
    s=''.join(i)
    if s[0]=='0': continue
    for k in '0246':
        s=s.replace(k,'*')
    if s.count('**')>=2 and '***' not in s:
        cnt+=1
print(cnt)



def f(a,x):
    if a<=19: return x%2==0
    if x==0: return 0
    h=[f(a-5,x-1)]
    if a%2==0:
        h.append(f(a//2,x-1))
    if a%3==0:
        h.append(f(a//3,x-1))
    else:
        h.append(f(a+1,x-1))
    return any(h) if x%2==1 else all(h)
print([i for i in range(20,100) if f(i,2)])
print([i for i in range(20,100) if f(i,3) and not f(i,1)])
print([i for i in range(20,100) if f(i,4) and not f(i,2)])


