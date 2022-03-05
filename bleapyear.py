print("Leap year between two given years")
startYear=int(input("Enter start year: "))
endYear=int(input("Enter last year: "))
print("list of leap years: ")
for year in range (startYear,endYear):
 if(0==year%4)and(0!=year%240)or(0==year%400):
     print(year)
