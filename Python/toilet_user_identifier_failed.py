'''
This code is unimportant since it failed.
'''

import glob
import numpy as np
import matplotlib.pyplot as plt
import os

from processing_functions_for_user_identification.unpacking_the_data import unpack_and_append_data3
from processing_functions_for_user_identification.threshold_locators_and_trimmers import threshold_locater_and_posterior_trimmer3
from processing_functions_for_user_identification.finding_shortest_length import find_shortest_length
from processing_functions.theshold_locator_and_trimmers import anterior_trimmer_x_and_y_and_z
from processing_functions.math import total_and_averager_y_and_z
from processing_functions.math import std_calculator_y_and_z
from processing_functions.Plotter import matplotlib_plotter_with_z_no_std

#Todo 1. Normalize the individual curves to the last value of the calculated total body weight. DONE
#TODO 2. Write a function that takes one experiment(3 curves) and returns the first time points (indexes) where the weight is not ~0 for each 3 curves(total,floor,seat)
# Hint: define a threshold value for the non-zero value (e.g. ~0.5kg) and start to interate through the data points until the
# current value > threshold

# -------------------- user input ------------------------
project_dir_1 = "/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction"
project_dir_list2 = ("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/anjany(straight)","/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/aron(straight)","/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/kyriakos(straight)","/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/leon(straight)","/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/matteo(straight)")
label_list = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
filename = "*.csv"
number_of_files = 10
weight_threshold = .05
# -------------------- program ------------------------
# print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))

names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
color_list = ('purple','red','green','orange','blue')
# files = (sorted(glob.glob("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction//*/*.csv")))
# filenames = sorted(glob.glob(os.path.join(project_dir1, project_dir2[0], filename)))
# print(filenames[0])
# for i, q in enumerate(project_dir_list2):
x_listy = list()  # This is where all the x arrays of data are uploaded
x_listz = list()
y_list = list()  # This is where all the y arrays of data are uploaded
z_list = list()
res_list = list()  # This is used to list all the indexes for weight values above .weight threshhold.
# All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
final_0_list = list()  # This is used to list the smallest index from each array of indexes over weight_threshold. This takes the smallest values from each array
# and puts it in a list.
original_length_listxy = list()
original_length_listxz = list()
modifiedx_length_list = list()
modifiedy_length_list = list()
modifiedz_length_list = list()
totaly = 0  # This is to add all the y lists into one array
totalz = 0
filenames = sorted(glob.glob(os.path.join(project_dir_list2[0], filename)))
filenames = filenames[0:number_of_files]
x_listy, x_listz, y_list, z_list = unpack_and_append_data3(filenames, x_listy, x_listz, y_list, z_list)
x_listy, x_listz, y_list, z_list = threshold_locater_and_posterior_trimmer3(x_listy, x_listz, y_list, z_list, weight_threshold)
d,g = find_shortest_length(filenames, original_length_listxy, original_length_listxz, x_listy, x_listz)
x_axis, x_list, y_list, z_list, modifiedx_length_list, modifiedy_length_list, modifiedz_length_list = anterior_trimmer_x_and_y_and_z(d, x_list, y_list, z_list, modifiedx_length_list, modifiedy_length_list, modifiedz_length_list)


    # totaly, totalz, averagey, averagez = total_and_averager_y_and_z(y_list, z_list, totaly, totalz)
    # stdy, stdz, above_stdy, below_stdy, above_stdz, below_stdz = std_calculator_y_and_z(averagey, averagez, y_list, z_list)
    # matplotlib_plotter_with_z_no_std(x_axis, averagey, averagez, color = color_list[i], filler = label_list[i])
    # plt.legend(loc="best")
    # plt.title("Weight vs Time (ms) Normalized (Straight)")
    # plt.xlabel("Time (ms)")
    # plt.ylabel("Weight")
    # plt.show()