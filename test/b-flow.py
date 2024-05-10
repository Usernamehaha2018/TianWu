import matplotlib.pyplot as plt
import numpy as np

# 五组数据
data ,data2 = [[0.0584938, 0.100326, 0.0683, 0.101065, 0.0521468, 0.048614, 0.0369906, 0.0329436], [0.402531, 0.839765, 0.494774, 0.607774, 0.609075, 0.358398, 0.544778, 0.248162], [0.784908, 0.271328, 0.508366, 0.374896, 0.525778, 0.419207, 0.768931, 0.393772], [0.751522, 0.59923, 0.616257, 0.571678, 0.451676, 0.418568, 0.49806, 0.640275], [0.646845, 0.72767, 0.422984, 0.482278, 0.758517, 0.435666, 0.78842, 0.70988]] , [[0.0203838, 0.0394266, 0.0303868, 0.056836, 0.0227714, 0.0184256, 0.0167422, 0.0151034], [0.321608, 0.745753, 0.422441, 0.552691, 0.536058, 0.308595, 0.463645, 0.19295], [0.702945, 0.171633, 0.414129, 0.327662, 0.455208, 0.359048, 0.66525, 0.326602], [0.684992, 0.541434, 0.551134, 0.495568, 0.399204, 0.363353, 0.423749, 0.59816], [0.58083, 0.64599, 0.349786, 0.401211, 0.697592, 0.365669, 0.712704, 0.658065]]
# 设置每个 bar 包含的子 bar 的数量
num_subbars = 8

# 设置每组数据的偏移量
index = np.arange(len(data))

# 子 bar 的宽度
subbar_width = 0.35 / num_subbars  # 每个 bar 的宽度是 0.35，将其等分为三部分

# 创建画布和子图
fig, ax = plt.subplots()

# 为每组数据创建直方图
for i, group_data in enumerate(data):
    for j, value in enumerate(group_data):
        # 计算子 bar 的位置
        subbar_x = index[i] + j * subbar_width
        
        # 绘制每个子 bar 的两部分
        ax.bar(subbar_x, data2[i][j], subbar_width, color='blue' ,edgecolor='black')  # 蓝色部分
        ax.bar(subbar_x, value-data2[i][j], subbar_width, color='orange', bottom=data2[i][j], edgecolor='black')  # 橙色部分

# 设置图例
blue_patch = plt.Rectangle((0,0),1,1,fc="blue", edgecolor = 'none')
orange_patch = plt.Rectangle((0,0),1,1,fc='orange',  edgecolor = 'none')
ax.legend([blue_patch, orange_patch], ['Recorded Flows', 'Other Flows'])

# 设置刻度和标签
ax.set_xlabel('Time')
ax.set_ylabel('load')
ax.set_title('')

# 设置 x 轴刻度标签
ax.set_xticks(index + 0.35 / 2)
ax.set_xticklabels(('+500000.0ns', '+1000000.0ns', '+1500000.0ns', '+2000000.0ns','+2500000.0ns'))

plt.savefig("bflow8.png")