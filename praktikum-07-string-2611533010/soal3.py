text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:11])

text = "Muhammad Farhan Amri"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)

