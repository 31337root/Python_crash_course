"""Program that ask for name and save it in a file."""

while True:
    name = input("Give me your name: ")

    if name:
        print("Thanks " + name + "!")
    with open("guest_book.txt", "a") as file_:
        file_.write(name + "\n")
