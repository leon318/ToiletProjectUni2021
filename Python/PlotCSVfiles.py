import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import glob

import numpy as np
import pandas as pd
print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Experiment3(Leon_Standing2)/Experiment3,T-*.csv'))
filenames = sorted(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Experiment3(Leon_Standing2)/Experiment3,T-*.csv'))
filenames = filenames[0:5]

x_list = list()

for filename in filenames:
  print(filename)
  x,y = np.loadtxt(filename,
                     unpack = True,
                     delimiter= ',')
  x_list.append(x)
  print(type(x))
  print(x)
  print(y)
  plt.plot(x,y)
plt.title("Weight vs Time")
plt.xlabel("Time")
plt.ylabel("Weight")
y.mean(axis=-1)
plt.show()
#t = pd.read_csv('/Users/Leon/Documents/ToiletProjectUni2021/Experiment3(Leon_Standing2)/Experiment3,T-1.csv')
#t.head()

