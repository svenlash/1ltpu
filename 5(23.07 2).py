x=10000
for n in range(0,100):
    a=bin(n)[2:]
    if a.count('1')%2==0:
        a = '10' + a[2:] + '0'
    else:
        a = '11' + a[2:] + '1'
    r=int(a, 2)
    if n>27:
        x=min(x,r)
print(x)
'''42'''
    
