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
    info = {}
    for f in range(featureLen):
        af = features[:, f]
        minf = np.min(af)
        maxf = np.max(af) + 1e-4
        width =(maxf - minf)/10.0
        d = (af - minf)/width
        dd = np.floor(d)
        c = Counter(dd)
        sub_energy = getEnergy(c, dd, label)
        informationGain.append(samples_energy - sub_energy)
        info['第{}列对应特征的信息增益'.format(f+1)] = samples_energy - sub_energy

    return informationGain, info


def getEnergy(c, data, label):
    dataLen = len(label)
    energy = 0.0
    for key, value in c.items():
        c[key] /= float(dataLen)
        label_picked = label[data == key]
        l = Counter(label_picked)
        e = 0.0
        for k, v in l.items():
            r = v/float(value)
            e -= r * np.log2(r)
        energy += c[key] * e
    return energy


if __name__ == '__main__':
    fielpath = './data/iris.txt'
    data_matrix, str_name = loadIris(fielpath)
    informationGain,info = featureSelection(data_matrix, str_name.values)
    print(info)
    d_order = sorted(info.items(), key=lambda x: x[1], reverse=True)
    print(d_order)
    # print(informationGain)
