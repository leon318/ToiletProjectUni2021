import numpy as np
def unpack_and_append_data3(filenames, x_listy, x_listz, y_list, z_list, skiprow = 1):
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
        x, y, z = np.loadtxt(filename,
                          unpack=True,
                          delimiter=',',
                          skiprows=skiprow)

        x_listy.append(x)
        y_list.append(y)
        for filename in filenames:
            x, y, z = np.loadtxt(filename,
                                 unpack=True,
                                 delimiter=',',
                                 skiprows=skiprow)
        x_listz.append(x)
        z_list.append(z)

    return x_listy, x_listz, y_list, z_list