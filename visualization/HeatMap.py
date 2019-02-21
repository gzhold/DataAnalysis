#热力图


import matplotlib.pyplot as plt
import seaborn as sns
# 数据准备 使用 Seaborn 中自带的数据集 flights
flights = sns.load_dataset("flights")
data=flights.pivot('year','month','passengers')
# 用 Seaborn 画热力图
sns.heatmap(data)
plt.show()
