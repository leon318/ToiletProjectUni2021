import glob
import numpy as np
import matplotlib.pyplot as plt


print(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames = sorted(glob.glob('/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-*.csv'))
filenames = filenames[0:10]

x_list = list()
y_list = list()
res_list = list() #This is used to list all the indexes for weight values above .5
final_0_list = list()   #This is used to list the smallest index from each test over .5
original_length_list = list()
modifiedx_length_list = list()
modifiedy_length_list = list()
c = 0 #index for first lists
b = 0 #index for x lists
g = 0 #index for y lists
s = 0
q = 0
v = 0
k = 0

for filename in filenames:
  print(filename)
  x,y = np.loadtxt(filename,
                     unpack = True,
                     delimiter= ',')

  x_list.append(x)
  y_list.append(y)
  print(x_list)
while s < len(y_list):
    res = [idx for idx, val in enumerate(y_list[s]) if val > .5]
   # print(str(res))
    res_list.append(res)
    s+=1
#
print(res_list)
for res in res_list:
   f = min(res_list[q])
   final_0_list.append(f)
   q+=1
print(final_0_list)
print(min(final_0_list))
lowest_index = min(final_0_list)

for i, x in enumerate(x_list):
     x_list[i] = x[lowest_index:]
for h, y in enumerate(y_list):
     y_list[h] = y[lowest_index:]
print("hello")
print(x_list[0])
print(y_list[0])

#####################################
for filename in filenames:
  print(len(x_list[c]))

  print(len(y_list[c]))
  original_length_list.append(len(x_list[c]))
  d = min(original_length_list)
  print(d)
  c += 1
for i, x in enumerate(x_list):
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


for filename in filenames:
  plt.plot(x_list[k],y_list[k])
  k+=1

plt.title("Weight vs Time")
plt.xlabel("Time")
plt.ylabel("Weight")
plt.show()










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
