my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1,80)
my_list.extend([70,50,60])
del my_list[-1]
my_list.sort()
#my_list.remove(70)
print(my_list)
index=my_list.index(30)
print(index)