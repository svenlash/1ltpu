from ipaddress import * 
net = ip_network('87.226.26.72/255.255.255.252')
k=0
for ip in net: 
  if bin(int(ip)).count('0')%2==0:
    print(bin(int(ip))[2:])
    k+=1
print()   
print(k)
    
