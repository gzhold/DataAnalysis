#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
import jieba



# 加载数据
def load_data(base_path):
    """
    :param base_path: 基础路径
    :return: 分词列表，标签列表
    """
    documents = []
    labels = []
    # 循环所有文件并进行分词打标
    for root, dirs, files in os.walk(base_path):
        for file in files:
            label = root.split('/')[-1]
            filename = os.path.join(root, file)
            # 因为字符集问题因此直接用二进制方式读取
            with open(filename, 'rb') as f:
                content = f.read()
                word_list = list(jieba.cut(content))
                words = [wl for wl in word_list if wl not in stop_words]
                documents.append(' '.join(words))
                labels.append(labelMap[label]);
    return documents, labels

labelMap = {'体育': 0, '女性': 1, '文学': 2, '校园': 3}
#加载停用词
stop_words = [line.strip() for line in open('./../data/nativeBayes/stopword.txt').readlines()]

# 训练集
train_contents, train_labels = load_data('./../data/textClassification/train')

#计算单词的权重
tfidf_vec = TfidfVectorizer(stop_words=stop_words, max_df=0.5)
train_features = tfidf_vec.fit_transform(train_contents)

#print('每个单词的 ID:', tfidf_vec.vocabulary_)
#print('每个单词的 tfidf 值:', train_features.toarray())

# 多项式贝叶斯分类器
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)

#测试集
test_contents, test_labels = load_data('./../data/textClassification/test');

# vocabulary 词汇表：字典型
# max_df 参数用来描述单词在文档中的最高出现率。
# 假设 max_df=0.5，代表一个单词在 50% 的文档中都出现过了，那么它只携带了非常少的信息，因此就不作为分词统计(一般很少设置 min_df，因为 min_df 通常都会很小）。
test_tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5, vocabulary=tfidf_vec.vocabulary_)

# 用 fit_transform 方法进行拟合，得到 TF--IDF 特征空间 features，你可以理解为选出来的分词就是特征
test_features = test_tf.fit_transform(test_contents)

# 预测得到分类结果（predict 函数做的工作就是求解所有后验概率并找出最大的那个）
predicted_labels = clf.predict(test_features)

#计算准确率实际上是对分类模型的评估。accuracy_score 函数方便我们对实际结果和预测的结果做对比，给出模型的准确率。
print(metrics.accuracy_score(test_labels, predicted_labels))

