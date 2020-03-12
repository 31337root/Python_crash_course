def sandwiches(*items):
    """Print the items of a requested sandwich."""
    print("The sandwich will have:")
    for item in items:
        print("\t- " + item)

sandwiches("lola", "Chesse", "Tomato")
sandwiches("Potato", "Bread", "Water")
sandwiches("Omar")
