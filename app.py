print("Wellcome this is a test file!")
name = input("Please enter your name: ")
print("Your name will never be the same!")
reverse_name=""
for ch in range(len(name)-1, -1, -1):
    reverse_name += name[ch]
    print(name[ch])
reverse_name = reverse_name.lower()
reverse_name = reverse_name.capitalize()
print("From now on, you are to be called:", reverse_name)
satisfied = input("Satisfied? (y,n)")
if satisfied == "y" :
    print("Goodbye {}, have a great life!".format(reverse_name))
else:
    new_name = "Đoka"
    print(f"Best we call you {new_name} then!")
    print("Goodbye {}, have a great life!".format(new_name))
