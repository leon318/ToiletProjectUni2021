'''
This program makes a bar chart showing the difference between the Toilet and Floor scale weight in each position for each person.
It imports a CSV file from tbe average_weight_csv_generator program.
'''
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/Python/"
filename = "Summary.csv"
names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
color_list = ('purple','red','green','orange','blue')
fname = os.path.join(project_dir,
                     filename)



df = pd.read_csv(fname)
names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
positions = ('hunched', 'straight')

mean_list_hunched = list()
mean_list_straight = list()
std_list_hunched= list()
std_list_straight = list()
for i, name in enumerate(names):
    for j, position in enumerate(positions):
        a = df[(df['Person'] == names[i]) & (df['Position'] == positions[j])]
        tot = a['Total_Weight'].mean()
        normf = a['Floor_Weight']/tot
        normt = a['Toilet_Weight']/tot
        # print(f"{names[i]}, {positions[j]} :")
        dif = normt - normf
        difmean = dif.mean()
        std = dif.std()
        if positions[j] == 'hunched':
            mean_list_hunched.append(difmean)
            std_list_hunched.append(std)
        else:
            mean_list_straight.append(difmean)
            std_list_straight.append(std)

print(mean_list_hunched)
print(mean_list_straight)

x = np.arange(len(names))

width = 0.25
fig, ax = plt.subplots()
rects1 = ax.bar(x-width/2, mean_list_hunched, width, label='Hunched', yerr=std_list_hunched)
rects2 = ax.bar(x+width/2, mean_list_straight, width, label='Straight', yerr=std_list_straight)
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.set_ylabel('Average difference between Toilet Scale and Floor Scale Weight')
ax.set_title('Average diff btw Toilet and Floor Scale Weight vs People (Hunched/Straight)')
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
ax.legend()
fig.tight_layout()
plt.show()