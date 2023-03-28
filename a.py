import os
import xml.etree.ElementTree as ET
import math
import matplotlib.pyplot as plt
import numpy as np
from xml.dom import minidom
import matplotlib


import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns
import os
import requests
import pandas as pdq
import math
import pylab
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors
import mpl_scatter_density

from matplotlib.pyplot import MultipleLocator

ecmp = []
lf = []
xe = []
xf = []
    # y = []
def read_xml(xml_file, e):
    """
    读取xml文件，找到角度并存储进列表
    :param xml_file:xml文件的路径
    :return:
    """
    
    
    tree = minidom.parse(xml_file)
    objs = tree.getElementsByTagName('Flow')
    for ix, obj in enumerate(objs):
        t1 = obj.getAttribute('timeFirstTxPacket')
        t2 = obj.getAttribute('timeLastTxPacket')
        b = obj.getAttribute('txBytes')
        if t1 and t2 and b:
            if e:
                ecmp.append(int(t2[1:-4]) - int(t1[1:-4]))
                xe.append(int(b))
            else:
                lf.append(int(t2[1:-4]) - int(t1[1:-4]))
                xf.append(int(b))
        
if __name__ == '__main__':
    read_xml("0-1-large-load-4X4-0.8-Tcp-tianwu-simulation-500-3-b600.xml", 1) 
    read_xml("0-1-large-load-4X4-0.8-Tcp-letflow-simulation-500-3-b600.xml", 0)
    ecmp.sort()
    lf.sort()
    print(sum(ecmp)/len(ecmp))
    print(sum(lf)/len(lf))
    print(len(ecmp), len(lf))
    print(ecmp[int(0.999*len(ecmp))])
    print(lf[int(0.999*len(lf))])
    print(ecmp[-10:], lf[-10:])

    
    # x = [40,50,60,70,80]
    # x_major_locator=MultipleLocator(4)
    # print(y3)
    # sns.set_style("whitegrid")
    # matplotlib.rcParams.update({'font.size': 20, "font.weight": "bold"}) 
    # plt.xticks(None, weight='bold')

    # plt.xlim((40, 80))
    
    # my_x_ticks = np.arange(40, 81, 10)
    # my_y_ticks = np.arange(-2, 2, 0.3)
    # plt.xticks(my_x_ticks,weight='bold')
    
    # my_y_ticks = np.arange(10000000, 40000000, 10000000)
    # plt.yticks(my_y_ticks)
    # plt.plot(x, y99, 'ro-', label='ECMP', linewidth=2.5, markersize=8)
    # plt.plot(x, y991, 'g*-', label='LetFlow', linewidth=2.5, markersize=8)
    # plt.plot(x, y992, 'b^-', label='DRILL', linewidth=2.5, markersize=8)
    # plt.plot(x, y993, 'ys-', label='LFB', linewidth=2.5, markersize=8)
    
    # plt.plot(x, y50, 'ro-', label='ECMP', linewidth=2.5, markersize=8)
    # plt.plot(x, y501, 'g*-', label='LetFlow', linewidth=2.5, markersize=8)
    # plt.plot(x, y502, 'b^-', label='DRILL', linewidth=2.5, markersize=8)
    # plt.plot(x, y503, 'ys-', label='LFB', linewidth=2.5, markersize=8)
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
    
    # norm = mcolors.TwoSlopeNorm(vcenter=0)   
    # density = ax.scatter_density(xe, ecmp,norm=norm, cmap=plt.cm.RdBu)
    # ax.set_xlim(min(xe), max(xe))
    # ax.set_ylim(min(ecmp), max(ecmp))
    # fig.colorbar(density, label='Number of points per pixel')
    # fig.savefig('gaussian_color_coded.png')
    
    # plt.hist((np.array(xe), np.array(ecmp)))
    

    # plt.xlabel('link offered load %', weight="bold")
    # plt.ylabel('FCT(ns)', weight="bold")
    # plt.legend(loc='upper left' )
    # plt.tight_layout()
    # plt.tight_layout()
    # plt.show()
    # plt.savefig("fc.png")
    
    