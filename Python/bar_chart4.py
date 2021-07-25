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

mean_list_hunched_floor = list()
mean_list_straight_floor = list()
mean_list_hunched_toilet = list()
mean_list_straight_toilet = list()
std_list_hunched_floor= list()
std_list_straight_floor = list()
std_list_hunched_toilet= list()
std_list_straight_toilet = list()
for i, name in enumerate(names):
    for j, position in enumerate(positions):
        a = df[(df['Person'] == names[i]) & (df['Position'] == positions[j])]
        print(a)
        tot = a['Total_Weight'].mean()
        norm_floor_data = a['Floor_Weight']/tot
        norm_toilet_data = a['Toilet_Weight']/tot
        print(f"{names[i]}, {positions[j]} :")
        print(norm_toilet_data)
        mean_floor_data = norm_floor_data.mean()
        std_floor = norm_floor_data.std()
        mean_toilet_data = norm_toilet_data.mean()
        std_toilet = norm_toilet_data.std()
        if positions[j] == 'hunched':
            mean_list_hunched_floor.append(mean_floor_data)
            std_list_hunched_floor.append(std_floor)
            mean_list_hunched_toilet.append(mean_toilet_data)
            std_list_hunched_toilet.append(std_toilet)
        elif positions[j] == 'straight':
            mean_list_straight_floor.append(mean_floor_data)
            std_list_straight_floor.append(std_floor)
            mean_list_straight_toilet.append(mean_toilet_data)
            std_list_straight_toilet.append(std_toilet)
# print(mean_list_hunched_toilet)
# print(mean_list_straight_toilet)
# print(mean_list_hunched_floor)
# print(mean_list_straight_floor)
x = np.arange(len(names))

width = 0.2
fig, ax = plt.subplots()
rects1 = ax.bar(x, mean_list_hunched_floor, width, label='Hunched Floor', yerr=std_list_hunched_floor, edgecolor='black', ecolor='black', capsize=5 )
rects2 = ax.bar(x+width, mean_list_hunched_toilet, width, label='Hunched Toilet', yerr=std_list_hunched_toilet, edgecolor='black', ecolor='black', capsize=5)
rects3 = ax.bar(x + (2*width), mean_list_straight_floor, width, label='Straight Floor', yerr=std_list_straight_floor, edgecolor='black', ecolor='black', capsize=5)
rects4 = ax.bar(x + (3*width), mean_list_straight_toilet, width, label='Straight Toilet', yerr=std_list_straight_toilet, edgecolor='black', ecolor='black', capsize=5)
ax.set_xticks(x + width + width/2)
ax.set_xticklabels(names)
ax.set_xlabel('People')
ax.set_ylabel('Normalized Mean Weight')
ax.set_title('Normalized Mean Weight vs People in Hunched or Straight Positions')
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
ax.legend()
fig.tight_layout()
plt.show()