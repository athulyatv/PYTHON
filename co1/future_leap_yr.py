 #display the future leap yeras fromthe current year to a final years
count=0
y1=int(input("enter the current year:"))
y2=int(input("enter the last year:"))
for i in range(y1,y2 +1):
    if (i%4==0 and i%100!=0 or i%400==0):
        print(i,end=" ")
        count=count+1
    i=i+1
print("\n no of leap years:",count)
