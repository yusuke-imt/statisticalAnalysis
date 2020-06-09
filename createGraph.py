import matplotlib.pyplot as plt

def Graph(dfs, title, xlabel, ylabel):
    dfs.plot(title=title, grid=True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()