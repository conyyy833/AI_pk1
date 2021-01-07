import math

import numpy as np
from math import *

Data = np.genfromtxt("hospital.csv")

def PearsonCorrelation(xData, yData):
    if len(xData) != len(yData):
        raise RuntimeError('Incorrect data')
    xMeans = getMeans(xData)
    yMeans = getMeans(yData)
    numerator = generateNumerator(xData, xMeans, yData, yMeans)
    denominator = generateDenomiator(xData, xMeans, yData, yMeans)
    result = round(numerator / denominator, 2)
    return result

# generateNumerator
def generateNumerator(xData, xMeans, yData, yMeans):
    numerator = 0
    for i in range(1, len(xData)):
        numerator += (xData[i] - xMeans) * (yData[i] - yMeans)
    return numerator

# generateDenomiator
def generateDenomiator(xData, xMeans, yData, yMeans):
    xSum = 0
    for i in range(1, len(xData)):
        xSum += (xData[i] - xMeans) * (xData[i] - xMeans)
    ySum = 0
    for i in range(1, len(yData)):
        ySum += (yData[i] - yMeans) * (yData[i] - yMeans)
    return math.sqrt(xSum) * math.sqrt(ySum)

# getMeans
def getMeans(datas):
    sum = 0
    for i in range(1, len(datas)):
        sum += datas[i]
    mean = sum / (len(datas) - 1)
    return mean



#Eucledian Distance
def eculidSim1(x,y):
    return sqrt(sum(pow(a-b,2)for a,b in zip(x,y)))


#Manhattan Distance
def manhattan_dis(x,y):
    return sum(abs(a-b)for a,b in zip(x-y))


#Minkowski
def sumvalue(args):
    pass
def minkowski_dis(x, y, p):
    sumvalue+sum(pow(abs(a-b),p)for a,b in zip(x,y))
    mi=1/float(p)
    return round(sumvalue**mi,3)


#Cosine Similarity
def norm(x):
    pass
def cosine_dis(x,y):
    num=sum(map(float,x*y))
    denom=np.linalg,norm(x)*np.linalg.norm(y)
    return round(num/float(denom),3)


#Jaccard Similarity
def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x),set(y)]))
    union_cardinality = len(set.union(*[set(x),set(y)]))
    return intersection_cardinality/float(union_cardinality)
