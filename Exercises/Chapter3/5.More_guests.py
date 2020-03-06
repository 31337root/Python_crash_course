# List of guests for a dinner

names = ["Lola", "Judi", "Hugo", "Roberto", "Roberta", "Pili"]

print("Te invito a que cenemos " + names[0])
print("Te invito a que cenemos " + names[1])
print("Te invito a que cenemos " + names[2])
print("Te invito a que cenemos " + names[3])
print("Te invito a que cenemos " + names[4])
print("Te invito a que cenemos " + names[5])

print(names[2] + " can't come with us")
del names[2]
names.insert(2, "José María")

print("Te invito a que cenemos " + names[0])
print("Te invito a que cenemos " + names[1])
print("Te invito a que cenemos " + names[2])
print("Te invito a que cenemos " + names[3])
print("Te invito a que cenemos " + names[4])
print("Te invito a que cenemos " + names[5])

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
