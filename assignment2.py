mylist= [1,3,5,7,9]
mylist[2]=10
print(mylist[2])
mylist.append(12)
mylist.remove(mylist[2])
print(mylist)

sliced_list = mylist[1:3]
print(sliced_list)

combined_list = mylist+sliced_list
print(combined_list)

if 8 in combined_list:
    print("8 is there")
else:
    print("8 is not there")
print(sorted(combined_list))