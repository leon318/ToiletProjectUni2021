''''
Plots vs measurements with only y data. Test not important
'''
import glob
from matplotlib import pyplot as plt
import numpy as np

print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Experiment3(Leon_Standing2)/Experiment3,T-*.csv'))
filenames = sorted(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Experiment3(Leon_Standing2)/Experiment3,T-*.csv'))
filenames = filenames[0:10]

for filename in filenames:
    print(filename)
    data = np.loadtxt(fname=filename, delimiter='\n')
    print(data)
    y = data

    plt.plot(y)
plt.title("Weight vs Measurements")
plt.xlabel("Time")
plt.ylabel("Weight")
plt.show()
