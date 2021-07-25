'''
This program also processes the data. It does not use the functions yet. In order to plot people's different curves, just change the directory and the filename
you will get each persons' graphs. Each person will have two, one straight and one hunched. Change the words hunched and straight in
the variables in order to get two graphs.
This plots 3 curves: total curve, floor curve, seat curve.
Use this to make 2 charts for everyone.
'''
import glob
import numpy as np
import matplotlib.pyplot as plt
import os
# -------------------- user input ------------------------
project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/papi(straight)"
filename = "papi(straight)T-*.csv"
number_of_files = 9
weight_threshold = .3
# -------------------- program ------------------------
# print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames = sorted(glob.glob(os.path.join(project_dir, filename)))
filenames = filenames[0:number_of_files]
print(filenames)
x_list = list() #This is where all the x arrays of data are uploaded
y_list = list() #This is where all the y arrays of data are uploaded
z_list = list()
res_list = list() #This is used to list all the indexes for weight values above .weight threshhold.
# All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
final_0_list = list()   #This is used to list the smallest index from each array of indexes over weight_threshold. This takes the smallest values from each array
# and puts it in a list.
original_length_list = list()
modifiedx_length_list = list()
modifiedy_length_list = list()
modifiedz_length_list = list()
totaly = 0 #This is to add all the y lists into one array
totalz = 0
for filename in filenames: #This forloop opens up all the files from the experiment and puts the time in the x and the weight in
    # the y. It then adds it to the x list and the y list. In the end, you have multiple arrays with in a list
  #print(filename)
  x,y,z = np.loadtxt(filename,
                     unpack = True,
                     delimiter= ',',
                   skiprows =1 )
  x_list.append(x)
  y_list.append(y)
  z_list.append(z)

# print(x_list)
# print(y_list)
# print(z_list)
##################################################

for i, y in enumerate(y_list):
    res = np.argmax(y >= weight_threshold)
    y_list[i] = y[res:]
    x_list[i] = x_list[i][res:]
    z_list[i] = z_list[i][res:]
# print(len(x_list[0]))
# print(len(y_list[0]))
# print(len(z_list[0]))

for idx, filename in enumerate(filenames): #This prints the length of both the x and y files. This will allow us to cut away from the end so they
    # are all the same length.
    # print(len(x_list[idx]))
    # print(len(y_list[idx]))
    # print(len(z_list[idx]))
    original_length_list.append(len(x_list[idx])) #This puts the length of each x file into another list. Its the same for the y.
print(original_length_list)
d = min(original_length_list) #This defines
print(d)
  ###################################################
for i, x in enumerate(x_list): #
    x_list[i]= x[:d]
    modifiedx_length_list.append(len(x_list[i]))
    x_axis = x_list[i]-min(x_list[i])
#print(x_axis)

for i, y in enumerate(y_list):
    y_list[i] = y[:d]
    modifiedy_length_list.append(len(x_list[i]))
print(y_list)
for i, z in enumerate(z_list):
    z_list[i] = z[:d]
    modifiedz_length_list.append(len(x_list[i]))
# print(modifiedz_length_list)
# print(modifiedx_length_list)
# print(modifiedy_length_list)
# print(x_list[0])
# print(y_list[0])
#
################################### This uses a for loop to insert the index into the y_list list to add them all together to make on giant array
for idx, y in enumerate(y_list):
    totaly = y_list[idx]+totaly
for idx, z in enumerate(z_list):
    totalz = z_list[idx]+totalz

# print(total) #This is the one giant matrix with all the corresponging values added to eachother
averagey = totaly/len(y_list) #This is the average that will be graphed later.
averagez = totalz/len(z_list)
print(averagey)
################################# This organizes the y data into an array to which the std can be added too.
arrayy = np.column_stack(y_list)
arrayz = np.column_stack(z_list)
#verticalarray= np.vstack(array)
# print(array)
#################### This is a successful std calculation. The stds are added to the corresponging values.
stdy = np.std(arrayy, axis = 1)
# print(std)
above_stdy = averagey + stdy
below_stdy = averagey - stdy

stdz = np.std(arrayz, axis = 1)
# print(std)
above_stdz = averagez + stdz
below_stdz = averagez - stdz

#
# #The following is to plot all the graphs on the same thing
# # for i, filename in enumerate(filenames):
# #   plt.plot(x_axis,y_list[i])
# #
# # plt.title("Weight vs Time")
# # plt.xlabel("Time")
# # plt.ylabel("Weight")
# # plt.show()
#
plt.plot(x_axis, averagey, color = 'orange', label = 'floor_scale')#This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
plt.plot(x_axis, above_stdy, color = 'orange', alpha=0.25) #Below plots the standard deviation in orange
plt.plot(x_axis, below_stdy, color = 'orange', alpha=0.25)
plt.fill_between(x_axis, averagey, below_stdy, color='orange', alpha=0.25)
plt.fill_between(x_axis, averagey, above_stdy, color='orange', alpha=0.25)

plt.plot(x_axis, averagez, color = 'blue', label = 'toilet_scale')#This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
plt.plot(x_axis, above_stdz, color = 'blue', alpha=0.25) #Below plots the standard deviation in orange
plt.plot(x_axis, below_stdz, color = 'blue', alpha=0.25)
plt.fill_between(x_axis, averagez, below_stdz, color='blue', alpha=0.25)
plt.fill_between(x_axis, averagez, above_stdz, color='blue', alpha=0.25)

plt.plot(x_axis, (averagey+averagez), color = 'red', label = 'total_weight')

plt.title("Weight (kg) vs Time (ms) (Straight Posture Papi)")
plt.xlabel("Time (ms)")
plt.ylabel("Weight (kg)")
plt.legend(loc="best")
f = open('testfile', 'w')
f.write(str(averagey))
plt.show()
