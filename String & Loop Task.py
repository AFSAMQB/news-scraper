text = input("Enter a string: ")
for i in range(len(text)):
    if text[i] == " ":
        continue
    if text[i] == "z":
        print("Found z, stopping loop")
        break
    print(i, ":", text[i])





