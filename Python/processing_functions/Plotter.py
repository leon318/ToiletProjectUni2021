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
