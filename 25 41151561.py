from fnmatch import *
k=0
for i in range(124,10**9,124):
    while k!=7:
        if not(fnmatch(str(i),'1*77*1'))and not(fnmatch(str(i),'7*11*7')):
            if fnmatch(str(i),'1?3**5?'):
                print(i,i//124)
                k+=1
        
from fnmatch import *
for i in range(124,10**4,124):
    if fnmatch(str(i),' 1?3**5?'):      
        print(i,i//124)
        
