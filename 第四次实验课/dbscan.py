import matplotlib.pyplot as plt
import random
import numpy as np
import math


def loadDataSet(filename, splitChar='\t'):
    dataSet = []
    with open(filename) as fr:
        for line in fr.readlines():
            curline = line.strip().split(splitChar)
            fltline = list(map(float, curline))
            dataSet.append(fltline)
    return dataSet


def dist(t1, t2):
    dis = math.sqrt((np.power(t1[0] - t2[0], 2) + np.power(t1[1] - t2[1], 2)))
    return dis


def dbscan(data, eps, minpts):
    num = len(data)
    unvisited = [i for i in range(num)]
    visited = []
    C = [-1 for i in range(num)]
    k = -1
    while len(unvisited) > 0:
        # 随机选一个没访问的
        p = random.choice(unvisited)
        unvisited.remove(p)
        visited.append(p)
        # N为p的eps邻域对象的集合
        N = []
        for i in range(num):
            if (dist(data[i], data[p]) <= eps):
                N.append(i)
        # 如果p的eps邻域中对象数大于阈值，则p为核心对象
        if len(N) >= minpts:
            k += 1
            C[p] = k
            for pi in N:
                if pi in unvisited:
                    unvisited.remove(pi)
                    visited.append(pi)
                    # M是位于pi邻域中的点的列表
                    M = []
                    for j in range(num):
                        if (dist(data[j], data[pi]) <= eps):
                            M.append(j)
                    if len(M) >= minpts:
                        for t in M:
                            if t not in N:
                                N.append(t)
                # 如果pi不属于任何簇，说明第pi个值没有改动
                if C[pi] == -1:
                    C[pi] =k
        # 如果p的eps邻域中的对象数小于指定与之，则p为噪声点
        else:
            C[p] = -1
    return C


if __name__ == "__main__":
    dataSet = loadDataSet('./DBSCAN.txt', splitChar=',')
    C = dbscan(dataSet, 1, 9)
    print(C)
    x = []
    y = []
    for data in dataSet:
        x.append(data[0])
        y.append(data[1])
    plt.figure(figsize=(8, 6), dpi=80)
    plt.scatter(x, y, c=C, marker='o')
    plt.show()
