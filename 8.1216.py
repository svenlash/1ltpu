from itertools import product 
ZV=product('01234', repeat=6)
SVO=[z for z in ZV if (z[0]!='0' and z[0]!='1') and (z[5]!='3' and z[5]!='4') ]
print(len(SVO))
