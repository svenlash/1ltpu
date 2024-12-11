def f(x):
  a=set()
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      a.add(i)
      a.add(x//i)
  return sorted(a)
for x in range(700000,1000000):
  a=f(x)
  if len(a)==2:
    k=a[-1]-a[0]
    if k<=15:
      print(x,k)
