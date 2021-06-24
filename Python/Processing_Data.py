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
# while s < len(y_list): #This removes all the indexes with y values less than .1. It then adds them into a list. it does this for
#     #every y file. In the end, you have all the indexes for each y_list[] in an array in a list
#     res = [idx for idx, val in enumerate(y_list[s]) if val > weight_threshold]
#    # print(str(res))
#     res_list.append(res)
#     s+=1
# print(res_list)
####################################################
# # # TODO c = np.argmax(a<=2) --> locate smallest value and append it to a list
# for y in y_list:
#     res = [idx for idx, val in enumerate(y) if val > weight_threshold]
#     res_list.append(res)
#     print(res)
####################################################
# print(len(y_list[2]))
# print(len(x_list[2]))
for i, y in enumerate(y_list):
    res = np.argmax(y >= weight_threshold)
    y_list[i] = y[res:]
for i, x in enumerate(x_list):
 x_list[i] = x[(len(x_list[i]) - len(y_list[i])):] #I did this wierd thing since there was a glitch that made the corresponging x and y parts different
    # print(len(y_list[i]))
    # print(len(x_list[i]))

# print(res_list)
# TODO Cut each series at its own minimum index of the weight threshold
# for res in res_list: #This uses iteration of q. This checks every single array in the larger list and finds the minimum value in each array.
#     #It then publishes that minimum value to a list and increases the counter so it goes through all the arrays. It then finds the greate of those values
#    f = min(res_list[q])
#    final_0_list.append(f)
#    q+=1
# print(final_0_list)
# print(max(final_0_list)) #I changed the following two to max since the maximum is where they are all above the certain defined value.
# highest_index = max(final_0_list) #This finds the most common index where the number is larger than .1. This is the largest one of the smallest ones
# ###################################################
# #ToDO Cut each y and x series in a for loop. Cut by their lowest index.
# for i, x in enumerate(x_list): #This deletes all the numbers before the certain lowest index to get rid of all the 0.0 values in
#    # the y and all the time values in the x.
#      x_list[i] = x[highest_index:]
# for h, y in enumerate(y_list):
#      y_list[h] = y[highest_index:]
# # print("hello")
# # print(x_list[0])
# # print(y_list[0])
#
# #####################################
# #Todo enumerate instead of a counter
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
print(x_axis)

#Todo put i where be is
for i, y in enumerate(y_list):
    y_list[i] = y[:d]
    modifiedy_length_list.append(len(x_list[i]))

# print(modifiedx_length_list)
# print(modifiedy_length_list)
# print(x_list[0])
# print(y_list[0])
#
###################################################
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

# #############################################
#TODO chnage subtraction, one for each one since first x won't be the same
plt.plot(x_axis, average, color = 'orange')#This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
plt.plot(x_axis, above_std, color = 'orange', alpha=0.25) #Below plots the standard deviation in orange
plt.plot(x_axis, below_std, color = 'orange', alpha=0.25)
plt.fill_between(x_axis, average, below_std, color='orange', alpha=0.25)
plt.fill_between(x_axis, average, above_std, color='orange', alpha=0.25)
plt.title("Weight (kg) vs Time (ms) ")
plt.xlabel("Time (ms)")
plt.ylabel("Weight (kg)")
plt.show()
# #########################################
#
# #The following is to plot all the graphs on the same thing
# # for filename in filenames:
# #   plt.plot(x_list[k],y_list[k])
# #   k+=1
# #
# # plt.title("Weight vs Time")
# # plt.xlabel("Time")
# # plt.ylabel("Weight")
# # plt.show()