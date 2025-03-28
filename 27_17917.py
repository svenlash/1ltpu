def centroid(cluster):
    xc,yc,mn=0,0,10**10
    for i in range(len(cluster)):
        res=0
        for j in range(len(cluster)):
            x1,y1=cluster[i]
            x2,y2=cluster[j]
            res+= ((x2-x1)**2 + (y2-y1)**2)**0.5
        if res<mn:
            mn=res
            xc,yc=x1,y1
    return (xc,yc)

f=open('27_A_17917.txt')
cluster1=[]
cluster2=[]
cluster3=[]
cluster4=[]
for i in f:
    x,y=map(float,i.split())
    if x<10 and y>14:
        cluster1.append((x,y))
    if x<10 and y<14:
        cluster2.append((x,y))
    if x>10 and y<8:
        cluster3.append((x,y))
    if x>10 and y>8:
        cluster4.append((x,y))
x1,y1=centroid(cluster1)
x2,y2=centroid(cluster2)
x3,y3=centroid(cluster3)
x4,y4=centroid(cluster4)
print(int((x1+x2+x3+x4)/4 * 10000),int((y1+y2+y3+y4)/4 * 10000))



def centroid(cluster):
    xc,yc,mn=0,0,10**10
    for i in range(len(cluster)):
        res=0
        for j in range(len(cluster)):
            x1,y1=cluster[i]
            x2,y2=cluster[j]
            res+= ((x2-x1)**2 + (y2-y1)**2)**0.5
        if res<mn:
            mn=res
            xc,yc=x1,y1
    return (xc,yc)

f=open('27_B_17917.txt')
cluster1=[]
cluster2=[]
cluster3=[]
cluster4=[]
cluster5=[]
for i in f:
    x,y=map(float,i.split())
    if x<6.5:
        cluster1.append((x,y))
    elif x<18:
        cluster2.append((x,y))
    elif x<24:
        cluster3.append((x,y))
    elif x<28:
        cluster4.append((x,y))
    else:
        cluster5.append((x,y))
x1,y1=centroid(cluster1)
x2,y2=centroid(cluster2)
x3,y3=centroid(cluster3)
x4,y4=centroid(cluster4)
x5,y5=centroid(cluster5)
print(int((x1+x2+x3+x4+x5)/5 * 10000),int((y1+y2+y3+y4+y5)/5 * 10000))
