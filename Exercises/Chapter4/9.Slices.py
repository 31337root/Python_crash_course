cubes = [cube**3 for cube in range(1, 11)]

print(cubes)

for cube in cubes[:3]:
    print(cube)
for cube in cubes[3:7]:
    print(cube)
for cube in cubes[-3:]:
    print(cube)
