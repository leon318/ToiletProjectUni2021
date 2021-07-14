
'''
Generates csv file. This CSV file is used to make the bar charts and the dot plots.
'''
import glob
import numpy as np

title = "Summary.csv"
#TODO Put names into alphabetical order
names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
columns = ['Person', 'Test', 'Position','Total_Weight', 'Floor_Weight', 'Toilet_Weight']

f = open(title, "w")
f.write(f"{','.join(columns)}\n")
files = (sorted(glob.glob("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction//*/*.csv")))
h = 0

for i, file in enumerate(files):
    x, y, z = np.loadtxt(file,
                         unpack=True,
                         delimiter=',',
                         skiprows=1)
    if names[h] not in file:
        h += 1

    name = names[h]
    position = 'hunched' if 'hunch' in file else 'straight'
    f.write(f"{name},{i},{position},{y[-1] + z[-1]:.3f},{y[-1]:.3f},{z[-1]:.3f}\n")
