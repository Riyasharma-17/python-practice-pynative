text = input("Enter a string: ")

for i in range(len(text)):
    if i % 2 == 0:
        print("Character at even index", i, ":", text[i])
