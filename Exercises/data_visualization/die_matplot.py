import matplotlib.pyplot as plt

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

options = [x for x in range(1, 7)]

plt.plot(options, frequencies, linewidth=5)


plt.show()
