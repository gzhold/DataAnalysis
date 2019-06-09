#!/usr/bin/env python
# -*- coding:utf8 -*-

import pandas as pd


# 加载数据集，你需要把数据放到目录中
data = pd.read_csv("./../data/greatLotto/2019-4-23-中国体彩网 - 开奖历史页-大乐透.csv")

# 数据探索
# 因为数据集中列比较多，我们需要把 dataframe 中的列全部显示出来
pd.set_option('display.max_columns', None)

print(data.columns)
print(data.head(5))