import numpy as np
import matplotlib.pyplot as plt

# 感知机

# load data from txt
data_set = []
data_label = []
file = open('ann_Perceptron.txt')
for line in file:
    line = line.split(' ')
    for i in range(len(line)):
        line[i] = float(line[i])
    data_set.append(line[0:2])
    data_label.append(int(line[-1]))
file.close()
data = np.array(data_set)
label = np.array(data_label)

# 初始化w, b, alpha
w = np.array([0, 0])
b = 0
alpha = 2.0

# 计算 y*(w*x+b)
f = (np.dot(data, w.T) + b) * label
idx = np.where(f <= 0)

# 使用随机梯度下降算法求解w, b
iteration = 1
while f[idx].size != 0:
    point = np.random.randint((f[idx].shape[0]))
    x = data[idx[0][point], :]
    y = label[idx[0][point]]
    w = w + alpha * y * x
    b = b + alpha * y
    print('Iteration:%d w:%s b:%s' % (iteration, w, b))
    f = (np.dot(data, w.T) + b) * label
    idx = np.where(f <= 0)
    iteration = iteration + 1

# 绘图演示
x1 = np.arange(0, 6, 0.1)
x2 = (w[0] * x1 + b) / (-w[1])
idx_p = np.where(label == 1)
idx_n = np.where(label != 1)
data_p = data[idx_p]
data_n = data[idx_n]
plt.scatter(data_p[:, 0], data_p[:, 1], color='red')
plt.scatter(data_n[:, 0], data_n[:, 1], color='blue')
plt.plot(x1, x2)
plt.show()
print('\nPerception leanring algorithm is over')
