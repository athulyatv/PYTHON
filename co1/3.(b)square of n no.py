#square of n numbers
n=int(input("enter the limit:"))
listi=[]
for i in range(1,n+1):
    listi.append(i)
print(listi)
newlist=[x**2 for x in listi]
print(newlist)
