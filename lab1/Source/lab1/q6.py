import numpy as np
x = np.random.randint(21, size=15)
print(x)
counts = np.bincount(x)
print("Most frquent item in the list is", np.argmax(counts))