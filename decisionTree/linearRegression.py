from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

boston=load_boston()

# 通过DESCR属性可以查看数据集的详细情况，这里数据有14列，前13列为特征数据，最后一列为标签数据。
#print(boston.DESCR)

# 特征
#print(boston.data)
# 标签
#print(boston.target)

# 随机抽取 33% 的数据作为测试集，其余为训练集
features = boston.data
prices = boston.target
X_train, X_test, y_train, y_test = train_test_split(features, prices, test_size=0.2, random_state=2)

"""
普通的线性回归模型太简单，容易导致欠拟合，我们可以增加特征多项式来让线性回归模型更好地拟合数据。
在sklearn中，通过preprocessing模块中的PolynomialFeatures来增加特征多项式。
其重要参数有：
degree：多项式特征的个数，默认为2
include_bias：默认为True，包含一个偏置列，也就是用作线性模型中的截距项，这里选择False，
因为在线性回归中，可以设置是否需要截距项。
"""
poly=PolynomialFeatures(degree=2,include_bias=False)
X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.fit_transform(X_test)


"""
线性算法使用sklearn.linear_model 模块中的LinearRegression方法。
常用的参数如下：
fit_intercept：默认为True，是否计算截距项。
normalize：默认为False，是否对数据归一化。
"""
# 简单线性回归
model2=LinearRegression(normalize=True)
model2.fit(X_train,y_train)
score2 = model2.score(X_test,y_test)
print(score2)

# 多项式线性回归
model3=LinearRegression(normalize=True)
model3.fit(X_train_poly,y_train)
score3 = model3.score(X_test_poly,y_test)
print(score3)

"""
总结
多项式的个数的不断增加，可以在训练集上有很好的效果，但缺很容易造成过拟合，没法在测试集上有很好的效果，
也就是常说的：模型泛化能力差。
"""
