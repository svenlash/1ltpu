K=[]
def tw(x): #10=>12 система
  s=''
  while x: 
    a=x%12
    if x%12==10:
      a='A'
    if x%12==11:
      a='B'
    s=str(a)+s
    x//=12
  return s
for n in range(1,100000): #перебор N
  b=tw(n) #далее условия 
  spis=sorted(i for i in b)
  sp=spis[-1] 
  if n%4==0:
    b='2'+b+'64'
  else: b=b+sp
  r=int(b,12)
  if r>1799:
    K+=[r]
print(sorted(K)) #мин = 1806