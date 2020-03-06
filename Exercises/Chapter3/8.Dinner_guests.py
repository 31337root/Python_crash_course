# List of guests for a dinner

names = ["Lola", "Judi", "Hugo", "Roberto", "Roberta", "Pili"]

print("Te invito a que cenemos " + names[0])
print("Te invito a que cenemos " + names[1])
print("Te invito a que cenemos " + names[2])
print("Te invito a que cenemos " + names[3])
print("Te invito a que cenemos " + names[4])
print("Te invito a que cenemos " + names[5])

print(str(len(names)) + " were invited")

print(names[2] + " can't come with us")
del names[2]
names.insert(2, "José María")

print("Te invito a que cenemos " + names[0])
print("Te invito a que cenemos " + names[1])
print("Te invito a que cenemos " + names[2])
print("Te invito a que cenemos " + names[3])
print("Te invito a que cenemos " + names[4])
print("Te invito a que cenemos " + names[5])

print(str(len(names)) + " ºwere invited")

print("\nWe found a bigest tatble, let's invite more people")
names.insert(0, "Juliette")
names.insert(3, "Omar")
names.append("Perro")

print("Te invito a que cenemos " + names[0])
print("Te invito a que cenemos " + names[1])
print("Te invito a que cenemos " + names[2])
print("Te invito a que cenemos " + names[3])
print("Te invito a que cenemos " + names[4])
print("Te invito a que cenemos " + names[5])
print("Te invito a que cenemos " + names[6])
print("Te invito a que cenemos " + names[7])
print("Te invito a que cenemos " + names[8])

print(str(len(names)) + " were invited")

print("\nWe can invite only two, sorry everyone")
print("Bye " + names.pop(0))
print("Bye " + names.pop(1))
print("Bye " + names.pop(2))
print("Bye " + names.pop(2))
print("Bye " + names.pop(2))
print("Bye " + names.pop(2))
print("Bye " + names.pop(2))

print("\nSee ya in the party " + names[0])
print("See ya in the party " + names[1])

print(str(len(names)) + " were invited")

del names[1]
del names[0]

print(names)
