#TUPLES
#Tuples are immutable
tup = (23, 45, 89, 12, 37, 101, 44, 2, 45)


print("Original tuple:")
print(tup)


print("Type:")
print(type(tup))


print("Length of tuple:")
print(len(tup))


print("3rd element:")
print(tup[2])


print("5th element:")
print(tup[4])


#slicing
tup1 = tup[4:8]
print("Sliced tuple")
print(tup1)


#tuple methods


print("Index no of element 101 is:")
print(tup.index(101))


print("Count of 45 is:")
print(tup.count(45))

