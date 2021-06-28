import numpy as np

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
        Return:
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
        Return:
            above_std: returned so it can be graphed
            below_std: returned so it can be graphed
            std: returned just to test
    """
    array = np.column_stack(y_list)
    std = np.std(array, axis = 1)
    above_std = average + std
    below_std = average - std
    return std, above_std, below_std