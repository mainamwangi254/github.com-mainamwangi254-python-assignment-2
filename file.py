my_list = []
my_list.extend([10, 20, 30, 40])
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()

index_of_30 = my_list.index(30)
print("index of 30 in my list:", index_of_30)

print("modified my_list:", my_list)