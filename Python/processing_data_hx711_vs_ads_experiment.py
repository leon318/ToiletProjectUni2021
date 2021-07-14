'''
This program was used to plot the results of 4 experiments on the same graph. It is not setup for the hunch and straight experiment
rather only the experiment where you get on and get off either the toilet scale or the floor scale. It uses functions however which can be reused.
'''



import glob
import numpy as np
import matplotlib.pyplot as plt
import os
from Python.processing_functions.Plotter import matplotlib_plotter
from Python.processing_functions.unpacking_data import unpack_and_append_data
from Python.processing_functions.theshold_locator_and_trimmers import threshold_locater_and_posterior_trimmer
from Python.processing_functions.find_shortest_length import find_shortest_length
from Python.processing_functions.theshold_locator_and_trimmers import anterior_trimmer_x_and_y
from Python.processing_functions.math import total_and_averager
from Python.processing_functions.math import std_calculator
#Functions
# -------------------- user input ------------------------
project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/exp1(floorads)"
filename = "exp1(floorads)T-*.csv"
number_of_files = 8
weight_threshold = .05
# -------------------- program ------------------------
# print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames = sorted(glob.glob(os.path.join(project_dir, filename)))
filenames = filenames[0:number_of_files]

x_list = list() #This is where all the x arrays of data are uploaded
y_list = list() #This is where all the y arrays of data are uploaded
res_list = list() #This is used to list all the indexes for weight values above .weight threshhold.
# All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
final_0_list = list()   #This is used to list the smallest index from each array of indexes over weight_threshold. This takes the smallest values from each array
# and puts it in a list.
original_length_list = list()
modifiedx_length_list = list()
modifiedy_length_list = list()
total = 0 #This is to add all the y lists into one array

project_dir2 = "/Users/Leon/Documents/ToiletProjectUni2021/exp2(toilethx711)"
filename2 = "exp2(toilethx711)T-*.csv"
number_of_files2 = 10
weight_threshold = .05
# -------------------- program ------------------------
# print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames2 = sorted(glob.glob(os.path.join(project_dir2, filename2)))
filenames2 = filenames2[0:number_of_files2]

x_list2 = list() #This is where all the x arrays of data are uploaded
y_list2 = list() #This is where all the y arrays of data are uploaded
res_list2 = list() #This is used to list all the indexes for weight values above .weight threshhold.
# All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
final_0_list2 = list()   #This is used to list the smallest index from each array of indexes over weight_threshold. This takes the smallest values from each array
# and puts it in a list.
original_length_list2 = list()
modifiedx_length_list2 = list()
modifiedy_length_list2 = list()
total2 = 0 #This is to add all the y lists into one array

project_dir3 = "/Users/Leon/Documents/ToiletProjectUni2021/exp3(floorhx711)"
filename3 = "exp3(floorhx711)T-*.csv"
number_of_files3 = 10
weight_threshold = .05
# -------------------- program ------------------------
# print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames3 = sorted(glob.glob(os.path.join(project_dir3, filename3)))
filenames3 = filenames3[0:number_of_files3]

x_list3 = list() #This is where all the x arrays of data are uploaded
y_list3 = list() #This is where all the y arrays of data are uploaded
res_list3 = list() #This is used to list all the indexes for weight values above .weight threshhold.
# All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
final_0_list3 = list()   #This is used to list the smallest index from each array of indexes over weight_threshold. This takes the smallest values from each array
# and puts it in a list.
original_length_list3 = list()
modifiedx_length_list3 = list()
modifiedy_length_list3 = list()
total3 = 0 #This is to add all the y lists into one array

project_dir4 = "/Users/Leon/Documents/ToiletProjectUni2021/exp4(toiletads)"
filename4 = "exp4(toiletads)T-*.csv"
number_of_files4 = 10
weight_threshold = .05
# -------------------- program ------------------------
# print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames4 = sorted(glob.glob(os.path.join(project_dir4, filename4)))
filenames4 = filenames4[0:number_of_files4]

x_list4 = list() #This is where all the x arrays of data are uploaded
y_list4 = list() #This is where all the y arrays of data are uploaded
res_list4 = list() #This is used to list all the indexes for weight values above .weight threshhold.
# All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
final_0_list4 = list()   #This is used to list the smallest index from each array of indexes over weight_threshold. This takes the smallest values from each array
# and puts it in a list.
original_length_list4 = list()
modifiedx_length_list4 = list()
modifiedy_length_list4 = list()
total4 = 0 #This is to add all the y lists into one array


x_list, y_list = unpack_and_append_data(filenames, x_list, y_list)
x_list, y_list = threshold_locater_and_posterior_trimmer(x_list, y_list, weight_threshold)
d = find_shortest_length(filenames, original_length_list, x_list)
x_axis, x_list, y_list, modifiedx_length_list, modifiedy_length_list = anterior_trimmer_x_and_y(d, x_list, y_list, modifiedx_length_list, modifiedy_length_list)
total, average = total_and_averager(y_list,total)
std, above_std, below_std = std_calculator(average, y_list)
matplotlib_plotter(x_axis, above_std, below_std, average, label = "floorADS1232")
#
x_list2, y_list2 = unpack_and_append_data(filenames2, x_list2, y_list2, skiprow = 1)
x_list2, y_list2 = threshold_locater_and_posterior_trimmer(x_list2, y_list2, weight_threshold)
d2 = find_shortest_length(filenames2, original_length_list2, x_list2)
print(d2)
x_axis2, x_list2, y_list2, modifiedx_length_list2, modifiedy_length_list2 = anterior_trimmer_x_and_y(d2, x_list2, y_list2, modifiedx_length_list2, modifiedy_length_list2)
print(modifiedx_length_list2)
print(modifiedy_length_list2)
total2, average = total_and_averager(y_list2, total2)
std, above_std, below_std = std_calculator(average, y_list2)
matplotlib_plotter(x_axis2, above_std, below_std, average, color = 'blue', alpha =.25, label="toiletHX711")
#
x_list3, y_list3 = unpack_and_append_data(filenames3, x_list3, y_list3, skiprow = 1)
x_list3, y_list3 = threshold_locater_and_posterior_trimmer(x_list3, y_list3, weight_threshold)
d3 = find_shortest_length(filenames3, original_length_list3, x_list3)
print(d3)
x_axis3, x_list3, y_list3, modifiedx_length_list3, modifiedy_length_list3 = anterior_trimmer_x_and_y(d3, x_list3, y_list3, modifiedx_length_list3, modifiedy_length_list3)
print(modifiedx_length_list3)
print(modifiedy_length_list3)
total3, average = total_and_averager(y_list3, total3)
std, above_std, below_std = std_calculator(average, y_list3)
matplotlib_plotter(x_axis3, above_std, below_std, average, color = 'green', alpha =.25, label="floorHX711")
#
x_list4, y_list4 = unpack_and_append_data(filenames4, x_list4, y_list4, skiprow = 1)
x_list4, y_list4 = threshold_locater_and_posterior_trimmer(x_list4, y_list4, weight_threshold)
d4 = find_shortest_length(filenames4, original_length_list4, x_list4)
print(d4)
x_axis4, x_list4, y_list4, modifiedx_length_list4, modifiedy_length_list4 = anterior_trimmer_x_and_y(d4, x_list4, y_list4, modifiedx_length_list4, modifiedy_length_list4)
total4, average = total_and_averager(y_list4, total4)
std, above_std, below_std = std_calculator(average, y_list4)
matplotlib_plotter(x_axis4, above_std, below_std, average, color = 'black', alpha =.25, label="toiletADS1232")

plt.legend(loc="best")
plt.title("Weight (kg) vs Time (ms) ")
plt.xlabel("Time (ms)")
plt.ylabel("Weight (kg)")
plt.show()
#
