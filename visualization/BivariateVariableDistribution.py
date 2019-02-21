#二元变量分布


import matplotlib.pyplot as plt
import seaborn as sns
# 数据准备
tips = sns.load_dataset("tips")
print(tips.head(10))
# 用 Seaborn 画二元变量分布图（散点图，核密度图，Hexbin 图）
#“kind=‘scatter’”代表散点图，“kind=‘kde’”代表核密度图，“kind=‘hex’代表 Hexbin 图，它代表的是直方图的二维模拟
sns.jointplot(x="total_bill", y="tip", data=tips, kind='scatter')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='kde')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='hex')
plt.show()
