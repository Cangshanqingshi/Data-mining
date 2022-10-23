import numpy as np
import pandas as pd

# 读取数据(Iris)
def loadIris(address):
  spf = pd.read_csv(address, sep=',', index_col=False, header=None)
  strs = spf[4]
  # 用drop方法去掉最后一列字符串方便处理
  spf.drop([4], axis=1, inplace=True)
  return spf.values, strs


# 归一化
def normalization(data_matrix):
  e = 1e-5  # 防止出现0，加一个拉普拉斯因子
  for c in range(4):
    maxNum = np.max( data_matrix[:, c])
    minNum = np.min( data_matrix[:, c])
    # 利用最小-最大规范化公式进行归一化，统一至[0，1]区间
    data_matrix[:, c] = (data_matrix[:, c] - minNum + e)/(maxNum - minNum + e)
  return data_matrix


if __name__ == '__main__':
    fielpath = './data/iris.txt'
    writepath = './data/ans/iris_normal.txt'
    
    # read data
    data_matrix, str_name = loadIris(fielpath)
    # print(data_matrix)
    # normalization
    data_matrix = normalization(data_matrix)

    # 重新组合数据（标签无法归一化）
    spf = pd.DataFrame(data_matrix)

    # 保存归一化后的数据
    strs = str_name.values
    spf.insert(4, 4, strs)
    spf.to_csv(writepath, index=False, header=False)
