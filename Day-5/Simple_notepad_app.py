def add_note():
    note = input("Write your note: ")
    with open("C:/6-Months-To-Internship/Day-5/Notes.txt", "a") as file:
        file.write(note + "\n")

def read_notes():
    with open("C:/6-Months-To-Internship/Day-5/Notes.txt", "r") as file:
        print(file.read())

choice = input("Add or Read note? (a/r): ").lower()
if choice == 'a':
    add_note()
elif choice == 'r':
    read_notes()
