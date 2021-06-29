import glob
import os
import csv
import shutil
import numpy as np
from os import listdir
from os.path import isfile, join
Title = "Summary.csv"
f = open(Title, "w")
f.write(",".join(['Person', 'Test', 'Position','Total_Weight', 'Floor_Weight', 'Toilet_Weight']))
c = 0
h = 0
# project_dir_folders = glob.glob("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction" , recursive=True)
# project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction//**/*.csv"
# filename = "*.csv"
# foldername = "*)"
# number_of_files = 10
# number_of_folders = 10
# Name = 'Leon'
Names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
x_list = list()
y_list = list()
z_list = list()
# # -------------------- program ------------------------
# filenames = sorted(glob.glob(os.path.join(project_dir, filename)))
# filenames = filenames[0:number_of_files]
# foldernames = sorted(glob.glob("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction//**/*.csv"))
# foldernames = foldernames[0:number_of_folders]
#
# f.write('\n')
# for i, foldername in enumerate(foldernames):
#     print('hi')
#     for i, filename in enumerate(filenames):
#         f.write(",".join([Name, str(i+1), " "]))
#         if 'hunched' in filename:
#             f.write(",".join(['hunched',]))
#         elif 'straight' in filename:
#             f.write(",".join(['straight',]))
#         # f.write((filename[i]))
#         x, y, z = np.loadtxt(filename,
#                              unpack=True,
#                              delimiter=',',
#                              skiprows=1)
#         x_list.append(x)
#         y_list.append(y)
#         z_list.append(z)
#         f.write((",".join([" " , str(((y_list[i][-1] + z_list[i][-1]))), str(y_list[i][-1]),  str(z_list[i][-1])])))
#         f.write('\n')


files = (sorted(glob.glob("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction//*/*.csv")))
print(files[0:10])
file = '*.csv'
f.write('\n')
if 1:
    for i, file in enumerate(files):
        print(i)
        #print('\n')
        x, y, z = np.loadtxt(file,
                             unpack=True,
                             delimiter=',',
                             skiprows=1)
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        if Names[h] not in file:
            h += 1

        f.write(",".join([Names[h], str(i), " ",]))
        if 'hunch' in file:
            f.write(",".join(['hunched',]))
        elif 'straight' in file:
            f.write(",".join(['straight',]))
        f.write((",".join([" ", str(((y_list[i][-1] + z_list[i][-1]))), str(y_list[i][-1]), str(z_list[i][-1])])))
        f.write('\n')




    # while c > 10:
    #     h += 1
    #     c = 0
    # while c <= 10:
    #     while Names[h] in file:

    # f.write(",".join([Name, str(i + 1), " "]))
    #         if 'hunched' in filename:
    #             f.write(",".join(['hunched',]))
    #         elif 'straight' in filename:
    #             f.write(",".join(['straight',]))
    #         # f.write((filename[i]))
    #         x, y, z = np.loadtxt(filename,
    #                              unpack=True,
    #                              delimiter=',',
    #                              skiprows=1)
    #         x_list.append(x)
    #         y_list.append(y)
    #         z_list.append(z)

    #         f.write('\n')