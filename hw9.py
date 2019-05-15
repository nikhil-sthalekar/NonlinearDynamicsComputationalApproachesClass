import numpy as np
import matplotlib.pyplot as plt
import math

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
        y.append(i[1])

    plt.plot(x, y)
    return np.transpose(np.array([x,y]))




def dcap(trajectory, eps):
    mins = np.zeros((1, trajectory.shape[1]))[0]
    maxs = np.zeros((1, trajectory.shape[1]))[0]
    # print(mins)
    # print(maxs)
    for i in range(len(maxs)):
        maxs[i] = max(trajectory[:, i])

    for i in range(len(mins)):
        mins[i] = min(trajectory[:, i])
    # print(maxs[0], maxs[1])
    # print(mins[0], mins[1])
    box_matrix = np.zeros((
                     round((maxs[0] - mins[0])/eps).astype(int),
                     round((maxs[1]-mins[1])/eps).astype(int)
                 ))
    # print(box_matrix.shape)
    for index in range(trajectory.shape[0]):
        xcurr = trajectory[index, :]
        ind = list(np.zeros((1, trajectory.shape[1]))[0])

        for i in range(trajectory.shape[1]):
            element = round((xcurr[i]-mins[i])/eps)
            # print(i, element, box_matrix.shape[i])
            if element < box_matrix.shape[i]:
              ind[i] = element
              if ind[i] == 0:
                  ind[i] = 1
        # print(int(ind[0]), int(ind[1]))
        box_matrix[int(ind[0]), int(ind[1])] = 1

    poop = np.sum(np.sum(box_matrix))

    return poop


fml = dcets(data, 8, 2)
print(fml.shape)

poop = dcap(fml, 0.5)
print(poop)
