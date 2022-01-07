def sum1(a):
    s=0
    
    while(a>0):
       d=a%10
       s=s+d
       a=a/10
a=int(input("Enter the  number"))
m=sum1(a)
print("Sum of digit of a number is:",m)
    
