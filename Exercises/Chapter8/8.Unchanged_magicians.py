def show_magicians(magicians):
    """Display all magicians names."""

    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add the word great to the name string."""
    for i in range(len(magicians)):
        magicians[i] = "Great " + magicians[i]
    return magicians

magicians = ["Alfredo", "Pepito", "Juanito"]

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)

great_magicians = make_great(magicians[:])
make_great(magicians)
show_magicians(great_magicians)
