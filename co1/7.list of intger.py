list1=[10,8,6]
list2=[2,4,6,7,8,3]
l1=len(list1)
l2=len(list2)
sum1=0
sum2=0
#a)
if l1==l2:
    print("length of list1 and list2 is same")
else:
    print("length of list1 and list 2 is different")
#b)
for i in list1:
    sum1=sum1+i
for j in list2:
    sum2=sum2+i
if sum1==sum2:
    print("sum of 2 list is equal")
else:
    print("sum of 2 list is different")
#c)
for i in list1:
    for j in list2:
        if i==j:
            print(j,"occur in both")
