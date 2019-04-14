import pandas as pd
import numpy as np
from pyecharts import Bar


data = pd.read_csv('friend1.csv',encoding='utf-8')
sex = data.groupby('Sex')['Sex'].count()
attr = ['外星人','男性','女性']

v = list(sex)
bar = Bar("微信好友性别分布",'')
bar.add('',
        attr,
        v,
        [5,20,36,10,75,90]
        )
#bar.show_config()               #调试输出pyecharts的js配置信息
bar.render('./html/first01.html')