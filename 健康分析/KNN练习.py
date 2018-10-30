# Author: Yan

import numpy as np
import pandas as pd
import operator

#读取处理数据
def dataRead():
    #读取并贴好标签
    dataSet = pd.read_table('D:\yandata\datingTestSet.txt',names=['a','b','c','r'])
    #进行值替换
    dataSeted = dataSet.replace({'didntLike':1,'smallDoses':2,'largeDoses':3})
    #划分数据
    rules = dataSeted[['r']]
    reason = dataSeted[['a','b','c']]
    taringdata_re = reason[:899]
    testdata_re = reason[899:]
    taringdata_ru = rules[:899]
    testdata_ru = rules[899:]
    #训练数据
    taringdata1 = taringdata_re.values
    lables1 = taringdata_ru.values.tolist()
    #测试数据
    testdata2 = testdata_re.values
    lables2 = testdata_ru.values.tolist()
    return taringdata1,lables1,testdata2,lables2












