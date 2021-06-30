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

    # if df.Person == 'aron':
df.Person.astype('category').cat.codes

plt.scatter(x=df.Position[0:19],
            y=df.Toilet_Weight,
            s=5,
            c = df.Person.astype('category').cat.codes,
            marker='v')

plt.scatter(x=df.Position,
            y=df.Floor_Weight,
            s=5,
            c = df.Person.astype('category').cat.codes,
            marker='s')

plt.scatter(x=df.Position,
            y=df.Total_Weight,
            s=5,
            c = df.Person.astype('category').cat.codes,
            marker='o')
plt.xlabel("Position")
plt.ylabel("Weight (kg)")
# if df['Person'].str.contains('aron').any():
#     print ("aron is there")
plt.legend(["Toilet_Weight", "Floor_Weight", "Total_Weight"], loc ="best")
# plt.legend([df.Person], loc = 'best')
# Create the figure
plt.show()
