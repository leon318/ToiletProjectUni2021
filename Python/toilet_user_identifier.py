import glob
import numpy as np
import matplotlib.pyplot as plt
import os

from processing_functions.unpacking_data import unpack_and_append_data3
from processing_functions.theshold_locator_and_trimmers import threshold_locater_and_posterior_trimmer3
from processing_functions.find_shortest_length import find_shortest_length
from processing_functions.theshold_locator_and_trimmers import anterior_trimmer_x_and_y_and_z
from processing_functions.math import total_and_averager_y_and_z
from processing_functions.math import std_calculator_y_and_z
from processing_functions.Plotter import matplotlib_plotter_with_z_no_std
#Functions
# -------------------- user input ------------------------
project_dir_1 = "/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction"
project_dir_list2 = ("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/anjany(straight)","/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/aron(straight)","/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/kyriakos(straight)","/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/leon(straight)","/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/matteo(straight)")
label_list = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
filename = "*.csv"
number_of_files = 10
weight_threshold = .05
# -------------------- program ------------------------
# print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
g = 0
names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
color_list = ('purple','red','green','orange','blue')
# files = (sorted(glob.glob("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction//*/*.csv")))
# filenames = sorted(glob.glob(os.path.join(project_dir1, project_dir2[0], filename)))
# print(filenames[0])
#Todo 1. Normalize the individual curves to the last value of the calculated total body weight. DONE
#TODO 2. Write a function that takes one experiment(3 curves) and returns the first time points (indexes) where the weight is not ~0 for each 3 curves(total,floor,seat)
# Hint: define a threshold value for the non-zero value (e.g. ~0.5kg) and start to interate through the data points until the
# current value > threshold DONE
#TODO 3
max_value_storage = ([])
max_value_location_storage = ([])
stabilize_value_storage = ([])
stabilize_location_storage = ([])
def threshold_finder(y_list, z_list):
    for i, y in enumerate(y_list):
        resy = np.argmax(y >= weight_threshold)
    for i, z in enumerate(z_list):
        resz = np.argmax(z >= weight_threshold)
        # print(resy, resz)
    return resy, resz
def total_weight_calculator(y_list, z_list, total_list):
    for i, y in enumerate(y_list):
        a= y_list[i]+z_list[i]
        total_list.append(a)
    return total_list
def normalizer(total_list, y_list,z_list):
    for i, y in enumerate(y_list):
        y_list[i] = y_list[i]/total_list[i][-1]
        z_list[i] = z_list[i]/total_list[i][-1]
        total_list[i] = total_list[i]/total_list[i][-1]
    return total_list, y_list, z_list
def max_values(total_list, y_list,z_list):
    for i, y in enumerate(y_list):
        max_floor = np.amax(y_list[i])
        max_floor_loc = np.argmax(y_list[i])
        # print(max_floor, max_floor_loc)

        max_total = np.amax(total_list[i])
        max_total_loc = np.argmax(total_list[i])
        # print(max_total, max_total_loc)

        max_toilet = np.amax(z_list[i])
        max_toilet_loc = np.argmax(z_list[i])
        # print(max_toilet, max_toilet_loc)
        max_value_storage.append([max_total,max_floor,max_toilet])
        max_value_location_storage.append([max_total_loc, max_floor_loc, max_toilet_loc])
        # print(max_value_storage)
    return max_value_storage, max_value_location_storage
def stabilize_location(total_list):
    for i, t in enumerate(total_list):
        for idx,element in reversed(list(enumerate(total_list[i]))):
           stabilizer = abs(total_list[i][idx]-total_list[i][idx-1])
           # print(i, idx, stabilizer)
           if stabilizer > .05:
               # print(i, idx+1, element)
               stabilize_value_storage.append([element])
               stabilize_location_storage.append([idx])
               break
    print(stabilize_value_storage)
    print(stabilize_location_storage)
    return stabilize_value_storage, stabilize_location_storage
def hunch_vs_straight(filenames):
    if 'straight' in filenames:
        y_array = [0, 1]
    elif 'hunch' in filenames:
        y_array = [1,0]

           # while g == 0:
           #     if stabilizer < .1:
           #         print(element)
           #     if stabilizer > .1:
           #         print(idx, element)
           #         g=1
x_list = list()  # This is where all the x arrays of data are uploaded
y_list = list()  # This is where all the y arrays of data are uploaded
z_list = list()
total_list = list()
res_list = list()  # This is used to list all the indexes for weight values above .weight threshhold.
# All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
final_0_list = list()  # This is used to list the smallest index from each array of indexes over weight_threshold. This takes the smallest values from each array
# and puts it in a list.
original_length_list = list()
modifiedx_length_list = list()
modifiedy_length_list = list()
modifiedz_length_list = list()
totaly = 0  # This is to add all the y lists into one array
totalz = 0
filenames = sorted(glob.glob(os.path.join(project_dir_list2[0], filename)))
filenames = filenames[0:number_of_files]
# print(filenames)
x_list, y_list, z_list = unpack_and_append_data3(filenames, x_list, y_list, z_list)
resy, resz = threshold_finder(y_list, z_list)
x_list, y_list, z_list = threshold_locater_and_posterior_trimmer3(x_list, y_list, z_list, weight_threshold)
d = find_shortest_length(filenames, original_length_list, x_list)
x_axis, x_list, y_list, z_list, modifiedx_length_list, modifiedy_length_list, modifiedz_length_list = anterior_trimmer_x_and_y_and_z(d, x_list, y_list, z_list, modifiedx_length_list, modifiedy_length_list, modifiedz_length_list)
total_list = total_weight_calculator(y_list, z_list, total_list)
total_list, y_list, z_list = normalizer(total_list, y_list,z_list)
max_value_storage, max_value_location_storage = max_values(total_list, y_list,z_list)
stabilize_value_storage, stabilize_location_storage = stabilize_location(total_list)
stabilize_value_storage, stabilize_location_storage = stabilize_location(y_list)
stabilize_value_storage, stabilize_location_storage = stabilize_location(z_list)

plt.plot(x_axis, y_list[6], color = 'blue', label = 'floor_scale')
plt.plot(x_axis, z_list[6], color = 'orange', label = 'toilet_weight')
#This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
plt.plot(x_axis, total_list[6], color = 'red', label = 'total_weight')

plt.title("Weight (kg) vs Time (ms) (Hunched Posture Aron)")
plt.xlabel("Time (ms)")
plt.ylabel("Weight (kg)")
plt.legend(loc="best")

plt.show()
#


#
# totaly, totalz, averagey, averagez = total_and_averager_y_and_z(y_list, z_list, totaly, totalz)
#
# #
# def destabilizer_finder(y_list, z_list):
#     for i, y in reversed(y_list):
#         abs(current_value - last_value) > threshold
#     for i, z in enumerate(z_list):
#         resz = np.argmax(z >= weight_threshold)
#         print(resy, resz)
#     return resy, resz
#
