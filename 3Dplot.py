from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import numpy as np
import random

from single_sample_data import cell_count_list

path = "C:/Users/Jordan Chen/Desktop/要的/實驗室/data/2022 data/ROS/ROS_DHE excel檔/"

fig = plt.figure()
ax = plt.axes(projection='3d')

yaxis = 0
dy = 0.01
dx = 0.01

data1 = cell_count_list("WT1_0", 0, path)
data2 = cell_count_list("WT1_4", 0, path)
data3 = cell_count_list("WT1_6", 0, path)
data4 = cell_count_list("WT1_8", 0, path)
data5 = cell_count_list("WT1_12", 0, path)

def plot_(data, n = 1 , color="silver"):  #n:第幾行(y軸)
	data_h = plt.hist(data, bins=300, alpha = 0, color = color)
	z = list(data_h[0])
	z.append(0)
	ax.bar3d(data_h[1] , (n-1)* 50 , 0, dx, dy , z , color= color)

plot_(data1, 1, "black")
plot_(data2, 2, "silver")
plot_(data3, 3)
plot_(data4, 4)
plot_(data5, 5)







plt.show()




