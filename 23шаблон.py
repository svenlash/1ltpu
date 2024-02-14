from itertools import product
nums=(product('123', repeat=5))
for i in nums:
    print(''.join(i))
