for n in range(1,200):
    a=bin(n)[2:]
    if n%8==0: 
        a+=a[-2:]
    if n%8!=0:
        c=bin(n%8 * 2)[2:]
        a+=c
    r=int(a,2)
    if r>3000:
        print(n)
   