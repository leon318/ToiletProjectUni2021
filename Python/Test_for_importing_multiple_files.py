import glob
from matplotlib import pyplot as plt
import numpy as np

print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T*'))
filenames = sorted(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T*'))
filenames = filenames[0:10]

for filename in filenames:
    print(filename)
    data = np.loadtxt(fname=filename, delimiter='\n')
    print(data)
    y = data
    plt.plot(y)
plt.title("Weight vs Measurements")
plt.xlabel("Measurements")
plt.ylabel("Weight")
plt.show()
