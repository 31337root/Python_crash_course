"""Ask for the name and save it in a file."""

name = input("Give me your name: ")

with open("guest.txt", "a") as file:
    file.write(name + "\n")
