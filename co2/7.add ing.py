st=input("enter a string")
if(len(st)>2):
    if st[-3:]=='ing':
        st+='ly'
    else:
        st+='ing'
print(st)
