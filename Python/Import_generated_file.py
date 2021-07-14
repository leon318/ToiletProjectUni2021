'''
Test at the beginning. Not an important file.
'''
from matplotlib import pyplot as plt
import numpy as np
import glob
with open("/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T2") as f:
    lines = f.readlines()  # read
lines[0] = ("0.0" + "\n")  # you can replace zero with any line number
with open("/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T2", "w") as f:
    f.writelines(lines) #write back
data = np.loadtxt(fname='/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T2', delimiter='\n')
print(data)
y = data
plt.plot(y, 'r')
plt.title("Weight vs Measurements")
plt.xlabel("Measurements")
plt.ylabel("Weight")
plt.show()
exit()