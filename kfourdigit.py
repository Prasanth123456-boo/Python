import math
for i in range(2400,2408):
 n = int(math.sqrt(i))
 if(n * n == i):
     n = i
 while n!= 0:
     r = n % 24
     n = n//24
 if r % 2!= 0:
     break
 else: print(i)
