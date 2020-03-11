def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "Great " + magicians[i]

magicians = ["Alfredo", "Pepito", "Juanito"]

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
