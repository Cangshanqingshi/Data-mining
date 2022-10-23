import collections
import itertools
import pandas as pd


# traDatas = ['abe', 'ae', 'abc', 'ade']
txt = open("./data/规则挖掘.txt", "r", encoding="utf-8").read()
traDatas = txt.split(",")
# print(traDatas)

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
        for item in itertools.combinations(self.freTran.keys(), 2):
            if self.cmpTwoSet(item[0], item[1]) == True:
                key = ''.join((sorted(''.join(set(item[0]).union(set(item[1]))))))
                if self.cutBranch(key) != False:
                    self.traCount[key] = 0

    def scanDatas(self):
        self.k = self.k +1
        for tra in traDatas:
            for key in self.traCount.keys():
                self.traCount[key] = self.traCount[key] + self.findChars(tra, key)

    def cutBranch(self, key):
        for subKey in list(itertools.combinations(key, self.k)):
            if ''.join(list(subKey)) not in self.freTran.keys():
                return False

    def findChars(self, str, chars):
        for char in list(chars):
            if char not in str:
                return False
        return 1

    def permutation(self, string, pre_str, container):
        if len(string) == 1:
            container.append(pre_str + string)
        for idx, str in enumerate(string):
            new_str = string[:idx] + string[idx + 1:]
            new_pre_str = pre_str + str
            self.permutation(new_str, new_pre_str, container)

    def genAssRule(self):
        container = []
        ruleSet = set()
        for item in self.freTran.keys():
            self.permutation(item, '', container)
        for item in container:
            for i in range(1, len(item)):
                # print(item[:i] + " " + item[i:])
                ruleSet.add((''.join(sorted(item[:i])), ''.join(sorted(item[i:]))))
        for rule in ruleSet:
            if self.calcConfi(rule[0], rule[1]) > self.conf:
                print(rule[0] + "---->>>" + rule[1])

    def calcConfi(self, first, last):
        return self.freAllTran[''.join(sorted(first+last))]/self.freAllTran[''.join(sorted(first))]

    def algorithm(self):
        self.scanFirDatas()
        while self.traCount != {}:
            self.getEreSet()
            self.selfConn()
            self.scanDatas()
        # print(self.freAllTran)
        # print(self.freTran)
        self.genAssRule()


apriori = Apriori(traDatas, 9, 0.999)
apriori.algorithm()