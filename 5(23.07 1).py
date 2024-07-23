for n in range(1,100):
    a=bin(n)[2:]
    a+=str(a.count('1')%2)
    a+=str(a.count('1')%2)
    r = int(a, 2)
    if r>123:
        print(r)
'''126'''
