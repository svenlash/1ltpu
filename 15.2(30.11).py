def treug(a,b,c): 
    h = [a, b ,c]
    return max(h)<sum(h)-max(h)
def f(x, a): 
    return ((treug(x,11,18)==(not(max(x,5)>68))) and (treug(x,a,5))) == 0
for a in range(1,1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a)
#64