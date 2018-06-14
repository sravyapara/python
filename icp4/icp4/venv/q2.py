# import numpy
import numpy as np
# Creating a Random Matrix of size 10*10
x=np.random.random((10, 10))
print(x)
# Prints max value in all the rows
print("Max values in each row are",x.max(1))
# Prints min value in all the rows
print("Min values in each row are",x.min(1))