"""Program that ask why people like programming and save it in a file."""

while True:
    answer = input("Why you like programming? ")

    with open("answers.txt", "a") as file_:
        file_.write(answer + "\n")
