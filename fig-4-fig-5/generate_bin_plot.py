import matplotlib.pyplot as plt
import numpy as np

lengths = []

# read in element lengths. This file should only contain the length of each element, separated by newlines
with open("all_element_lengths_joined_filtered.txt") as input:
    for line in input:
        lengths.append(int(line.strip()))

#lengths.sort()

lengths_array = np.array(lengths)

print(f"Min: {lengths_array.min()}")
print(f"Max: {lengths_array.max()}")
print(f"Mean: {lengths_array.mean()}")
print(f"Median: {np.median(lengths_array)}")

fig, ax = plt.subplots()

plt.hist(lengths_array, "auto", edgecolor='white')
plt.xlabel("Integration Length")
plt.ylabel("Count (log)")
plt.yscale("log")
plt.title("Binned Integration Lengths")
ax.xaxis.set_major_locator(plt.MaxNLocator(40))
ticks = plt.xticks(rotation=45)
plt.show()