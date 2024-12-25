#перевод в любую систему счисления
''' def perevod(x):
    alf='0123456789abcdefghijklmnopqrstuvwxyz'
    s=''
    while x:
        s=alf[x%25]+s
        x//=25
    return s '''
''' rr=[]
def tri(x):
  s=''
  while x:
    s=str(x%3)+s
    x//=3
  return s 
for n in range(1,10000):
  a=tri(n)
  if len(a)%2==1:
    a='1'+a
  if len(a)%2==0: 
    a=a
  b=a
  x=[int(i) for i in str(b)]
  if sum(x)%2==0:
    b=b+b[-2:]
  if sum(x)%2==1: 
    b=b+tri(n%5)
  if b[0]=='2':
    b=b[1:]
  if b[-1]==b[-2]:
    b=b[:-1]
  r=int(b,3)
  if r>150:
    rr+=[r]
print(min(rr)) #151'''

'''for n in range(1000,10000):
  x=[int(i) for i in str(n)]
  if (x[0]!=x[1] and  x[0]!=x[2] and  x[0]!=x[3] and  x[1]!=x[2]
      and  x[1]!=x[3] and  x[2]!=x[3]): #if len(set(x))==len(x):
    x=sorted(x)
    y=min(x)+max(x)
    z=x[1]*x[2]
    s=[str(y),str(z)]
    s=sorted(s)
    s=''.join(s)
    r=int(s)
    if r>85:
      print(n,r) #1089'''

'''rr=[]
for n in range(1,10000):
  a=bin(n)[2:]
  if n%2==0:
    a='1'+a+'0'
  if n%2==1:
    a='11'+a+'11'
  r=int(a,2)
  if r>48:
    rr+=[r]
print(min(rr)) #52 '''

'''rr=[]
for n in range(1,10000):
  a=bin(n)[2:]
  x=a.replace('1','s')
  y=a.replace('0','1')
  z=a.replace('s','0')
  p=sum([int(i) for i in str(z)])%2
  z=z+str(p)
  r=int(z,2)
  if r<170:
    rr+=[r]
print(max(rr)) #169'''

for n in range(3, 100): #это собственный код
  a=bin(n)[2:]
  if a[-1]==a[-2]:
    if a[-1]=='0':
      a=a[:-1]+'1'+a[-1]
    if a[-1]=='1':
      a=a[:-1]+'0'+a[-1]
  else:
    x=a[-2:]
    x=x.replace('1','s')
    x=x.replace('0','1')
    x=x.replace('s','0')
    a=a[:-2]+x+x[-1]
  if a[-1]==a[-2]:
    if a[-1]=='0':
      a=a[:-1]+'1'+a[-1]
    if a[-1]=='1':
      a=a[:-1]+'0'+a[-1]
  else:
    x=a[-2:]
    x=x.replace('1','s')
    x=x.replace('0','1')
    x=x.replace('s','0')
    a=a[:-2]+x+x[-1]
  r=a
  if int(r,2)>168:
    print(n) #41 

''' это чат гпт
def transform_binary(binary_str):
    for _ in range(2):
        if binary_str[-1] == binary_str[-2]:
            if binary_str[-1] == '0':
                binary_str = binary_str[:-1] + '1' + binary_str[-1]
            else:
                binary_str = binary_str[:-1] + '0' + binary_str[-1]
        else:
            x = binary_str[-2:]
            x = x.replace('1', 's')
            x = x.replace('0', '1')
            x = x.replace('s', '0')
            binary_str = binary_str[:-2] + x + x[-1]
    return binary_str

for n in range(3, 100000):
  a = bin(n)[2:]
  r = transform_binary(a)
  if int(r, 2) > 168:
    print(n)
    break '''