list1 = [1,2,3]
list2 = [1,2,3]
list3 = [1,2,3]
list4 = [1,2,3]
a = [4]
b = [4,5,6]

list1.append(a)
print('list1 append a :')
print(list1)

list2.append(b)
print('list2 append b :')
print(list2)

list3.extend(a)
print('list3 extend a :')
print(list3)

list4.extend(b)
print('list4 extend b :')
print(list4)
