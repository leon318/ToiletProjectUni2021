from matplotlib import pyplot as plt
import numpy as np
import os

with open("Weightfile") as f:
    lines = f.readlines()  # read
lines[0] = ("0.0" + "\n")  # you can replace zero with any line number
with open("Weightfile", "w") as f:
    f.writelines(lines) #write back
data = np.loadtxt(fname='Weightfile', delimiter='\n')
print(data)
y = data
plt.plot(y)
plt.title("Weight vs Measurements")
plt.xlabel("Measurements")
plt.ylabel("Weight")
plt.show()
exit()