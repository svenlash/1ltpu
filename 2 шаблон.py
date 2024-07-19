for x in range(0,2,1):
    for y in range(0,2,1):
        for z in range(0,2,1):
            for w in range(0,2,1):
                f = not(w==y) and (not(z) or w) and not(x) 
                if f == 1:
                    print(x,y,z,w)
                    

