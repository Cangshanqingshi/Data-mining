import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def kmeans(data, n, m, k, plt):
    # 获取k个随机数
    rarrary = np.random.random(size=k)
    # 乘以数据集大小
    rarrary = np.floor(rarrary * n)
    # 转化为Int
    rarrary = rarrary.astype(int)
    # 随机取数据集中k个点作为初始点
    center = data[rarrary]
    # 1行80列的0数组，标记每个样本所属的类（k[i]）
    cls = np.zeros([n], np.int)
    print('初始中心为：\n', center)
    run = True
    time = 0
    while run:
        time += 1
        for i in range(n):
            # 求差
            tmp = data[i] - center
            # 求平方
            tmp = np.square(tmp)
            # axis = 1表示按行求和
            tmp = np.sum(tmp, axis=1)
            # 取最小（最近）的给该店染色
            cls[i] = np.argmin(tmp)
        # 如果没有修改中心带你则结束循环
        run = False
        # 计算更新的中心点
        for i in range(k):
            # 找到属于该类的所有样本
            club = data[cls == i]
            # axis=0表示按列求均值，计算出新的中心点
            newcenter = np.mean(club, axis=0)
            # 如果差距小，则视为没变，否则更新之，重置run，再次循环
            ss = np.abs(center[i] - newcenter)
            if np.sum(ss, axis=0) > 1e-4:
                center[i] = newcenter
                run = True
        print('新的中心为：\n', center)
    print('程序结束，迭代次数', time)
    # 按类打印图表
    for i in range(k):
        club = data[cls == i]
        showtable(club, plt)
    # 打印最后的中心点
    showtable(center, plt)


def showtable(data, plt):
    x = data.T[0]
    y = data.T[1]
    plt.scatter(x, y)


if __name__ == "__main__":
    csv = pd.read_csv("./kmeans.txt")
    # 打印原始数据
    kmeans(csv.values, 80, 2, 4, plt)
    plt.show()
