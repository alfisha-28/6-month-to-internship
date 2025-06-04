source = "C:/6-Months-To-Internship/Day-5/Original.txt"
destination = "C:/6-Months-To-Internship/Day-5/Copy.txt"

with open(source, "r") as src, open(destination, "w") as dest:
    dest.write(src.read())
