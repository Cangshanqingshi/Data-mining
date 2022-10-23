# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 09:54:41 2022

@author: 李宏洋
"""
"""
import numpy as np
import pandas as pd

# 读取数据(Iris)
def loadIris(address):
  spf = pd.read_csv(address, sep=',', index_col=False, header=None)
  strs = spf[4]
  spf.drop([4], axis=1, inplace=True)
  return spf.values, strs


# 归一化
def normalization(data_matrix):
  e = 1e-5  # 防止出现0，加一个拉普拉斯因子
  for c in range(4):
    maxNum = np.max( data_matrix[:,c])
    minNum = np.min( data_matrix[:,c])
    data_matrix[:,c] = (data_matrix[:,c] - minNum + e)/(maxNum - minNum + e)
  return data_matrix


if __name__ == '__main__':
    fielpath = 'iris.txt'
    writepath = 'iris_normal.txt'
    
    # read data
    data_matrix, str_name = loadIris(fielpath)

    # normalization
    data_matrix = normalization(data_matrix)

    # 重新组合数据（标签无法归一化）
    spf = pd.DataFrame(data_matrix)
    strs = str_name.values
    spf.insert(4, 4, strs)

    # 保存归一化后的数据
    spf.to_csv(writepath, index= False, header= False)
    strs = str_name.values
    spf.insert(4, 4, strs)
    spf.to_csv(writepath, index = False, header = False)
"""


"""
import numpy as np
import pandas as pd
from collections import Counter


def loadLabor(address):
    spf = pd.read_csv(address, sep=',', index_col = False, header = None)
    column = []
    spf.columns = column

    # label data
    str_typename = []
    str2numeric = {}
    str2numeric['?'] = '-1'
    spf = spf.replace(str2numeric)
    return spf, str2numeric, str_typename


def fillMissData(spf, str2pnumeric):
    row, col = spf.shape
    columns = spf.columns
    for column_name in columns:
        if column_name not in str2pnumeric:
            # number,first strategy
            tmp = spf[column_name].apply(float)
            ave = np.average(tmp[tmp != -1])
            tmp[tmp == -1] = ave
            spf[column_name] = tmp
        else:
            # label,second strategy
            v = spf[column_name].values
            v1 = v[v != '-1']
            c = Counter(v1)
            cc = c.most_common(1)
            v[v = '-1'] = cc[0][0]
    return spf


if __name__ == '__main__':
    fielpath = 'laborMissing.txt'
    fillFilepath = 'laborMissing_handle.txt'
    spf, str2numeric, str2numeric = loadLabor(fielpath)
    spf = fillMissData(spf, str2numeric)
    spf.to_csv(fillFilepath, index = False, header = False)
"""


"""
import numpy as np
import pandas as pd
from collections import Counter


def loadIris(address):
  spf = pd.read_csv(address, sep=',', index_col=False, header=None)
  strs = spf[4]
  spf.drop([4], axis=1, inplace=True)
  return spf.values, strs


def featureSelection(features, label):
    featureLen = len(features[0,:])
    label_count = Counter(label)
    samples_energy = 0.0
    data_len = len(label)
    for i in label_count.keys():
        label_count[i] /= float(data_len)
        samples_energy -= label_count[i] * np.log2(label_count[i])

    informationGain = []

    for f in range(featureLen):
        af = features[:,f]
        minf = np.min(af)
        maxf = np.max(af) + 1e-4
        width =(maxf - minf)/10.0

        d = (af - minf)/width
        dd = np.floor(d)
        c = Counter(dd)
        sub_energy = getEnergy(c, dd, label)
        informationGain.append(samples_energy - sub_energy)
        return informationGain


def getEnergy(c, data, label):
    dataLen = len(label)
    energy = 0.0
    for key, value in c.items():
        c[key] /= float(dataLen)
        label_picked = label[data == key]
        l = Counter(label_picked)
        e = 0.0
        for k, v in l.items:
            r = v/float(values)
            e -= r * np.log2(r)
        energy += c[key] * e
    return energy


if _name_ == '_main_':
    fielpath = 'laborMissing.txt'
    data_matrix, str_name = loadIris(fielpath)
    informationGain = featureSelection(data_matrix, str_name.values)
    print(informationGain)
"""


import collections
import itertools

traDatas = ['abe', 'ae', 'abc', 'ade',]

class Apriori:
    traDatas = []
    traLen = 0
    k = 1
    traCount = {}
    freTran = {}
    sup = 0
    conf = 0
    freAllTran = {}


    def __init__(self, traDatas, sup, conf):
        self.traDatas = traDatas
        self.traLen = len(traDatas)
        self.sup = sup
        self.conf = conf


    def scanFirDatas(self):
        tmpStr = ''.join(traDatas)
        self.traCount = dict(collections.Counter(tmpStr))
        return self.traCount


    def getEreSet(self):
        self.freTran = {}
        for tra in self.traCount.keys():
            if self.traCount[tra] >= self.sup and len(tra) == self.k:
                self.freTran[tra] = self.traCount[tra]
                self.freAllTran[tra] = self.traCount[tra]


    def cmpTwoSet(self, setA, setB):
        setA = set(setA)
        setB = set(setB)
        if len(setA - setB) == 1 and len(setB - setA) == 1:
            return  True
        else:
            return False


    def selfConn(self):
        self.traCount = {}
        for item in cmpTwoSet(item[0])

    