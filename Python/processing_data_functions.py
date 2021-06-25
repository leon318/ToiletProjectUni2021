import glob
import numpy as np
import matplotlib.pyplot as plt
import os
#Functions
# -------------------- user input ------------------------
project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)"
filename = "Exp4,T-*.csv"
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

project_dir2 = "/Users/Leon/Documents/ToiletProjectUni2021/exp6(Leon_toilet_sitting)"
filename2 = "Exp6T-*.csv"
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

def unpack_and_append_data(filenames, x_list, y_list, skiprow = 0):
    for filename in filenames:
        x, y = np.loadtxt(filename,
                          unpack=True,
                          delimiter=',',
                          skiprows=skiprow)

        x_list.append(x)
        y_list.append(y)
    return x_list, y_list
def threshold_locater_and_posterior_trimmer(x_list, y_list,weight_threshold,):
    for i, y in enumerate(y_list):
        res = np.argmax(y >= weight_threshold)
        y_list[i] = y[res:]
        x_list[i] = x_list[i][res:]
    return x_list, y_list
def find_shortest_length(filenames, original_length_list, x_list):
    for idx, filename in enumerate(filenames): #This prints the length of both the x and y files. This will allow us to cut away from the end so they
        original_length_list.append(len(x_list[idx])) #This puts the length of each x file into another list. Its the same for the y.
    d = min(original_length_list) #This defines
    # print(d)
    return d
def anterior_trimmer_x(d, x_list, modifiedx_length_list):
    for i, x in enumerate(x_list): #
        x_list[i]= x[:d]
        modifiedx_length_list.append(len(x_list[i]))
        x_axis = x_list[i]-min(x_list[i])
    return x_axis, x_list, modifiedx_length_list
def anterior_trimmer_y(d, x_list, y_list, modifiedy_length_list):
    for i, y in enumerate(y_list):
        y_list[i] = y[:d]
        modifiedy_length_list.append(len(x_list[i]))
    return y_list, modifiedy_length_list

def total_and_averager(y_list,total):
    for idx, y in enumerate(y_list):
        total = y_list[idx]+total
    average = total/len(y_list)
    return total, average
def std_calculator(average, y_list):
    array = np.column_stack(y_list)
    std = np.std(array, axis = 1)
    above_std = average + std
    below_std = average - std
    return std, above_std, below_std


def matplotlib_plotter(x_axis, above_std, below_std, average, color = 'orange', alpha =.25):
    plt.plot(x_axis, average,
             color=color)  # This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
    plt.plot(x_axis, above_std, color=color, alpha= alpha)  # Below plots the standard deviation in orange
    plt.plot(x_axis, below_std, color=color, alpha=alpha)
    plt.fill_between(x_axis, average, below_std, color=color, alpha=alpha)
    plt.fill_between(x_axis, average, above_std, color= color, alpha=alpha)

x_list, y_list = unpack_and_append_data(filenames, x_list, y_list)
x_list, y_list = threshold_locater_and_posterior_trimmer(x_list, y_list, weight_threshold)
d = find_shortest_length(filenames, original_length_list, x_list)
x_axis, x_list, modifiedx_length_list = anterior_trimmer_x(d, x_list, modifiedx_length_list)
y_list, modifiedy_length_list = anterior_trimmer_y(d, x_list, y_list, modifiedy_length_list)
total, average = total_and_averager(y_list,total)
std, above_std, below_std = std_calculator(average, y_list)
matplotlib_plotter(x_axis, above_std, below_std, average)

x_list2, y_list2 = unpack_and_append_data(filenames2, x_list2, y_list2, skiprow = 1)
x_list2, y_list2 = threshold_locater_and_posterior_trimmer(x_list2, y_list2, weight_threshold)
d2 = find_shortest_length(filenames2, original_length_list2, x_list2)
print(d2)
x_axis2, x_list2, modifiedx_length_list2 = anterior_trimmer_x(d2, x_list2,modifiedx_length_list2)
print(modifiedx_length_list2)
y_list2, modifiedy_length_list2 = anterior_trimmer_y(d2, x_list2, y_list2, modifiedy_length_list2)
print(modifiedy_length_list2)
total2, average = total_and_averager(y_list2, total2)
std, above_std, below_std = std_calculator(average, y_list2)
matplotlib_plotter(x_axis2, above_std, below_std, average, color = 'blue', alpha =.25)
#
plt.show()


