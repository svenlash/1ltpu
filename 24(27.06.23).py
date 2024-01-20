import re
pat=re.compile(r'((8|9)?([ABC][89])+(A|B|C)?)')
m=pat.findall(open("24(27.06.23).txt").readline())
print(m[:5])
m=[x[0] for x in m]
print(len(max(m,key=len)))
