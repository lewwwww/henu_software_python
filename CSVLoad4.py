# -*- coding:utf-8 -*-
# 混合绘图
#

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams["axes.unicode_minus"]=False
# arrstd=np.loadtxt(open("ScoreTest2.txt",encoding='utf8'),dtype=np.str,delimiter=',')

#
arrstd=np.loadtxt("e:\\ScoreTest.csv",dtype=bytes,delimiter=',',skiprows=1).astype(str)
# a=str(arrstd,'gbk')
# print(str(arrstd[2,1],"latin-1"))
# print(type(arrstd[2,1]))
# print(arrstd[2,1])
# a=arrstd
# print(a)
# arrstd=np.array([["1","张三",11,23,45],["1","李四",32,21,65]])

# a2=arrstd[0:,2:].astype(np.float32)
a2=arrstd
# print(a2)
a3=a2[ : , 7: 8].astype(int)
print(a3)

tarr=arrstd[:,1:7].astype(int)

print(tarr)
tmean=tarr.mean(axis=0)
print(tmean)
tdsl=tmean/20
print(tdsl)
########################################################################################
plt.figure("多图", figsize=(15, 8))
plt.subplot(121)
hist,bins=np.histogram(a3,bins=[0,60,70,80,90,100],range=(0,100))
print(hist)
print(bins)
# 构建数据
x = [50,60,70,80,90]
y = hist
# 绘制柱状图
plt.bar(x, y, width=5, color='steelblue',align='center')

# 设置标题及坐标轴名称
plt.title("成绩分布图")
plt.xlabel("分数段")
plt.ylabel("人数")
plt.axis([40,100,0,40])
plt.xticks(x,['60分以下','60-70分','70-80分','80-90分','90-100分'])
plt.grid(True)
for x, y in zip(x, y):
    plt.text(x, y+0.05, str(y), ha='center', va='bottom')
#########################################################################################

###############################################################################
#使用ggplot的绘图风格
# plt.style.use('ggplot')

#构建角度与值
# angles = np.array([0,np.pi/3,np.pi*2/3,np.pi*3/3,np.pi*4/3,np.pi*5/3])
angles=np.linspace(0,np.pi*2,6,endpoint=False)
print(angles)
data =tdsl  # [20,60,40,80,20,90]
data = np.concatenate((data, [data[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合
labels=['选择题','填空题','判断题','简答题','程序编写题','程序填空题']

plt.subplot(122,polar=True)

# plt.axis('off')
# plt.xticks([])
# plt.yticks([])
plt.polar(angles,data,"bo-",lw=1)

# plt.axis([0,np.pi*2,0,100])
# plt.xticks([0,np.pi/3,np.pi*2/3,np.pi*3/3,np.pi*4/3,np.pi*5/3],labels)
plt.thetagrids(angles * 180/np.pi, labels,y=0.02) # 做标签
#设置填充颜色，并且透明度为0.75
plt.fill(angles,data,'r',alpha=0.3)
plt.ylim(0,1)
for x, y in zip(angles, data):
    plt.text(x, y+0.09, round(y,2), ha='center', va='bottom')
plt.title("得分率雷达图",y=1.06,fontsize=15)
#显示网格线

plt.show()





















# hist,bins=np.histogram(a3,bins=[0,60,70,80,90,100],range=(0,100))
# print(hist)
# print(bins)
# # 构建数据
# x = [50,60,70,80,90]
# y = hist
# # 绘制柱状图
# plt.bar(x, y, width=5, color='steelblue',align='center')
#
# # 设置标题及坐标轴名称
# plt.title("成绩分布图")
# plt.xlabel("分数段")
# plt.ylabel("人数")
# plt.axis([40,100,0,40])
# plt.xticks(x,['60分以下','60-70分','70-80分','80-90分','90-100分'])
# plt.grid(True)
# for x, y in zip(x, y):
#     plt.text(x, y+0.05, str(y), ha='center', va='bottom')
#
# # 显示图表
# plt.show()
#
#
#
#
#
#
#
#
#
# # a4=a2[ : , 2: 7].astype(int)
# print(a4)
