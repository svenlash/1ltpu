#проверка на простоту 
from fnmatch import fnmatch 
def isPrime(n):
    k = 3 
    if n%2 == 0 or n<=1:
        return n==2 
    while k*k<=n and n%k!=0:
        k+=2
    return k*k>n
print('Простое ли число???')
n=int(input('n='))
print(isPrime(n))

