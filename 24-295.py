a=open('24-295.txt')
f=a.readline()
c=[x for x in f.split()]
maxLen=0
for i in range(len(c)-240):
    curLen=0
    for x in range(i,i+240+1):
        curLen+=len(c[x])
    maxLen=max(curLen,maxLen)
print(maxLen, curLen)
