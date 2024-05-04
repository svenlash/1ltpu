from itertools import product
Z=product('1234',repeat=4)
V=[x for x in Z if x[0]<=x[1]<=x[2]<=x[3]]
print(len(V))
        
