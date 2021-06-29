import numpy as np
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

def anterior_trimmer_x_and_y(d, x_list, y_list, modifiedx_length_list, modifiedy_length_list):
    """
       Free text description:
       This trims the end values of the x arrays to make them all the same length.
    Arg:
        d (variable): this is imported from the previous function. This represents the smallest length of one of the arrays.
        Its used to index all the other arrays.
        x_list (list): This is imported so it can be indexed by the d value.
        modifiedx_length_list (list): This is the returned x_list with all arrays the same length
        y_list (list): This is imported so it can be indexed by the d value.
            modifiedx_length_list (list): This is the returned y_list with all arrays the same length
     Return:
        x_axis (list): this is the returned x_axis that will be graphed
        x_list (list): This contains all the equal length x arrays
        modifiedx_length_list (list): This just has all the length of each array in the x_list. When it is
        printed, it will prove all of them are the same length.
        y_list (list): This contains all the equal length y arrays
        modifiedy_length_list (list): This just has all the length of each array in the y_list. When it is
            printed, it will prove all of them are the same length.
    """
    for i, x in enumerate(x_list): #
        x_list[i]= x[:d]
        modifiedx_length_list.append(len(x_list[i]))
        x_axis = x_list[i]-min(x_list[i])
    for i, y in enumerate(y_list):
        y_list[i] = y[:d]
        modifiedy_length_list.append(len(x_list[i]))
    return x_axis, x_list,y_list, modifiedy_length_list, modifiedx_length_list



import numpy as np
def threshold_locater_and_posterior_trimmer3(x_list, y_list,z_list, weight_threshold,):
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
        z_list[i] = z_list[i][res:]
    return x_list, y_list, z_list

def anterior_trimmer_x_and_y_and_z(d, x_list, y_list, z_list, modifiedx_length_list, modifiedy_length_list, modifiedz_length_list):
    """
       Free text description:
       This trims the end values of the x arrays to make them all the same length.
    Arg:
        d (variable): this is imported from the previous function. This represents the smallest length of one of the arrays.
        Its used to index all the other arrays.
        x_list (list): This is imported so it can be indexed by the d value.
        modifiedx_length_list (list): This is the returned x_list with all arrays the same length
        y_list (list): This is imported so it can be indexed by the d value.
            modifiedx_length_list (list): This is the returned y_list with all arrays the same length
     Return:
        x_axis (list): this is the returned x_axis that will be graphed
        x_list (list): This contains all the equal length x arrays
        modifiedx_length_list (list): This just has all the length of each array in the x_list. When it is
        printed, it will prove all of them are the same length.
        y_list (list): This contains all the equal length y arrays
        modifiedy_length_list (list): This just has all the length of each array in the y_list. When it is
            printed, it will prove all of them are the same length.
    """
    for i, x in enumerate(x_list): #
        x_list[i]= x[:d]
        modifiedx_length_list.append(len(x_list[i]))
        x_axis = x_list[i]-min(x_list[i])
    for i, y in enumerate(y_list):
        y_list[i] = y[:d]
        modifiedy_length_list.append(len(x_list[i]))
    for i, z in enumerate(z_list):
        z_list[i] = z[:d]
        modifiedz_length_list.append(len(x_list[i]))
    return x_axis, x_list,y_list, z_list, modifiedy_length_list, modifiedx_length_list, modifiedz_length_list
