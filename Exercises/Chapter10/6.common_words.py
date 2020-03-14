try:
    with open("lotin_avioliitto.txt") as lotin:
        text = lotin.read()
except FileNotFoundError:
    print("Could't open the Lotin file.")
else:
    print(str(text.lower().count("the")) + " the word")
