with open("learning_python.txt") as file:
    """Simple program that reads and print a txt file."""

    file_lines = file.readlines()
    for i in range(0, 3):
        for line in file_lines:
            string = line.replace("Python", "Lola")
            print(string.strip())
