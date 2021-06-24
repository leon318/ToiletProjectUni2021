"""
Processes all the data by cutting out zeros and making an average graph
"""
import glob
import numpy as np
import matplotlib.pyplot as plt
import os
# -------------------- user input ------------------------
project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)"
filename = "Exp4,T-*.csv"
number_of_files_plus_one = 8
weight_threshold = .05
# -------------------- program ------------------------
# TODO Simplify path to Files in a variable (os)
# print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames = sorted(glob.glob(os.path.join(project_dir, filename)))
filenames = filenames[0:number_of_files_plus_one]

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
for filename in filenames: #This forloop opens up all the files from the experiment and puts the time in the x and the weight in
    # the y. It then adds it to the x list and the y list. In the end, you have multiple arrays with in a list
  #print(filename)
  x,y = np.loadtxt(filename,
                     unpack = True,
                     delimiter= ',')

  x_list.append(x)
  y_list.append(y)
 # print(x_list)
###################################################

for i, y in enumerate(y_list):
    res = np.argmax(y >= weight_threshold)
    y_list[i] = y[res:]
    x_list[i] = x_list[i][res:]

# for i, x in enumerate(x_list):
#  x_list[i] = x[(len(x_list[i]) - len(y_list[i])):] #I did this wierd thing since there was a glitch that made the corresponging x and y parts different
#     # print(len(y_list[i]))
#     # print(len(x_list[i]))

# # #Todo enumerate instead of a counter
# for idx, filename in enumerate(filenames): #This prints the length of both the x and y files. This will allow us to cut away from the end so they
#     # are all the same length.
#     # print(len(x_list[idx]))
#     # print(len(y_list[idx]))
#     original_length_list.append(len(x_list[idx])) #This puts the length of each x file into another list. Its the same for the y.
# d = min(original_length_list) #This defines
# # print(d)
# #   ###################################################
# for i, x in enumerate(x_list): #
#     x_list[i]= x[:d]
#     modifiedx_length_list.append(len(x_list[i]))
#     x_axis = x_list[i]-min(x_list[i])
# #print(x_axis)
#
# #Todo put i where be is
# for i, y in enumerate(y_list):
#     y_list[i] = y[:d]
#     modifiedy_length_list.append(len(x_list[i]))
#
# # print(modifiedx_length_list)
# # print(modifiedy_length_list)
# # print(x_list[0])
# # print(y_list[0])
#
# ################################### This uses a for loop to insert the index into the y_list list to add them all together to make on giant array
# for idx, y in enumerate(y_list):
#     total = y_list[idx]+total
#
# # print(total) #This is the one giant matrix with all the corresponging values added to eachother
# average = total/len(y_list) #This is the average that will be graphed later.
# # print(average)
# ################################# This organizes the y data into an array to which the std can be added too.
# array = np.column_stack(y_list)
# #verticalarray= np.vstack(array)
# # print(array)
# #################### This is a successful std calculation. The stds are added to the corresponging values.
# std = np.std(array, axis = 1)
# # print(std)
# above_std = average + std
# below_std = average - std
#
# # #############################################
# #TODO chnage subtraction, one for each one since first x won't be the same
# plt.plot(x_axis, average, color = 'orange')#This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
# plt.plot(x_axis, above_std, color = 'orange', alpha=0.25) #Below plots the standard deviation in orange
# plt.plot(x_axis, below_std, color = 'orange', alpha=0.25)
# plt.fill_between(x_axis, average, below_std, color='orange', alpha=0.25)
# plt.fill_between(x_axis, average, above_std, color='blue', alpha=0.25)
# plt.title("Weight (kg) vs Time (ms) ")
# plt.xlabel("Time (ms)")
# plt.ylabel("Weight (kg)")
# plt.show()
#
# # #The following is to plot all the graphs on the same thing
# # for i, filename in enumerate(filenames):
# #   plt.plot(x_axis,y_list[i])
# #
# # plt.title("Weight vs Time")
# # plt.xlabel("Time")
# # plt.ylabel("Weight")
# # plt.show()
