'''
Plots all the CSV files from one experiment in the same file. Not very important. More of a test.
'''
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import glob

import numpy as np
import pandas as pd
print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp5(Leon_toilet_test)/Exp5,T-*.csv'))
filenames = sorted(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp5(Leon_toilet_test)/Exp5,T-*.csv'))
filenames = filenames[11:12]

x_list = list()

for filename in filenames:
  print(filename)
  x,y,z = np.loadtxt(filename, skiprows=1,
                     unpack = True,
                     delimiter= ',')
  # x_list.append(x)
  # print(type(x))
  # print(x)
  # print(y)
  plt.plot(x,y, color = "orange")
  plt.plot(x,z, color = "red")
plt.title("Weight vs Time")
plt.xlabel("Time")
plt.ylabel("Weight")
# y.mean(axis=-1)
plt.show()
#t = pd.read_csv('/Users/Leon/Documents/ToiletProjectUni2021/Experiment3(Leon_Standing2)/Experiment3,T-1.csv')
#t.head()

