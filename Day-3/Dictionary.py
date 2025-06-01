#dictionary


dict = {
    "name" : "Alfisha",
    "sem" : "2nd",
    "div" : "A",
    "Enroll_no" : "202403103510004",
    "subjects" : ["python", "c","calculus", "dlcd"],
    "age" : 18
}


print("Original Dictionary:")
print(dict)


print("Type:")
print(type(dict))


print()
print(dict["sem"])


print("Change division : ")
dict["div"] = "D"
print(dict)


print("Add CGPA :")
dict["CGPA"] = "9.55"
print(dict)


print("---------------Dictionary methods-------------------")


print("Dictionary keys")
print(dict.keys())


print("Dictionary values")
print(dict.values())


print("Dictionary items")
print(dict.items())


print("Key_name:")
print(dict.get("name"))


print("New key")
dict.update({"age" : "18"})
print(dict)


