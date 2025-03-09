def f(x, end, m):
    if x > end: return 0
    if x == end and m == 0: return 1
    if x != end and m == 0: return 0
    return f(x + 4, end, m - 1) + f(x * 2, end, m - 1)

cnt = 0
for end in range(1, 200):
    if f(2, end, 5) > 0:
        cnt += 1
print(cnt)
