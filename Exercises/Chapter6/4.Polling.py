favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }
pool = ["Omar", "Lola", "sarah"]

for user in pool:
    if user in favorite_languages:
        print("Thanks " + user + " for taking the survey.")
    else:
        print("You " + user + " should respond our survey.")
