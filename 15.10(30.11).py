def Q(x,a):
    return (x%a!=0)<=((x%28==0)<=(x%49!=0))
for a in range(1,999):
    if all(Q(x,a) for x in range(1,999)):
        print(a)
#196