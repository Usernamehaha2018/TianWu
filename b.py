import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 4, 9, 16, 25, 36, 49]
plt.title(r'$y=x^2$')
#r'$公式$'可以使用latex语法写公式
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y)
if __name__ == "__main__":
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    with open('aa', 'r') as file:
        for line in file:
            numbers = line.split()  # 以空格分隔每个数字
            if len(numbers) == 2:
                x1.append(float(numbers[0]) ) # 将字符串转换为浮点数
                y1.append( float(numbers[1]) ) # 将字符串转换为浮点数
    with open('bb', 'r') as file:
        for line in file:
            numbers = line.split()  # 以空格分隔每个数字
            if len(numbers) == 2:
                try:
                    x2.append(float(numbers[0]) ) # 将字符串转换为浮点数
                    y2.append( float(numbers[1]) ) # 将字符串转换为浮点数
                except:
                    x2 = x2[:-1]
    plt.plot(x1,y1,label="t")
    plt.plot(x2,y2,label="l")
    plt.legend(loc='upper left' )
    plt.savefig("f.png")

    
