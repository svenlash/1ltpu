
def dist(p1,p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5

f=open('27_A_17915.txt')
clusters=[[] for i in range(3)]
for point in f:
    x, y = map(float, point.split())
    if x<6:
        clusters[0].append((x,y))
    elif y>23:
        clusters[1].append((x,y))
    else:
        clusters[2].append((x,y))

centroids = []
for k in range(3):
    mn_sum=10**9
    xc=0
    yc=0
    for p1 in clusters[k]:
        sum_dist=0
        for p2 in clusters[k]:
            sum_dist += dist(p1,p2)
        if sum_dist < mn_sum:
            mn_sum, xc, yc = sum_dist, p1[0], p1[1]
    centroids.append([xc,yc])
print(int(sum(p[0] for p in centroids)/3*10000), int(sum(p[1] for p in centroids)/3*10000))


def dist(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


f = open('27_B_17915.txt')

clusters = [[] for i in range(4)]
for point in f:
    x, y = map(float, point.split())
    if x < 15 and y > 15:
        clusters[0].append((x, y))
    elif x < 15 and y < 15:
        clusters[1].append((x, y))
    elif x > 15 and y > 15:
        clusters[2].append((x, y))
    else:
        clusters[3].append((x, y))

centroids = []
for k in range(4):
    mn_sum = 10 ** 9
    xc = yc = 0
    for p1 in clusters[k]:
        sum_dist = 0
        for p2 in clusters[k]:
            sum_dist += dist(p1, p2)
        if sum_dist < mn_sum:
            mn_sum, xc, yc = sum_dist, p1[0], p1[1]
    centroids.append([xc, yc])
print(int(sum(p[0] for p in centroids) / 4 * 10000),
      int(sum(p[1] for p in centroids) / 4 * 10000))
















