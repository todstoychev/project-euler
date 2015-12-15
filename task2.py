max = 4000000
a = 1
b = 1
c = 0
sum = 0

while (a + b < max):
     c = a
     a = b
     b = b + c
     if (b % 2 == 0):
         sum += b
        
print(sum)
     
