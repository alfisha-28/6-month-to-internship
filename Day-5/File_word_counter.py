from collections import Counter

with open("C:/6-Months-To-Internship/Day-5/sample.txt", "r") as file:
    text = file.read().lower()

words = text.split()
word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")  