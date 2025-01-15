from string import printable 
alf=printable[:36]
for a in range(30, 37):
  s = int('LANCELOT', a) + int('ELSA', a) - int('DRAGON', a) + int('CAT', a)
  if s%1747 == 0: 
    print(s//1747)
