# -*- coding:utf-8 -*-
# 使用逻辑回归对信用卡欺诈进行分类
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_recall_curve
import itertools
from matplotlib.font_manager import FontProperties
from sklearn import svm, metrics

font_set = FontProperties(fname='/usr/local/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf', size=10)



# 混淆矩阵可视化
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix"', cmap=plt.cm.Blues):
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontproperties=font_set)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment='center',
                 color='white' if cm[i, j] > thresh else 'black')

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


# 显示模型评估结果
def show_metrics():
    tp = cm[1,1]
    fn = cm[1,0]
    fp = cm[0,1]
    tn = cm[0,0]
    print('精确率: {:.3f}'.format(tp/(tp+fp)))
    print('召回率: {:.3f}'.format(tp/(tp+fn)))
    print('F1 值: {:.3f}'.format(2*(((tp/(tp+fp))*(tp/(tp+fn)))/((tp/(tp+fp))+(tp/(tp+fn))))))

# 绘制精确率 - 召回率曲线
def plot_precision_recall():
    plt.step(recall, precision, color = 'b', alpha = 0.2, where = 'post')
    plt.fill_between(recall, precision, step ='post', alpha = 0.2, color = 'b')
    plt.plot(recall, precision, linewidth=2)
    plt.xlim([0.0,1])
    plt.ylim([0.0,1.05])
    plt.xlabel('召回率', fontproperties=font_set)
    plt.ylabel('精确率', fontproperties=font_set)
    plt.title('精确率 - 召回率 曲线', fontproperties=font_set)
    plt.show();



# 数据加载
data = pd.read_csv('./creditcard.csv')
# 数据探索
#print(data.describe())
# 设置 plt 正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制类别分布
plt.figure()
ax = sns.countplot(x='Class', data=data)
plt.title('类别分布', fontproperties=font_set)
plt.show()
# 显示交易笔数，欺诈交易笔数
num = len(data)
num_fraud = len(data[data['Class']==1])
print('总交易笔数: ', num)
print('诈骗交易笔数：', num_fraud)
print('诈骗交易比例：{:.6f}'.format(num_fraud/num))

# 欺诈和正常交易可视化
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(15,8))
bins = 50
ax1.hist(data.Time[data.Class == 1], bins=bins, color='deeppink')
ax1.set_title('诈骗交易', fontproperties=font_set)
ax2.hist(data.Time[data.Class == 0], bins=bins, color='deepskyblue')
ax2.set_title('正常交易', fontproperties=font_set)
plt.xlabel('时间', fontproperties=font_set)
plt.ylabel('交易次数', fontproperties=font_set)
plt.show()

# 对 Amount 进行数据规范化
data['Amount_Norm'] = StandardScaler().fit_transform(data['Amount'].values.reshape(-1, 1))
# 特征选择
y = np.array(data.Class.tolist())
data = data.drop(['Time', 'Amount', 'Class'], axis=1)
X = np.array(data.as_matrix())
# 准备训练集和测试集
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.1, random_state=33)


# 创建 SVM 分类器
model=svm.LinearSVC()
# 用训练集做训练
model.fit(train_x,train_y)
# 用测试集做预测
prediction=model.predict(test_x)
# 预测样本的置信分数
score_y = model.decision_function(test_x)

# 计算混淆矩阵，并显示
cm = confusion_matrix(test_y, prediction)
print('准确率: ', metrics.accuracy_score(prediction,test_y))

class_names = [0, 1]
# 显示混淆矩阵
plot_confusion_matrix(cm, classes=class_names, title='svm 混淆矩阵')
# 显示模型评估分数
show_metrics()
# 计算精确率，召回率，阈值用于可视化
precision, recall, thresholds = precision_recall_curve(test_y, score_y)
plot_precision_recall()