'''from re import * 
s=open('21.txt').readline()
reg=r'[ABC]+'
mx=0
for i in finditer(reg,s): 
    #finditer - находит по маске reg 
    mx=max(mx,len(i.group()))
print(mx) 
print(max(len(i.group()) for i in finditer(reg,s)))'''
