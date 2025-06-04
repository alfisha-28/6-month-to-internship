with open("C:/6-Months-To-Internship/Day-5/input.txt", "r") as infile, open("C:/6-Months-To-Internship/Day-5/reversed.txt", "w") as outfile:
    for line in infile:
        line = line.rstrip()             # removes \n and extra spaces at end
        reversed_line = line[::-1]       # reverses the actual text
        outfile.write(reversed_line + "\n")  # adds newline back at end
