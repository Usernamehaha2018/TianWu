from re import M
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
from xml.dom import minidom
import seaborn as sns
import pandas as pdq
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors
from matplotlib.pyplot import MultipleLocator
import matplotlib
if __name__=="__main__":
    f = open("aa")               # 返回一个文件对象 
    line = f.readline()               # 调用文件的 readline()方法 
    x1 = []
    y1 = []
    x2,y2,x3,y3,x4,y4 = [], [], [], [],[], []
    while line: 
        a = line.split(" ")
        if len(a) == 3:
            try:
                if float(a[0]) > 0.001:
                    if float(a[0]) < 0.1 and a[1] == "10.1.1.2":
                        x1.append(float(a[0]))
                        y1.append(int(a[2]))
                        # print(a[0])
                    if float(a[0]) < 0.1 and a[1] == "10.1.1.8":
                        x2.append(float(a[0]))
                        y2.append(int(a[2]))
                    # print(a[0])
                    if float(a[0]) < 0.1 and a[1] == "10.1.1.4":
                        x3.append(float(a[0]))
                        y3.append(int(a[2]))
                    if float(a[0]) < 0.1 and a[1] == "10.1.1.6":
                        x4.append(float(a[0]))
                        y4.append(int(a[2]))
            except:
                pass
            
        line = f.readline() 
    
    sns.set_style("whitegrid")
    matplotlib.rcParams.update({'font.size': 15, "font.weight": "bold"}) 
    plt.xticks(None, weight='bold')
        
    y_major_locator=MultipleLocator(100000)
    ax=plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    plt.ylim(0,300000)
    plt.xlim(0,0.1)
    plt.plot(x1,y1,"ro-",label='Flow 1')
    plt.plot(x2,y2,"g*-", label='Flow 2')
    plt.plot(x3,y3,"b^-", label='Flow 3')
    plt.plot(x4,y4,"ys-", label='Flow 4')
    plt.xlabel('Time (s)', weight="bold")
    plt.ylabel('Cwnd', weight="bold")
    plt.legend(loc='upper right' )
    plt.tight_layout()

    plt.savefig("f.png")
 
    f.close()