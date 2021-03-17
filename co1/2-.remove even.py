list = [10,13,25,30,33,15]
print(list)
for i in list:
  if(i%2==0):
      list.remove(i)
print("list after removing EVEN numbers:")
print(list)
