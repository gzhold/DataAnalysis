#!/usr/bin/env python
# -*- coding:utf8 -*-

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeRegressor



# 加载数据集，你需要把数据放到目录中
data = pd.read_csv("./../data/housingPrice/2019-4-23-【杭州商铺杭州门面杭州商铺网】-杭州58同城.csv")

# 数据探索
# 因为数据集中列比较多，我们需要把 dataframe 中的列全部显示出来
pd.set_option('display.max_columns', None)
#columns=['标题', '标题链接', '缩略图', '面积', '区域', 'tag-first', '特点', '位置', '价格（元/月）', '发布时间', '状态','tag-second', '日租金', 'picNum', 'tag-third', 'tag-fourth']
data.drop("标题链接", axis=1, inplace=True)
data.drop("缩略图", axis=1, inplace=True)
data.drop("picNum", axis=1, inplace=True)

data['time'] = data['time'].map({'今天': '2019-04-25', '广告': '2019-04-23'})

data['unit'] = data['unit'].astype('str')
# 删除左右两边空格
data['unit'] = data['unit'].map(str.strip)
# 合并列
data['tag'] = data['tag-first'].str.cat(data['tag-second'], sep=',').str.cat(data['tag-third'], sep=',').str.cat(data['tag-fourth'], sep=',')
data.drop("tag-first", axis=1, inplace=True)
data.drop("tag-second", axis=1, inplace=True)
data.drop("tag-third", axis=1, inplace=True)
data.drop("tag-fourth", axis=1, inplace=True)

data['address'] = data['list-info1'].str.cat(data['list-info3'], sep=',')
data.drop("list-info1", axis=1, inplace=True)
data.drop("list-info3", axis=1, inplace=True)

data['address'].fillna("未知", inplace=True)
data['list-info4'].fillna("空置中", inplace=True)
data['tag'].fillna("新房", inplace=True)

data['list-info'] = data['list-info'].replace("m²", '', regex=True)
#\n\t\t\t\t                元/㎡/天
data['unit'] = data['unit'].replace("\n\t\t\t\t                元/㎡/天", '', regex=True)
#data['unit'].astype(np.long)
#data['unit'].fillna(data['unit'].mean(), inplace=True)

#data['sum'] = data['sum'].filter("面议").transform(lambda x: x.fillna(x.mean()))
#data['sum'] = data['sum'].map(str.strip).replace("面议", '', regex=True)
#data['sum'].fillna(data['sum'].mean(), inplace=True)

#print(data.columns)
#print(data.head(5))
print(data['sum'])
#print(data.info())
#print(data.describe())

# 规范化到 [0,1] 空间
min_max_scaler = preprocessing.MinMaxScaler()


# 特征选择
features = ['list-info', 'list-info2', 'list-info4', 'unit', 'tag', 'address']

# 抽取 30% 的数据作为测试集，其余作为训练集
train, test = train_test_split(data, test_size=0.33)
train_features = train[features]
train_labels = data['sum']
test_features = test[features]


# 构造 ID3 决策树
clf = DecisionTreeRegressor()
train_x = min_max_scaler.fit_transform(train_labels)
# 决策树训练
clf.fit(train_features, train_x)

dvec = DictVectorizer(sparse=False)
test_features = dvec.transform(test_features.to_dict(orient='record'))
# 决策树预测
pred_labels = clf.predict(test_features)
#print(pred_labels)

# 得到决策树准确率
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score 准确率为 %.4lf' % acc_decision_tree)

# 使用 K 折交叉验证 统计决策树准确率
print(u'cross_val_score 准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))

