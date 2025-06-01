#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}


phy = int(input("Enter phy marks:"))
marks.update({"physics":phy})
chem = int(input("Enter chem marks:"))
marks.update({"chemistry":chem})
bio = int(input("Enter bio marks:"))
marks.update({"biology":bio})


print(marks)


