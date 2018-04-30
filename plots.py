import matplotlib.pyplot as plt
import numpy
import pandas as pd
from pandas.tools.plotting import parallel_coordinates

data = pd.read_csv('table.csv')
print data.describe()

def test():
    t = data[['Clinton','Donald','Fake','Hillary','Obama','Russian','Trump','hillary','news']]
    h = t.sum()
    # print h
    h.plot.hist(bins=10)
    h.plot(kind='hist')
    h.plot(kind='bar')
    t.plot(kind='box')
    t.plot(style="*")
    t.plot(kind='density')

    plt.xlabel("features")
    plt.ylabel("frequency")
    plt.show()

def paraCord():
    names = ['Clinton', 'Donald', 'Fake', 'Hillary', 'Obama', 'Russian', 'Trump', 'hillary', 'news']
    correlations = data.corr()
    # plot correlation matrix
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations, vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = numpy.arange(0, 9, 1)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(names)
    ax.set_yticklabels(names)
    plt.show()

if __name__ == '__main__':
    test()
    paraCord()

