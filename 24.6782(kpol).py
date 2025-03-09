# kpol 6782
from string import printable
a = open('24-264.txt').readline()
mx = -1000
for _ in printable[36:62]:
    a = a.replace(_, '*')
for k in '0123456789':
    a = a.replace(k, 'X')
R=[]
res=''
for i in range(len(a) - 1):
    if a[i] + a[i + 1] == 'XX' or a[i] + a[i + 1] == '**':
        mx = max(mx, len(res))
        R.append(res)
        res=''
        #continue
    res += a[i]
print(mx)
