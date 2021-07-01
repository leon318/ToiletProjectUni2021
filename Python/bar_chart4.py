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
        a = df[(df['Person'] == names[i])]
        tot = a['Total_Weight'].mean()
        norm_floor_data = a['Floor_Weight']/tot
        norm_toilet_data = a['Toilet_Weight']/tot
        # print(f"{names[i]}, {positions[j]} :")
        mean_floor_data = norm_floor_data.mean()
        std_floor = norm_floor_data.std()
        mean_toilet_data = norm_toilet_data.mean()
        std_toilet = norm_toilet_data.std()
        if positions[j] == 'hunched':
            mean_list_hunched_floor.append(mean_floor_data)
            std_list_hunched_floor.append(std_floor)
            mean_list_hunched_toilet.append(mean_toilet_data)
            std_list_hunched_toilet.append(std_toilet)
        else:
            mean_list_straight_floor.append(mean_floor_data)
            std_list_straight_floor.append(std_floor)
            mean_list_straight_toilet.append(mean_toilet_data)
            std_list_straight_toilet.append(std_toilet)


x = np.arange(len(names))

width = 0.25
fig, ax = plt.subplots()
rects1 = ax.bar(x-width/2, mean_list_hunched_floor, width, label='Hunched Floor', yerr=std_list_hunched_floor)
rects2 = ax.bar(x+width/2, mean_list_hunched_toilet, width, label='Hunched Toilet', yerr=std_list_hunched_toilet)
rects3 = ax.bar(x - width / 2, mean_list_straight_floor, width, label='Straight Floor', yerr=std_list_straight_floor)
rects4 = ax.bar(x + width / 2, mean_list_straight_toilet, width, label='Straight Toilet', yerr=std_list_straight_toilet)
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.set_ylabel('Normalized Mean Weight')
ax.set_title('Normalized Mean Weight vs People in Hunched or Straight Positions')
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
ax.legend()
fig.tight_layout()
plt.show()