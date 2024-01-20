import re
pat = re.compile(r'[1-9A-F][0-9A-F]+')
m=pat.findall(open ("24(20.06.23).txt").readline())
print(m[:5])
print(len(max(m,key=len)))