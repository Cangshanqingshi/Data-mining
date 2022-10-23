import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class KNearNeighbor(object):
    def __init__(self):
        pass

    # 定义一个内部类loadData，用于获取并初始化数据
    def loadData(self, path):
        data = pd.read_csv(path, header=None)

        # 特征及类别名称
        data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'species']
        x = data.iloc[0:150, 0:4].values
        y = data.iloc[0:150, 4].values

        num_of_train = 40

        # Iris-setosa 输出label用0表示
        y[y == 'Iris-setosa'] = 0
        # Iris-versicolor 输出label用1来表示
        y[y == 'Iris-versicolor'] = 1
        # Iris-virginica 输出label用1来表示
        y[y == 'Iris-virginica'] = 2
        # Iris-setosa 4个特征
        self.x_setosa, self.y_setosa = x[0:50], y[0:50]
        # Iris-versicolor 4个特征
        self.x_versicolor, self.y_versicolor = x[50:100], y[50:100]
        # Iris-virginica 4个特征
        self.x_virginica, self.y_virginica = x[100:150], y[100:150]

        # training set
        self.x_setosa_train = self.x_setosa[: num_of_train, :]
        self.y_setosa_train = self.y_setosa[: num_of_train]
        self.x_versicolor_train = self.x_versicolor[: num_of_train, :]
        self.y_versicolor_train = self.y_versicolor[: num_of_train]
        self.x_virginica_train = self.x_virginica[: num_of_train, :]
        self.y_virginica_train = self.y_virginica[: num_of_train]
        self.x_train = np.vstack([self.x_setosa_train, self.x_versicolor_train, self.x_virginica_train])
        self.y_train = np.hstack([self.y_setosa_train, self.y_versicolor_train, self.y_virginica_train])

        # test set
        self.x_setosa_test = self.x_setosa[num_of_train: 50, :]
        self.y_setosa_test = self.y_setosa[num_of_train: 50]
        self.x_versicolor_test = self.x_versicolor[num_of_train: 50, :]
        self.y_versicolor_test = self.y_versicolor[num_of_train: 50]
        self.x_virginica_test = self.x_virginica[num_of_train: 50, :]
        self.y_virginica_test = self.y_virginica[num_of_train: 50]
        self.x_test =np.vstack([self.x_setosa_test, self.x_versicolor_test, self.x_virginica_test])
        self.y_test = np.hstack([self.y_setosa_test, self.y_versicolor_test, self.y_virginica_test])

    # 利用matplotlib展示数据
    def showData(self):
        # 只选择sepal length和petal length两个特征，在二维平面上作图
        # 训练集
        plt.scatter(self.x_setosa_train[:, 0], self.x_setosa_train[:, 2], color='red', marker='o', label='setosa_train')
        plt.scatter(self.x_versicolor_train[:, 0], self.x_versicolor_train[:, 2], color='blue', marker='^', label='versicolor_train')
        plt.scatter(self.x_virginica_train[:, 0], self.x_virginica_train[:, 2], color='green', marker='s', label='virginica_train')
        # 测试集
        plt.scatter(self.x_setosa_test[:, 0], self.x_setosa_test[:, 2], color='y', marker='o', label='setosa_test')
        plt.scatter(self.x_versicolor_test[:, 0], self.x_versicolor_test[:, 2], color='y', marker='^', label='versicolor_test')
        plt.scatter(self.x_virginica_test[:, 0], self.x_virginica_test[:, 2], color='y', marker='s', label='virginica_test')

        plt.xlabel('sepal length')
        plt.ylabel('petal length')
        plt.legend(loc = 4)
        plt.show()

    # 预测函数
    def predict(self, x, k=1):
        # 计算欧氏距离
        num_test = x.shape[0]
        # 方差公式
        d1 = -2 * np.dot(x, self.x_train.T)
        # shape(num_test, 1)
        d2 = np.sum(np.square(x), axis=1, keepdims=True)
        d3 = np.sum(np.square(self.x_train), axis=1)
        dist = np.sqrt(d1 + d2 + d3)
        # print(dist)
        # 根据K值，选择最可能属于的类别
        y_pred = np.zeros(num_test)
        for i in range(num_test):
            dist_k_min = np.argsort(dist[i])[:k]    # 最近邻K个实例位置
            y_kclose = self.y_train[dist_k_min]     # 最近邻K个实例对应标签
            # 找出K个标签中从属类别最多的作为预测类别
            y_pred[i] = np.argmax(np.bincount(y_kclose.tolist()))
        return y_pred


if __name__ == "__main__":
    path = "./iris.data"
    knn = KNearNeighbor()
    knn.loadData(path)
    knn.showData()
    print('训练集：')
    print(knn.x_train)
    print('测试集：')
    print(knn.x_test)
    for k in range(1, 11):
        y_pred = knn.predict(x=knn.x_test, k=k)
        accuracy = np.mean(y_pred == knn.y_test)
        print(f'k={k}，时，测试机预测准确率：{accuracy}')
