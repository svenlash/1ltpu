# Доступен файл для чтения: 17.txt
kk=open('17.txt')
a=[int(i) for i in kk]
s=0
mx=-10**4
b=[int(i) for i in kk if i%2042==0]
k=len(b)
for i in range(len(a)-1):
  b=a[i:i+2]
  if sum(b)>k:
    s+=1
    mx=max(mx,sum(b))
print(s,mx)
