a = 3
b = 5
sumA = 0
sumB = 0

while (sumA <= 1000):
    sumA += a
    print ('Sum A is:' + str(sumA))    
    
    if (sumB <= 1000):
        sumB += b
        print ('Sum B is:' + str(sumB))
        
print ('Result is: ')
print (sumA + sumB)       
