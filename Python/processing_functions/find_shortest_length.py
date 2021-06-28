def find_shortest_length(filenames, original_length_list, x_list):
    """
    Free text description:
    This analyzes the x array and sees which one is the shortest. It then knows how much to cut from each of the other arrays to make
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