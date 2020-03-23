import matplotlib.pyplot as plt

input_values = list(range(1, 5001))
cubes = [x**3 for x in input_values]

plt.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Blues, s=40)

# Set chart and label axes.
plt.title("Cubes numbers", fontsize=24)
plt.xlabel("Number", fontsize=14)
plt.ylabel("Cube of number", fontsize=14)

plt.show()
