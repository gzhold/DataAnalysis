import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn import tree
import graphviz


def trans_sex(x):
    if x == 'male':
        return 1
    else:
        return 0


train_data = pd.read_csv('./../data/titanic/train.csv')
test_data = pd.read_csv('./../data/titanic/test.csv', index_col=0)

# 使用平均年龄来填充年龄中的 nan 值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
# 使用票价的均值填充票价中的 nan 值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)

# 使用登录最多的港口来填充登录港口的 nan 值
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)

# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]



dvec = DictVectorizer(sparse=False)
#fit_transform 这个函数，它可以将特征向量转化为特征值矩阵。
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
#train_features = dvec.transform(train_features.to_dict(orient='record'))

print(dvec.feature_names_)


# 构造 ID3 决策树
clf = DecisionTreeClassifier(criterion='entropy')
# 决策树训练
clf.fit(train_features, train_labels)
test_features = dvec.transform(test_features.to_dict(orient='record'))
# 决策树预测
pred_labels = clf.predict(test_features)
#print(pred_labels)

# 得到决策树准确率
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score 准确率为 %.4lf' % acc_decision_tree)


#K 折交叉验证的原理是这样的：
#1 将数据集平均分割成 K 个等份；
#2 使用 1 份数据作为测试数据，其余作为训练数据；
#3 计算测试准确率；
#4 使用不同的测试集，重复 2、3 步骤。

# 使用 K 折交叉验证 统计决策树准确率
print(u'cross_val_score 准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))

# 决策树可视化
#dot_data = tree.export_graphviz(clf, out_file=None)
#graph = graphviz.Source(dot_data)
#graph.view()


#plt.show()
#print(df.head)