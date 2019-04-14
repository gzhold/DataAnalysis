import pandas as pd
import numpy as np
from pyecharts import Pie


data = pd.read_csv('friend.csv',encoding='utf-8')
#print(data.head())

sex = data.groupby('Sex')['Sex'].count()
#print(sex)

#province = data.groupby('Province')['Province'].count()
#print(province)


attr = ['外星人','男性','女性']

v = list(sex)
pie = Pie("微信好友性别分布",  width=900)
"""
add(name,attr,value,radius = None,center = None,rosetype = None,**kwargs)
attr:属性名称
radius：饼图半径，数组第一项是内径，第二项是外径，默认[0,75,],设置成百分比
center：圆心，数组第一项是X轴，第二项是Y轴，默认[50,50]
rosetype: 是否展示成南丁格尔图，用过半径区分数据大小，radius和area两种模式，默认radius
"""
pie.add(
    "",
    attr,
    v,
    center=[50, 50],
    is_random=True,
    radius=[30, 75],
    rosetype="radius",
)
#print(pie)
pie.render('./html/pie01.html')
