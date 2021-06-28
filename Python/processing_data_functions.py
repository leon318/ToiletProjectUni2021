import glob
import numpy as np
import matplotlib.pyplot as plt
import os

# from Python.preprocessing.Plotter import matplotlib_plotter
# from Python.preprocessing.unpacking_data import unpack_and_append_data


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

def unpack_and_append_data(filenames, x_list, y_list, skiprow = 1):
    """
    Free text description:
    This function imports the csv files in a for loop and separates them into arrays which it then puts into a list. The list consists out of as many
    arrays as there are files.
    Args:
        filenames: This represents the 10 csv files that the program imports. every time the for loop loops
        it imports one of the files
        x_list (list): the x list is a list of all the arrays with the time values. If there are 10 files there will be 10 arrays each with all the time values for each
        test
         y_list (list: the same as the x list but for the weight values
         skiprow (variable): this tells the program to skip the first row which has the title of each column

    Return: This returns the x_list and the y_list so it can be processed in the next functions.

    """
    for filename in filenames:
        x, y = np.loadtxt(filename,
                          unpack=True,
                          delimiter=',',
                          skiprows=skiprow)

        x_list.append(x)
        y_list.append(y)
    return x_list, y_list

def threshold_locater_and_posterior_trimmer(x_list, y_list,weight_threshold,):
    """
    Free text descrpition:
    This function locates where the weight value starts to be greater than one and then indexes it from there, making that the
    first value. It thertefore cuts out all the zeros at the beginning of each test.
    Args:
        x_list (list): this list needs to be imported so the same amount of points can be cut out in its arrays as in their corresponding y arrays
        y_list (list): This list needs to be imported so all the 0.0 can be cut out.
        weight_threshold (variable): This is used as the cutofff point. The np.argmax uses this value to cut out all the indexes before
        it.

    Return: This returns the modified x_list and the y_list without the zeros and the corresponding x values.

    """
    for i, y in enumerate(y_list):
        res = np.argmax(y >= weight_threshold)
        y_list[i] = y[res:]
        x_list[i] = x_list[i][res:]
    return x_list, y_list

def find_shortest_length(filenames, original_length_list, x_list):
    """
    Free text description:
    This analyzez the x array and sees which one is the shortest. It then knows how much to cut from each of the other arrays to make
    them all equal.
    Args:
        filenames (variable): This represents the 10 csv files that the program imports. every time the for loop loops
        it imports one of the files
        x_list (list): this is the modified x list with the modified arrays. The arrays are different lengths so they need to be analyzed.

        original_length_list (list): this records all the lengths of each of the x value arrays. The function then finds the smallest one and stroes that
        index in d.
    Return:
        d (variable): this  stores the shortest length of the one of the x arrays. It is returned so the next function can shorten all the x and y arrays to this length

    """
    for idx, filename in enumerate(filenames): #This prints the length of both the x and y files. This will allow us to cut away from the end so they
        original_length_list.append(len(x_list[idx])) #This puts the length of each x file into another list. Its the same for the y.
    d = min(original_length_list) #This defines
    # print(d)
    return d

def anterior_trimmer_x(d, x_list, modifiedx_length_list):
    """
       Free text description:
       This trims the end values of the x arrays to make them all the same length.
    Arg:
        d (variable): this is imported from the previous function. This represents the smallest length of one of the arrays.
        Its used to index all the other arrays.

        x_list (list): This is imported so it can be indexed by the d value.
        modifiedx_length_list (list): This is the returned x_list with all arrays the same length
        x_axis (variable): this will be the x axis for the coressponding weight values. This is determined by subtracting the smallest value of each x array for that array
        to 0 them all out. All the arrays will have the same x axis value.
     Return:
        x_axis (list): this is the returned x_axis that will be graphed
        x_list (list): This contains all the equal length x arrays
        modifiedx_length_list (list): This just has all the length of each array in the x_list. When it is
        printed, it will prove all of them are the same length.
    """
    for i, x in enumerate(x_list): #
        x_list[i]= x[:d]
        modifiedx_length_list.append(len(x_list[i]))
        x_axis = x_list[i]-min(x_list[i])
    return x_axis, x_list, modifiedx_length_list

def anterior_trimmer_y(d, x_list, y_list, modifiedy_length_list):
    """
           Free text description:
           This trims the end values of the y arrays to make them all the same length.
        Arg:
            d (variable): this is imported from the previous function. This represents the smallest length of one of the arrays.
            Its used to index all the other arrays.

            y_list (list): This is imported so it can be indexed by the d value.
            modifiedx_length_list (list): This is the returned y_list with all arrays the same length

         Return:
            y_list (list): This contains all the equal length y arrays
            modifiedy_length_list (list): This just has all the length of each array in the y_list. When it is
            printed, it will prove all of them are the same length.
        """
    for i, y in enumerate(y_list):
        y_list[i] = y[:d]
        modifiedy_length_list.append(len(x_list[i]))
    return y_list, modifiedy_length_list

def total_and_averager(y_list,total):
    """
              Free text description:
              This adds all the weight values to their corresponding weight values in the other arrays to make one array with
              all the values added up. This array is divided by the length of the y_list in order to find the avergae weight values.
           Arg:
           y_list (list): this is imported for the for loop and so that all the arrays in this list can be totaled. It is also imported so its
           length can be used to divide the total to find the average
           total (variable): this represents all the y values added together
           average (variable): this represents the average matrix that will be graphed
           return:
            average (variable): This is returned so it can be graphed
            total: This is only returned for testing
    """
    for idx, y in enumerate(y_list):
        total = y_list[idx]+total
    average = total/len(y_list)
    return total, average
def std_calculator(average, y_list):
    """
        Free text description: This calculates the standard deviation of the each avearage p[oint in the array. It then adds this standard deviation
        to the average array and also subtracts from the average array.
        Arg:
            y_list (list):  This is reformatted to a column so STD can be taken
            Array (variable): This is used to organize the y_list and so the STD can be taked
            STD (variable): This stores the STD
            above_std: This will be a line that can be graphed above the avergae
            below_std: This will be a line graphed below the average
        return
            above_std: returned so it can be graphed
            below_std: returned so it can be graphe
            std: returned just to test
    """
    array = np.column_stack(y_list)
    std = np.std(array, axis = 1)
    above_std = average + std
    below_std = average - std
    return std, above_std, below_std
def matplotlib_plotter(x_axis, above_std, below_std, average, color='orange', alpha=.25, label='fill in'):
    """
    Free text description:
    This graphs the average graphs and the STD graphs.

    Args:
        x_axis: This provides the numbers on the x axis
        above_std: This will be the 1 std above the average line
        below_std: this will be the 1 std below the average line
        average: this will be the average line
        color: this will be the color of the line
        alpha: this will be the transparency of the shading between the lines
        label: this will be the key.
    """
    plt.plot(x_axis, average,
             color=color,
             label=label)
    plt.plot(x_axis, above_std, color=color, alpha=alpha)
    plt.plot(x_axis, below_std, color=color, alpha=alpha)
    plt.fill_between(x_axis, average, below_std, color=color, alpha=alpha)
    plt.fill_between(x_axis, average, above_std, color=color, alpha=alpha)


x_list, y_list = unpack_and_append_data(filenames, x_list, y_list)
x_list, y_list = threshold_locater_and_posterior_trimmer(x_list, y_list, weight_threshold)
d = find_shortest_length(filenames, original_length_list, x_list)
x_axis, x_list, modifiedx_length_list = anterior_trimmer_x(d, x_list, modifiedx_length_list)
y_list, modifiedy_length_list = anterior_trimmer_y(d, x_list, y_list, modifiedy_length_list)
total, average = total_and_averager(y_list,total)
std, above_std, below_std = std_calculator(average, y_list)
matplotlib_plotter(x_axis, above_std, below_std, average, label = "floorADS1232")

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
matplotlib_plotter(x_axis2, above_std, below_std, average, color = 'blue', alpha =.25, label="toilethx711")
#
x_list3, y_list3 = unpack_and_append_data(filenames3, x_list3, y_list3, skiprow = 1)
x_list3, y_list3 = threshold_locater_and_posterior_trimmer(x_list3, y_list3, weight_threshold)
d3 = find_shortest_length(filenames3, original_length_list3, x_list3)
print(d3)
x_axis3, x_list3, modifiedx_length_list3 = anterior_trimmer_x(d3, x_list3,modifiedx_length_list3)
print(modifiedx_length_list3)
y_list3, modifiedy_length_list3 = anterior_trimmer_y(d3, x_list3, y_list3, modifiedy_length_list3)
print(modifiedy_length_list3)
total3, average = total_and_averager(y_list3, total3)
std, above_std, below_std = std_calculator(average, y_list3)
matplotlib_plotter(x_axis3, above_std, below_std, average, color = 'green', alpha =.25, label="floorhx711")

x_list4, y_list4 = unpack_and_append_data(filenames4, x_list4, y_list4, skiprow = 1)
x_list4, y_list4 = threshold_locater_and_posterior_trimmer(x_list4, y_list4, weight_threshold)
d4 = find_shortest_length(filenames4, original_length_list4, x_list4)
print(d4)
x_axis4, x_list4, modifiedx_length_list4 = anterior_trimmer_x(d4, x_list4,modifiedx_length_list4)
print(modifiedx_length_list4)
y_list4, modifiedy_length_list4 = anterior_trimmer_y(d4, x_list4, y_list4, modifiedy_length_list4)
print(modifiedy_length_list4)
total4, average = total_and_averager(y_list4, total4)
std, above_std, below_std = std_calculator(average, y_list4)
matplotlib_plotter(x_axis4, above_std, below_std, average, color = 'black', alpha =.25, label="toilethx711")

plt.legend(loc="best")
plt.show()


