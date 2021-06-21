from matplotlib import pyplot as plt
import numpy as np
data = np.loadtxt(fname= 'Weaightfile', delimiter= '\n')
print(data)

y = data
plt.plot(y)
plt.title("Weight vs Measurements")
plt.xlabel("Measurements")
plt.ylabel("Weight")
plt.show()
exit()