import re
pat=re.compile(r'(?<=KK)(43\d{2}78\d{3}34)(?=KK)')
m=pat.findall(open("24(pol5646).txt").readline())
print(m[:5])
m=[int(x) for x in m]
maxx=max(m)
p=1
for x in str(maxx):
    if int(x)%2!=0:
        p=p*int(x)
print(p)