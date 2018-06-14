# import numpy
import numpy as np
# Create random integers of size 15 between 0 and 20
x = np.random.randint(21, size=15)
print(x)
# Counting the frequent occurences of a number
counts = np.bincount(x)
print("Most frquent item in the list is", np.argmax(counts))
