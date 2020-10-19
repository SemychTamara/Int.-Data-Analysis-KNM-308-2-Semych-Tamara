import matplotlib.pyplot as plt
import KN308Semych_Parser as parser


def scatter_plot(x, y, x_label="", y_label="", title="", color = "blue", yscale_log=False):
    _, ax = plt.subplots()
    ax.scatter(x, y, s = 10, color = color, alpha = 0.75)
    if yscale_log == True:
        ax.set_yscale('log')

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


def line_plot(x, y, x_label="", y_label="", title=""):
    _, ax = plt.subplots()
    ax.plot(x, y, lw = 2, color = '#539caf', alpha = 1)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


def histogram(data, x_label ='', title = ""):
    _, ax = plt.subplots()
    ax.hist(data, color = 'green')
    ax.set_ylabel("Frequency")
    ax.set_xlabel(x_label)
    ax.set_title(title)
    plt.show()


def pie_plot(data, title=""):
    _, ax = plt.subplots()
    arr = data.value_counts()
    ax.pie(arr, labels=arr.index)
    ax.set_title(title)
    plt.show()


def g_type_func(g_type):
    if g_type == 1:
        x = input("First Data(full name): ")
        y = input("Second Data(full name): ")
        scatter_plot(parser.data_type(x), parser.data_type(y), x, y, str("Plot: " + x + y))

    elif g_type == 2:
        x = input("First Data(full name): ")
        y = input("Second Data(full name): ")
        line_plot(parser.data_type(x), parser.data_type(y), x, y, str("Plot: " + x + y))

    elif g_type == 3:
        x = input("First Data(full name): ")
        histogram(parser.data_type(x), x, str("Plot: " + x ))
    elif g_type == 4:
        x = input("First Data(full name): ")
        pie_plot(parser.data_type(x), str("Plot: " + x ))


while True:
    print('\nWhat type of graph do you want?' + " Enter only number:")
    g_type = int(input( "1 - Scatter Plot\n" +
                        "2 - Line Plot\n" +
                        "3 - Histogram\n" +
                        "4 - Pie Plot\n" +
                        "5 - EXIT\n"))
    if g_type >= 5:
        break
    else:
        g_type_func(g_type)