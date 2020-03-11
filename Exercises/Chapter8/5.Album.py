def make_album(artist, title, tracks = ""):
    info = {}

    info["artist"] = artist
    info["title"] = title

    if tracks:
        info["tracks"] = tracks

    return info

print(make_album("Lola", "Lolas"))
print(make_album("Omar", "La vi"))
print(make_album("Roberto", "La locura de la genialidad", 9))

while True:
    print("Enter q to exit <------")
    artist = input("Give me an artist: ")
    if artist is "q":
        break
    title = input("Give me the album title: ")
    if title is "q":
        break
    tracks = input("Give me the number of tracks: ")
    if tracks is "q":
        break

    print(make_album(artist, title, tracks))
