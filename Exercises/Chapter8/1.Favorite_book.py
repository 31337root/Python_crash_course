def favorite_book(title):
    """Display a simple message."""
    if title:
        print("One of my favorite book is " + str(title) + ".")
    else:
        print("Invalid argument")

favorite_book("Alice in Wonderland")
