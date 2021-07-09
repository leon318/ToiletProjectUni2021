import matplotlib.pyplot as plt


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

def matplotlib_plotter_with_z_no_std(x_axis, averagey, averagez, color= 'orange', filler = ' '):
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
    total_weight = averagez +  averagey
    plt.plot(x_axis, averagey/total_weight[-1], color = color, label = ','.join(['floor_weight', filler]), linestyle = ':')
    # plt.plot(x_axis, above_stdy, color=color, alpha=alpha)
    # plt.plot(x_axis, below_stdy, color=color, alpha=alpha)
    # plt.fill_between(x_axis, averagey, below_stdy, color=color, alpha=alpha)
    # plt.fill_between(x_axis, averagey, above_stdy, color=color, alpha=alpha)


    plt.plot(x_axis, averagez/total_weight[-1], color = color, label = ','.join(['toilet_weight', filler]), linestyle = "--")
     # This plots the x values and the y values. Since all the x values are the same after the processing, it doesn't matter which one we use.
    # plt.plot(x_axis, above_stdz, color=color, alpha=0.25)  # Below plots the standard deviation in orange
    # plt.plot(x_axis, below_stdz, color=color, alpha=0.25)
    # plt.fill_between(x_axis, averagez, below_stdz, color=color, alpha=0.25)
    # plt.fill_between(x_axis, averagez, above_stdz, color=color, alpha=0.25)

    plt.plot(x_axis, (averagey + averagez)/total_weight[-1], color = color, label = ','.join(['total weight', filler]), linestyle = '-')