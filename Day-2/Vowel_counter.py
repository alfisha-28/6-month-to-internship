text = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"Vowels: {vowel_count}")

