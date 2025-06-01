text = input("Enter some text: ")

digits = letters = spaces = symbols = 0

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
    elif ch.isspace():
        spaces += 1
    else:
        symbols += 1

print(f"Letters: {letters}, Digits: {digits}, Spaces: {spaces}, Symbols: {symbols}")
