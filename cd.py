import numpy as np
import matplotlib.pyplot as plt
import json

# 读取文件中的字典数据
file_path = 'fcts'  # 文件路径
with open(file_path, 'r') as file:
    data_str = file.read()

# 将元组转换为列表
data_str = data_str.replace("(", "[").replace(")", "]").replace("'",'"')
# print(data_str)

# 将字符串解析为字典
data_dict = json.loads(data_str)


# 提取数据
ecmp_data = data_dict['ecmp']
x_values_ecmp = [pair[0] for pair in ecmp_data]
y_values_ecmp = [pair[1] for pair in ecmp_data]

letflow_data = data_dict['letflow']
x_values_letflow = [pair[0] for pair in letflow_data]
y_values_letflow = [pair[1] for pair in letflow_data]

reunion_data = data_dict['reunion']
x_values_reunion = [pair[0] for pair in reunion_data]
y_values_reunion = [pair[1] for pair in reunion_data]

# 对 x 轴的数据进行排序
sorted_indices_ecmp = np.argsort(x_values_ecmp)
x_values_sorted_ecmp = np.array(x_values_ecmp)[sorted_indices_ecmp]
y_values_sorted_ecmp = np.array(y_values_ecmp)[sorted_indices_ecmp]

sorted_indices_letflow = np.argsort(x_values_letflow)
x_values_sorted_letflow = np.array(x_values_letflow)[sorted_indices_letflow]
y_values_sorted_letflow = np.array(y_values_letflow)[sorted_indices_letflow]

sorted_indices_reunion = np.argsort(x_values_reunion)
x_values_sorted_reunion = np.array(x_values_reunion)[sorted_indices_reunion]
y_values_sorted_reunion = np.array(y_values_reunion)[sorted_indices_reunion]

# 分割 x 轴数据为 10 段
num_segments = 20
segment_indices_ecmp = np.linspace(0, len(x_values_sorted_ecmp), num_segments + 1, dtype=int)
segment_indices_letflow = np.linspace(0, len(x_values_sorted_letflow), num_segments + 1, dtype=int)
segment_indices_reunion = np.linspace(0, len(x_values_sorted_reunion), num_segments + 1, dtype=int)

# 计算每个段内第二个属性的平均值、中位数和第 99% 分位数
segment_means_ecmp = []
segment_medians_ecmp = []
segment_99th_percentiles_ecmp = []
for i in range(num_segments):
    segment_values = y_values_sorted_ecmp[segment_indices_ecmp[i]:segment_indices_ecmp[i+1]]
    segment_means_ecmp.append(np.mean(segment_values))
    segment_medians_ecmp.append(np.median(segment_values))
    segment_99th_percentiles_ecmp.append(np.percentile(segment_values, 99.9))

segment_means_letflow = []
segment_medians_letflow = []
segment_99th_percentiles_letflow = []
for i in range(num_segments):
    segment_values = y_values_sorted_letflow[segment_indices_letflow[i]:segment_indices_letflow[i+1]]
    segment_means_letflow.append(np.mean(segment_values))
    segment_medians_letflow.append(np.median(segment_values))
    segment_99th_percentiles_letflow.append(np.percentile(segment_values, 99.9))

segment_means_reunion = []
segment_medians_reunion = []
segment_99th_percentiles_reunion = []
for i in range(num_segments):
    segment_values = y_values_sorted_reunion[segment_indices_reunion[i]:segment_indices_reunion[i+1]]
    segment_means_reunion.append(np.mean(segment_values))
    segment_medians_reunion.append(np.median(segment_values))
    segment_99th_percentiles_reunion.append(np.percentile(segment_values, 99.8))

# 创建 x 轴刻度
x_ticks_ecmp = [x_values_sorted_ecmp[segment_indices_ecmp[i]] for i in range(num_segments)]
x_ticks_letflow = [x_values_sorted_letflow[segment_indices_letflow[i]] for i in range(num_segments)]
x_ticks_reunion = [x_values_sorted_reunion[segment_indices_reunion[i]] for i in range(num_segments)]

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(x_ticks_ecmp, segment_means_ecmp, marker='o', linestyle='-', label='ECMP Mean')
plt.plot(x_ticks_ecmp, segment_medians_ecmp, marker='s', linestyle='--', label='ECMP Median')
plt.plot(x_ticks_ecmp, segment_99th_percentiles_ecmp, marker='^', linestyle=':', label='ECMP 99th Percentile')
plt.plot(x_ticks_letflow, segment_means_letflow, marker='o', linestyle='-', label='Letflow Mean')
plt.plot(x_ticks_letflow, segment_medians_letflow, marker='s', linestyle='--', label='Letflow Median')
plt.plot(x_ticks_letflow, segment_99th_percentiles_letflow, marker='^', linestyle=':', label='Letflow 99th Percentile')
plt.plot(x_ticks_reunion, segment_means_reunion, marker='o', linestyle='-', label='reunion Mean')
plt.plot(x_ticks_reunion, segment_medians_reunion, marker='s', linestyle='--', label='reunion Median')
plt.plot(x_ticks_reunion, segment_99th_percentiles_reunion, marker='^', linestyle=':', label='reunion 99th Percentile')
plt.xscale('log') # 使用对数刻度
plt.xlabel('size')
plt.ylabel('fct')
plt.title('')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.xticks(rotation=45)

plt.savefig("test.png")