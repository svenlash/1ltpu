
#while len(s)<100:
for n in range(1,1000):
    s='1'+'0'*n
    while '10' in s or '1' in s:
        if '10' in s:
            s=s.replace('10','001',1)
        else:
            if '1' in s:
                s=s.replace('1','0',1) 
    if len(s)>=100: break
print(n)