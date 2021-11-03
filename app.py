print("Wellcome this is a test file!")
name = input("Please enter your name: ")
print("Your name will never be the same!")
reverse_name=""
for ch in range(len(name)-1, -1, -1):
    reverse_name += name[ch]
    print(name[ch])
print("From now on, you are to be called:", reverse_name)
