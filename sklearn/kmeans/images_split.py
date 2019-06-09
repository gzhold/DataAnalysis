# coding: utf-8


# 加载图像，并对数据进行规范化
from sklearn import preprocessing
import PIL.Image as image
import numpy as np
from sklearn.cluster import KMeans
from skimage import color


def load_data(filePath):
    # 读文件
    f = open(filePath, 'rb')
    data = []
    # 得到图像的像素值
    img = image.open(f)
    # 得到图像尺寸
    width, height = img.size
    for x in range(width):
        for y in range(height):
            # 得到点 (x,y) 的三个通道值
            c1, c2, c3 = img.getpixel((x, y))
            data.append([c1, c2, c3])
    f.close()
    # 采用 Min-Max 规范化
    mm = preprocessing.MinMaxScaler()
    data = mm.fit_transform(data)
    return np.mat(data), width, height


# 加载图像，得到规范化的结果 img，以及图像尺寸
img, width, height = load_data('./../data/kmeans/weixin.jpg')

# 用 K-Means 对图像进行 2 聚类
kmeans = KMeans(n_clusters=2)
kmeans.fit(img)
label = kmeans.predict(img)
# 将图像聚类结果，转化成图像尺寸的矩阵
label = label.reshape([width, height])
# 创建个新图像 pic_mark，用来保存图像聚类的结果，并设置不同的灰度值
pic_mark = image.new("L", (width, height))
for x in range(width):
    for y in range(height):
        # 根据类别设置图像灰度, 类别 0 灰度值为 255， 类别 1 灰度值为 127
        pic_mark.putpixel((x, y), int(256/(label[x][y]+1))-1)
pic_mark.save("./../data/kmeans/weixin_mark.jpg", "JPEG")


