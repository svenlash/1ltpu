import re
pat=re.compile(r'((Q|SQ)?(RSQ)+(RS|R)?)')
m=pat.findall(open("import re
pat=re.compile(r'((Q|SQ)?(RSQ)+(RS|R)?)')
m=pat.findall(open("24(16.12.23).txt").readline())
print(m[:5])
m=[x[0] for x in m]
print(len(max(m,key=len)))").readline())
print(m[:5])
m=[x[0] for x in m]
print(len(max(m,key=len)))