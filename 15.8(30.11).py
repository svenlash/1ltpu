def O(x,y,a):
    return (x<=19) or (y < 2*x + a - 50) or (y>17)
for a in range(0,999):
    if all(O(x,y,a) for x in range(0, 999) for y in range (0,999)): 
        print(a)
        break
#28