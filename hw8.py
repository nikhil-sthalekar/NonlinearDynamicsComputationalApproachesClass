import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('amplitude.dat', delimiter='\t')


def dcets(time_series, tau, m):
    arr = []
    print(len(time_series))
    for i in range(len(time_series)):
        vec = []
        for j in range(m):
            ind = i + (m-j) * tau
            if ind <= len(time_series) - (tau*m) -1:
                poop = time_series[(i) + (m - j)*tau]
            else:
                continue
            vec.append(poop)
        if len(vec) == m:
            arr.append(vec)
        else:
            continue

    print(arr)
    print(len(arr))
    x = []
    y = []
    for i in arr:
        x.append(i[0])
        y.append(i[2])

    plt.plot(x, y)


dcets(data, 8, 7)

plt.show()
