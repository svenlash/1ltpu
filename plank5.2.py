for n in range(1,100):
    x=bin(n)[2:]
    if n%2==0:
        x='1'+x+'00'
    else: x=x+bin(x.count('1'))[2:]
    if int(x,2)>=190:
        print(n)
        break
