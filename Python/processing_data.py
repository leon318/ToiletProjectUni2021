"""
Processes all the data by cutting out zeros and making an average graph
This was the first program that graphed. It has been adapted. This one has no functions and therefore would need to be copied
and pasted to plot multiple graphs.
"""
import glob
import numpy as np
import matplotlib.pyplot as plt
import os
# -------------------- user input ------------------------
project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/toilet(groundADS)"
filename = "toilet(groundADS)T-*.csv"
number_of_files = 10
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
for filename in filenames: #This forloop opens up all the files from the experiment and puts the time in the x and the weight in
    # the y. It then adds it to the x list and the y list. In the end, you have multiple arrays with in a list
  #print(filename)
  x,y = np.loadtxt(filename,
                     unpack = True,
                     delimiter= ',',
                   skiprows =1 )

  x_list.append(x)
  y_list.append(y)
 # print(x_list)
###################################################

for i, y in enumerate(y_list):
    res = np.argmax(y >= weight_threshold)
    y_list[i] = y[res:]
    x_list[i] = x_list[i][res:]

for idx, filename in enumerate(filenames): #This prints the length of both the x and y files. This will allow us to cut away from the end so they
    # are all the same length.
    # print(len(x_list[idx]))
    # print(len(y_list[idx]))
    original_length_list.append(len(x_list[idx])) #This puts the length of each x file into another list. Its the same for the y.
d = min(original_length_list) #This defines
# print(d)
#   ###################################################
for i, x in enumerate(x_list): #
    x_list[i]= x[:d]
    modifiedx_length_list.append(len(x_list[i]))
    x_axis = x_list[i]-min(x_list[i])
#print(x_axis)

for i, y in enumerate(y_list):
    y_list[i] = y[:d]
    modifiedy_length_list.append(len(x_list[i]))

# print(modifiedx_length_list)
# print(modifiedy_length_list)
# print(x_list[0])
# print(y_list[0])

################################### This uses a for loop to insert the index into the y_list list to add them all together to make on giant array
for idx, y in enumerate(y_list):
    total = y_list[idx]+total

# print(total) #This is the one giant matrix with all the corresponging values added to eachother
average = total/len(y_list) #This is the average that will be graphed later.
# print(average)
################################# This organizes the y data into an array to which the std can be added too.
array = np.column_stack(y_list)
#verticalarray= np.vstack(array)
# print(array)
#################### This is a successful std calculation. The stds are added to the corresponging values.
std = np.std(array, axis = 1)
# print(std)
above_std = average + std
below_std = average - std

############################################# With just one
# plt.plot(x_axis, average, color = 'orange')#This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
# plt.plot(x_axis, above_std, color = 'orange', alpha=0.25) #Below plots the standard deviation in orange
# plt.plot(x_axis, below_std, color = 'orange', alpha=0.25)
# plt.fill_between(x_axis, average, below_std, color='orange', alpha=0.25)
# plt.fill_between(x_axis, average, above_std, color='blue', alpha=0.25)
# plt.title("Weight (kg) vs Time (ms) ")
# plt.xlabel("Time (ms)")
# plt.ylabel("Weight (kg)")
# plt.show()

#The following is to plot all the graphs on the same thing
# for i, filename in enumerate(filenames):
#   plt.plot(x_axis,y_list[i])
#
# plt.title("Weight vs Time")
# plt.xlabel("Time")
# plt.ylabel("Weight")
# plt.show()

# # -------------------- user input ------------------------
# project_dir2 = "/Users/Leon/Documents/ToiletProjectUni2021/exp2(toilethx711)"
# filename2 = "exp2(toilethx711)T-*.csv"
# number_of_files2 = 10
# weight_threshold = .05
# # -------------------- program ------------------------
# # print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
# filenames2 = sorted(glob.glob(os.path.join(project_dir2, filename2)))
# filenames2 = filenames2[0:number_of_files2]
#
# x_list2 = list() #This is where all the x arrays of data are uploaded
# y_list2 = list() #This is where all the y arrays of data are uploaded
# res_list2 = list() #This is used to list all the indexes for weight values above .weight threshhold.
# # All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
# final_0_list2 = list()   #This is used to list the smallest index from each array of indexes over weight_threshold. This takes the smallest values from each array
# # and puts it in a list.
# original_length_list2 = list()
# modifiedx_length_list2 = list()
# modifiedy_length_list2 = list()
# total2 = 0 #This is to add all the y lists into one array
# for filename2 in filenames2: #This forloop opens up all the files from the experiment and puts the time in the x and the weight in
#     # the y. It then adds it to the x list and the y list. In the end, you have multiple arrays with in a list
#   #print(filename)
#   x,y = np.loadtxt(filename2,
#                      unpack = True,
#                      delimiter= ',',
#                    skiprows= 1)
#
#   x_list2.append(x)
#   y_list2.append(y)
#  # print(x_list)
# ###################################################
#
# for i, y in enumerate(y_list2):
#     res = np.argmax(y >= weight_threshold)
#     y_list2[i] = y[res:]
#     x_list2[i] = x_list2[i][res:]
#
# for idx, filename2 in enumerate(filenames2): #This prints the length of both the x and y files. This will allow us to cut away from the end so they
#     # are all the same length.
#     # print(len(x_list[idx]))
#     # print(len(y_list[idx]))
#     original_length_list2.append(len(x_list2[idx])) #This puts the length of each x file into another list. Its the same for the y.
# d2 = min(original_length_list2) #This defines
# # print(d)
# #   ###################################################
# for i, x in enumerate(x_list2): #
#     x_list2[i]= x[:d2]
#     modifiedx_length_list2.append(len(x_list2[i]))
#     x_axis2 = x_list2[i]-min(x_list2[i])
#     print(x_axis2)
#
# for i, y in enumerate(y_list2):
#     y_list2[i] = y[:d2]
#     modifiedy_length_list2.append(len(x_list2[i]))
#
# # print(modifiedx_length_list)
# # print(modifiedy_length_list)
# # print(x_list[0])
# # print(y_list[0])
#
# ################################### This uses a for loop to insert the index into the y_list list to add them all together to make on giant array
# for idx, y in enumerate(y_list2):
#     total2 = y_list2[idx]+total2
#
# # print(total) #This is the one giant matrix with all the corresponging values added to eachother
# average2 = total2/len(y_list2) #This is the average that will be graphed later.
# # print(average)
# ################################# This organizes the y data into an array to which the std can be added too.
# array2 = np.column_stack(y_list2)
# #verticalarray= np.vstack(array)
# # print(array)
# #################### This is a successful std calculation. The stds are added to the corresponging values.
# std2 = np.std(array2, axis = 1)
# # print(std)
# above_std2 = average2 + std2
# below_std2 = average2 - std2

# #############################################
plt.plot(x_axis, average, color = 'orange')#This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
plt.plot(x_axis, above_std, color = 'orange', alpha=0.25) #Below plots the standard deviation in orange
plt.plot(x_axis, below_std, color = 'orange', alpha=0.25)
plt.fill_between(x_axis, average, below_std, color='orange', alpha=0.25)
plt.fill_between(x_axis, average, above_std, color='orange', alpha=0.25)

# plt.plot(x_axis2, average2, color = 'blue')#This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
# plt.plot(x_axis2, above_std2, color = 'blue', alpha=0.25) #Below plots the standard deviation in orange
# plt.plot(x_axis2, below_std2, color = 'blue', alpha=0.25)
# plt.fill_between(x_axis2, average2, below_std2, color='blue', alpha=0.25)
# plt.fill_between(x_axis2, average2, above_std2, color='blue', alpha=0.25)
# plt.title("Weight (kg) vs Time (ms) ")
# plt.xlabel("Time (ms)")
# plt.ylabel("Weight (kg)")
plt.show()