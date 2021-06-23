import glob
import numpy as np
import matplotlib.pyplot as plt
import statistics

print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames = sorted(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames = filenames[0:10]

x_list = list() #This is where all the x arrays of data are uploaded
y_list = list() #This is where all the y arrays of data are uploaded
res_list = list() #This is used to list all the indexes for weight values above .1.
# All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
final_0_list = list()   #This is used to list the smallest index from each array of indexes over .1. This takes the smallest values from each array
# and puts it in a list.
original_length_list = list()
modifiedx_length_list = list()
modifiedy_length_list = list()
c = 0 #index for first lists
b = 0 #index for x lists
g = 0 #index for y lists
s = 0 #variable to compare to the y_list which has as many values as the number of files
q = 0
k = 0
Total = 0
for filename in filenames: #This forloop opens up all the files from the experiment and puts the time in the x and the weight in
    # the y. It then adds it to the x list and the y list. In the end, you have multiple arrays with in a list
  print(filename)
  x,y = np.loadtxt(filename,
                     unpack = True,
                     delimiter= ',')

  x_list.append(x)
  y_list.append(y)
  print(x_list)
###################################################
while s < len(y_list): #This removes all the indexes with y values less than .1. It then adds them into a list. it does this for
    #every y file
    res = [idx for idx, val in enumerate(y_list[s]) if val > .1]
   # print(str(res))
    res_list.append(res)
    s+=1
####################################################

print(res_list)
for res in res_list:
   f = min(res_list[q])
   final_0_list.append(f)
   q+=1
print(final_0_list)
print(min(final_0_list))
lowest_index = min(final_0_list)
###################################################

for i, x in enumerate(x_list):
     x_list[i] = x[lowest_index:]
for h, y in enumerate(y_list):
     y_list[h] = y[lowest_index:]
print("hello")
print(x_list[0])
print(y_list[0])

#####################################
for filename in filenames: #This prints the length of both the x and y files. This will allow us to cut away from the end so they
    # are all the same length.
  print(len(x_list[c]))
  print(len(y_list[c]))
  original_length_list.append(len(x_list[c])) #This puts the length of each x file into another list. Its the same for the y.
  d = min(original_length_list) #This defines
  print(d)
  c += 1
  ###################################################


for i, x in enumerate(x_list): #
    x_list[i]= x[:d]
    modifiedx_length_list.append(len(x_list[b]))
    b += 1

for i, y in enumerate(y_list):
    y_list[i] = y[:d]
    modifiedy_length_list.append(len(x_list[g]))
    g += 1


print(modifiedx_length_list)
print(modifiedy_length_list)
print(x_list[0])
print(y_list[0])

###################################################

#The following is to plot all the graphs on the same thing
# for filename in filenames:
#   plt.plot(x_list[k],y_list[k])
#   k+=1
#
# plt.title("Weight vs Time")
# plt.xlabel("Time")
# plt.ylabel("Weight")
# plt.show()
################################################### Matrix attempt below
# m = len(y_list[0])
# n = len(y_list)
# print(m)
# print(n)
# Y = np.zeros((n,m))
################################### This uses a for loop to insert the index into the y_list list to add them all together to make on giant matrix
for idx, y in enumerate(y_list):
    Total = y_list[idx]+Total

print(Total)
Average = Total/len(y_list)
print(Average)
#################################
Array = np.column_stack((y_list[0:7]))
verticalArray= np.vstack(Array)
print(Array)

STD = np.std(Array, axis = 1)
print(STD)

#################################
# STD = np.std(Total, axis = 1)
# print(STD)
###############################################
#This takes the average of all the y values and puts it into one array
# for filename in filenames:
#
#     result = [statistics.mean(k) for k in zip(y_list[0], y_list[1], y_list[2], y_list[3], y_list[4],
#                                                y_list[5], y_list[6], y_list[7])]
#
# print("yup")
# print(result)
#############################################
# x_axis = x_list[0] - (x_list[0][0]) #This shifts the data back to 0. We subtract the minimum value from the x_list[0] from the
# # x_list[0] so the first value shifts to 0.
# print(x_axis)
# plt.plot(x_axis,Average) #This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
# plt.title("Weight (kg) vs Time (ms) ")
# plt.xlabel("Time (ms)")
# plt.ylabel("Weight (kg)")
# plt.show()




###########################
#  print(y_list)
# print("This is length Y")
# print(len(y_list[0]))
# print(len(y_list[1]))
# print(x_list)
# print("This is length X")
# print(len(x_list[0]))
# print(len(x_list[1]))

# print(x_list)
# print(y_list)
# print(len(x_list))
# print(len(x_list[0]))
# print(len(x_list[1]))
# length_list.append(len(x_list[0]))
# length_list.append(len(x_list[1]))
# print(length_list)
# d = min(length_list)
# print(d)
#
# while len(x_list[0]) > len(x_list[1]):
#    x_list[0].pop[-1]
#     print(len(x_list[0]))
#   y_list.append(y)
