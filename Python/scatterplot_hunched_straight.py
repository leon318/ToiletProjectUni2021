'''
scatter plot with hunched and straight on the x axis and the dots above. It is normalized.
'''

import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/Python/"
filename = "Summary.csv"
names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
color_list = ('purple','red','green','orange','blue')
fname = os.path.join(project_dir,
                     filename)

df = pd.read_csv(fname)

df['Position_Encoding'] = df['Position']

mapping = {"hunched": 2,
          "straight": 1,}
df = df.replace({"Position_Encoding": mapping})
print(df)
x = 1


color_dict = { 'anjany' : 'purple',
               'aron' : 'red',
               'kyriakos' : 'green',
               'leon' : 'orange',
               'matteo' : 'blue'}

names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
for i, name in enumerate(names):
    a = df[(df['Person'] == names[i])]
    plt.scatter(x=a.Position,
                y=a.Toilet_Weight/(a.Total_Weight),
                s=5,
                c= color_dict[name],
                marker='v',
                label = f"{names[i]}, Toilet Weight")

    plt.scatter(x=a.Position,
                y=a.Floor_Weight/(a.Total_Weight),
                s=5,
                c= color_dict[name],
                marker='s',
                label = f"{names[i]}, Floor Weight")

    # plt.scatter(x=a.Position,
    #             y=a.Total_Weight/(a.Total_Weight),
    #             s=5,
    #             c= color_dict[name],
    #             marker='o',
    #             label = f"{names[i]}, Total Weight")

plt.title("Normalized Weight Hunched vs Straight Scatterplot")
plt.xlabel("Position")
plt.ylabel("Weight (normalized)")
# # if df['Person'].str.contains('aron').any():
# #     print ("aron is there")
# plt.legend(["Toilet_Weight", "Floor_Weight", "Total_Weight"], loc ="best")
plt.legend(loc = "lower center")
plt.show()
