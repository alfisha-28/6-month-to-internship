#list
#lists are mutable
li = [23, 45, 89, 12, 37, 101, 44, 2]


print("Original list:")
print(li)


print("Type:")
print(type(li))


print("Length of list:")
print(len(li))


print("3rd element:")
print(li[2])


print("5th element:")
print(li[4])


print("5th element changed to:")
li[4] = 39
print(li)


#slicing
li1 = li[4:8]
print("Sliced list")
print(li1)


#list methods


li.append(4)
print("List after append:")
print(li)


li.sort()
print("List after sorting in ascending order:")
print(li)


li.sort(reverse=True)
print("List after sorting in descending order:")
print(li)


li.reverse()
print("List in reverse order:")
print(li)


li.insert(5, 100)
print("List after inserting new element:")
print(li)


li.remove(101)
print("List after removing an element")
print(li)


li.pop(5)
print("List after popping an element from index 5")
print(li)
