import matplotlib.pyplot as plt
import numpy as np

# 五组数据
data ,data2 = [[2, 4, 4, 3, 3, 2, 3, 6], [10, 15, 11, 11, 15, 16, 17, 14], [12, 10, 11, 16, 16, 19, 15, 17], [17, 12, 22, 17, 19, 17, 12, 17], [22, 14, 29, 22, 19, 21, 26, 18]] , [[66, 78, 69, 72, 71, 90, 73, 74], [114, 116, 102, 119, 133, 138, 123, 99], [145, 137, 139, 132, 120, 131, 124, 110], [139, 142, 163, 128, 119, 117, 154, 134], [150, 137, 147, 119, 135, 154, 143, 158]]
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
        ax.bar(subbar_x, value, subbar_width, color='blue' ,edgecolor='black')  # 蓝色部分
        ax.bar(subbar_x, data2[i][j]-value, subbar_width, color='orange', bottom=value, edgecolor='black')  # 橙色部分

# 设置图例
blue_patch = plt.Rectangle((0,0),1,1,fc="blue", edgecolor = 'none')
orange_patch = plt.Rectangle((0,0),1,1,fc='orange',  edgecolor = 'none')
ax.legend([blue_patch, orange_patch], ['Recorded Flows', 'Other Flows'])

# 设置刻度和标签
ax.set_xlabel('Time')
ax.set_ylabel('Count')
ax.set_title('Flow Count')

# 设置 x 轴刻度标签
ax.set_xticks(index + 0.35 / 2)
ax.set_xticklabels(('+500000.0ns', '+1000000.0ns', '+1500000.0ns', '+2000000.0ns','+2500000.0ns'))

plt.savefig("b9.png")