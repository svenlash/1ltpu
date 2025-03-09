#kpol 7497
s=open('24-298.txt').readline()
s=s.replace('-','*')
mx=-1000
res = ''
for i in range(len(s)-1):
    if s[i]=='*' and (s[i+1]=='*' or s[i+1]=='0'):
        mx = max(mx, len(res))
        res=''
        continue
    '''if s[i]=='*' and s[i+1]=='0':
        mx = max(mx, len(res))
        res=''
        continue'''
    if res == '' and s[i]=='0':
        continue
    res+=s[i]
print(mx)


