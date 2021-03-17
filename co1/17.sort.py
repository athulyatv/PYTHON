import operator
d={0:8,1:5,2:6,3:9,4:4,5:0}
acs=sorted(d.items(),key=operator.itemgetter(1))
print("ascending order",acs)
ds=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("descending order",ds)
