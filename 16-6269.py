from functools import cache
@cache 
def s(n):
    if n<10: return n
    if n<1000: return s(n//10) + s(n%10)
    if n>=1000: return s(n//1000) - s(n%1000)
n=0
k=0
while n<=10**6:
    n+=1
    if s(n)==0:
        k+=1
print(k)
