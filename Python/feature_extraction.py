import glob
import numpy as np

title = "Summary.csv"
f = open(title, "w")
f.write(",".join(['Person', 'Test', 'Position','Total_Weight', 'Floor_Weight', 'Toilet_Weight']))
h = 0

#TODO Put names into alphabetical order
names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')

files = (sorted(glob.glob("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction//*/*.csv")))
print(files[0:10])
f.write('\n')
if 1:
    for i, file in enumerate(files):
        print(i)
        #print('\n')
        x, y, z = np.loadtxt(file,
                             unpack=True,
                             delimiter=',',
                             skiprows=1)
        if names[h] not in file:
            h += 1

        f.write(",".join([names[h], str(i)]))
        if 'hunch' in file:
            f.write(",hunched,")
        elif 'straight' in file:
            f.write(",straight,")
        f.write((",".join([str(((y[-1] + z[-1]))), str(y[-1]), str(z[-1])])))
        f.write('\n')