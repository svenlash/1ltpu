m=b=0
openn = open('04.03.txt')
x=[int(s) for s in openn]
for i in range (len(x)-3):
    if ( abs(x[i])%100==13 and abs(x[i+3])%100!=13 ) \
    or ( abs(x[i])%100!=13 and abs(x[i+3])%100==13 ):
        b+=1
        m=max( m,  x[i]+x[i+3] )
print(b, m)
    
