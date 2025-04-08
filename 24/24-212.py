from re import *
'''
#204
s=open('C:/Users/79539/Desktop/24/24-204.txt').readline()
reg = r'(AA|CC)+'
reg = rf'(?=({reg}))+'
print(max(len(i.group(1))//2 for i in finditer(reg,s)))

#239
s=open('24-239.txt').readline()
reg = r'(YZZ|XY|YZ)+'
reg = rf'(?=({reg}))'
print(max(len(i.group(1)) for i in finditer(reg,s)))


#298
s =  open('24-298.txt')

num = r'[1-9][0-9]*'
reg = rf'{num}([-*]{num})+'

print(max(len(i.group()) for i in finditer(reg,s)))

'''

#313
s=open('24-310.txt').readline()
num=r'([12][012]*|0)'
reg=rf'{num}([+*]{num})+'
print(max(len(i.group()) for i in finditer(reg,s)))
