https://education.yandex.ru/ege/task/60136ef5-552a-4bc0-9224-2914e321d93b
# Доступен файл для чтения: 24.txt
a=open('24.txt').readline() 
a=a.replace('-','*')
a=a.split('**')
m=0
a=sorted(a, key=len, reverse=True)
for i in a: 
  try: eval(i); print(len(i)); break
  except: continue
'''from re import * 
reg=r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*'
for k in finditer(reg,a): 
  if len(k.group())==154:
    print(k.group())'''


