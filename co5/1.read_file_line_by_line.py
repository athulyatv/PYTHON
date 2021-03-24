l = list()
f = open("demo.txt", "w")
n = int(input("Enter the number of lines:"))
for i in range(n):
    f.write(input("Enter some text:")+"\n")
f.close()
f = open("demo.txt", "r")
for i in f:
    print(i)
    l.append(i[:-1])
f.close()
print(l)
