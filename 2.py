print('b a c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a or b) and (not(b)==c) and (d or not(a)))==0:
                    print(b, a, c, d)
