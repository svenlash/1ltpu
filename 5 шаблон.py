for n in range(0, 100):
    a = bin(n)[2:]
    if n % 3 == 0:
        a += a[-3:]
    else:
        a += bin((n%3)*3)[2:]
    r = int(a, 2)
    print(n,r)
    if r >= 76:
        print('n =', n)
        break
