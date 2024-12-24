#f перевод в систему счисления 
def tri(x):
    s=''
    while x!=0:
        s=str(x%3)+s
        x//=3
    return s 
