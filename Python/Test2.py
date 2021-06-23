import matplotlib.pyplot as plt
def graphWriter():

    for file in os.listdir(os.getcwd()):
        List1 = []
        List2 = []
        List3 = []
        List4 = []

        with open(filename, 'r') as file:
            for col in csv.DictReader(file):
                List1.append(col['x1'])
                List2.append(col['y1'])
                List3.append(col['x2'])
                List4.append(col['y2'])

        plt.subplot(2, 1, 1)
        plt.grid(True)
        colors = np.random.rand(2)
        plt.plot(List1,List2,c=colors)
        plt.tick_params(axis='both', which='major', labelsize=8)

        plt.subplot(2, 1, 2)
        plt.grid(True)
        colors = np.random.rand(2)
        plt.plot(List1,List3,c=colors)
        plt.tick_params(axis='both', which='major', labelsize=8)

    plt.show()
    plt.gcf().clear()
    plt.close('all')