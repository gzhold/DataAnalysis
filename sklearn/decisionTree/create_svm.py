from math import log
import operator


# 创建数据集
def creatDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# 计算数据集熵的函数
def calcshannon(dataSet):
    num = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannon = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / num
        shannon -= prob * log(prob, 2)
    return shannon


#划分数据集的函数，参数为：待划分的数据，划分的特征和返回的特征值
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
       if featVec[axis] == value:
           reduce = featVec[:axis]
           reduce.extend(featVec[axis+1:])
           retDataSet.append(reduce)
    return retDataSet


def choose(dataSet):
    numfeature = len(dataSet[0]) - 1
    baseEntropy = calcshannon(dataSet)
    bestinfogain = 0.0
    bestfeature = -1
    for i in range(numfeature):
        featlist = [example[i] for example in dataSet]
        vals = set(featlist)
        newEntropy = 0.0
        for value in vals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcshannon(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestinfogain):
            bestinfogain = infoGain
            bestfeature = i
        return bestfeature


def majority(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedcount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True)
    return sortedcount[0][0]



def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majority(classList)
    bestFeat = choose(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del (labels[bestFeat])
    Vals = [example[bestFeat] for example in dataSet]
    uvals = set(Vals)
    for value in uvals:
        sublabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), sublabels)
    return myTree



dataset, labels = creatDataSet()
tree = createTree(dataset, labels)
print(tree)















