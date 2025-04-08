f=open('26_40.txt')
m,k,n=[int(i) for i in f.readline().split()]
a=[int(i) for i in f]
a.sort(reverse=True)
diski=[m]*k
local=[]
start=0
for i in range(n):
    flag=True
    for j in range(start, k):
        if a[i] <= diski[j]:
            diski[j] -= a[i]
            start = j + 1 
            flag=True
            break
    else:
        for j in range(start):
            if a[i] <= diski[j]:
                diski[j] -= a[i]
                start = j + 1
                flag = True
                break
    if flag == False:
        local.append(a[i])
print(sum(local), len(local))
