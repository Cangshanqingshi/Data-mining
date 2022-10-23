import numpy as np
import matplotlib.pyplot as plt


# BP网络
def BP(x, y, num):
    epochs = 20000
    learning_rate = 0.3
    times = 0

    I_num = x.shape[0]
    H_num = num
    O_num = y.shape[0]

    V = np.random.rand(I_num, H_num) - 0.5
    dV = np.random.rand(I_num, H_num)

    W = np.random.rand(H_num, O_num) - 0.5
    dW = np.random.rand(H_num, O_num)

    mse_record = np.ones((1, epochs))

    for step in range(epochs):
        # Forward
        H_in = np.dot(x, V)      # 1 x H_num
        H_out = sigmoid(H_in)   # 1 x H_num
        O_in = np.dot(H_out, W) # 1 x O_num
        O_out = O_in            # 1 x O_num

        error = (O_out - y)     # 1 x O_num

        mse = np.average(np.square(error))
        mse_record[0, step] = mse
        if mse < 4e-4:
            break

        # Backward
        # 更新W
        for h in range(H_num):
            for j in range(O_num):
                # W 偏导
                dW[h, j] = (y[j]- O_out[j]) * H_out[h]

        # 更新V
        for i in range(I_num):
            for h in range(H_num):
                sum = 0
                for j in range(O_num):
                    sum = sum + (y[j] - O_out[j]) * O_out[j] * (H_out[h]) * W[h, j]
                dV[i, h] = sum * H_out[h] * x[i]

        W = W + learning_rate * dW
        V = V + learning_rate * dV
        times = step
    print(V)
    print(W)
    print(30*'-')
    print(step, O_out)
    return times



def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


def sigmoid_dervative(x):
    s = 1 / (1 + np.exp(-x))
    ds = s * (1 - s)
    return ds


if __name__ == "__main__":
    x = np.array([2, 5], dtype=float)
    y_true = np.array([3, 6, 4], dtype=float)
    BP(x, y_true, 12)
    # traintime = {}
    # for j in range(3, 15, 3):
    #     totaltimes = []
    #     for i in range(100):
    #         totaltimes.append(BP(x, y_true, j))
    #     average = np.mean(totaltimes)
    #     traintime[j] = average
    # print(traintime)
