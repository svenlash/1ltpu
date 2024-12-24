f=open('17_9786.txt'); a=[int(i) for i in f]; m=max(i for i in a if abs(i)%100==25); k=0; mn=0
def R(x):
    return len(str(abs(x)))==4
for i in range(len(a)-2):
    b=a[i:i+3]
    if R(b[0])+R(b[1])+R(b[2])<=2 and sum(b)<=m: k+=1; mn=max(sum(b),mn)
print(k,mn) #6315 84523
    
