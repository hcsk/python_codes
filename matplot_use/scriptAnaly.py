# coding = utf-8

import string
import matplotlib.pyplot as plt
import numpy as np


def bar_chart():
    l = [1, 2, 3, 4, 5]
    h = [20, 14, 38, 27, 9]
    w = [0.1, 0.2, 0.3, 0.4, 0.5]
    b = [1, 2, 3, 4, 5]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects = ax.bar(l, h, w, b)
    plt.show()

def quxian():
    x = np.arange(-3, 3.5, 0.5)
    y = [ele ** 2 for ele in x]
    z = [ele * 2 for ele in x]

    fig = plt.figure(1)

    ax = fig.add_subplot(211)
    line1 = ax.plot(x, y, 'ro-')

    ax = fig.add_subplot(212)
    line2 = ax.plot(x, z, 'g-')

    plt.show()


if __name__ == '__main__':
    quxian()

