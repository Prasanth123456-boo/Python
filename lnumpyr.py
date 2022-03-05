n = int(input("Enter the step size: "))
for i in range(1,n+1):
 k= i
 for j in range(1,i+1):
     print(k, end = ' ')
     k += i
 print() 
