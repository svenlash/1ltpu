f = open('26_38.txt')

k = int(f.readline())
n = int(f.readline())

a = [list(map(int, l.split())) for l in f]
a.sort()

cells = [0]*k
index = 0
cnt = 0
for i in range(n):
    for j in range(k):
        if a[i][0] > cells[j]:
            cells[j] = a[i][1]
            cnt += 1
            index = j + 1
            break
print(cnt, index)
