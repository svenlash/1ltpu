def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result
a=(361*(2349**84))-(89**192)+((1953**481)*(4843**151))
b=convert_to(a,9)
b=str(b)
s=b.count('5')
print(s)