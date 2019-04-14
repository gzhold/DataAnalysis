import pandas as pd


# 数据加载
train_data = pd.read_csv('./../data/titanic/train.csv')
test_data = pd.read_csv('./../data/titanic/test.csv', index_col=0)

# 使用平均年龄来填充年龄中的 nan 值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
# 使用票价的均值填充票价中的 nan 值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)


print(train_data['Embarked'].value_counts())
print('-'*30)

# 使用登录最多的港口来填充登录港口的 nan 值
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S',inplace=True)


# 使用 info() 了解数据表的基本情况：行数、列数、每列的数据类型、数据完整度
print(train_data.info())
print('-'*30)

# 使用 describe() 了解数据表的统计情况：总数、平均值、标准差、最小值、最大值等
print(train_data.describe())
print('-'*30)

# 使用 describe(include=[‘O’]) 查看字符串类型（非数字）的整体情况
print(train_data.describe(include=['O']))
print('-'*30)

# 使用 head 查看前几行数据（默认是前 5 行
print(train_data.head())
print('-'*30)

# 使用 tail 查看后几行数据（默认是最后 5 行
print(train_data.tail())
