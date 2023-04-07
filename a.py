from re import M
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
from xml.dom import minidom
import seaborn as sns
import pandas as pdq
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors
# import mpl_scatter_density

from matplotlib.pyplot import MultipleLocator
import matplotlib

modes = [ "letflow","ecmp", "drill", "clove" ]
bottoms_20 = {}
tops_20 = {}
loads = [0.3, 0.4]
# loads = [0.6,0.7,0.8]
workloads = ["ml", "datamining"]
fcts = {}


def read_xml(xml_file, mode):
    tree = minidom.parse(xml_file)
    objs = tree.getElementsByTagName('Flow')
    for _, obj in enumerate(objs):
        t1 = obj.getAttribute('timeFirstTxPacket')
        t2 = obj.getAttribute('timeLastTxPacket')
        b = obj.getAttribute('txBytes')
        if t1 and t2 and b:
            fcts[mode].append(int(t2[1:-4]) - int(t1[1:-4]))

if __name__ == '__main__':
    for mode in modes:
        print(mode, ":")
        bottoms_20[mode] = []
        tops_20[mode] = []
        for load in loads:
            fcts[mode] = []
            read_xml("0-1-large-load-4X4-"+str(load)+"-DcTcp-"+mode+"-simulation-1-b600.xml", mode) 
            fcts[mode].sort()
            print(sum(fcts[mode])/len(fcts[mode]))
            print(fcts[mode][int(0.999*len(fcts[mode]))])
            # print(fcts[mode][-1])
            # print(fcts[mode][-10:])
            bottom_20 = int(0.2*len(fcts[mode]))
            bottoms_20[mode].append(sum(fcts[mode][-bottom_20:])/bottom_20)
            tops_20[mode].append(sum(fcts[mode][:bottom_20])/bottom_20)
    print(bottoms_20,tops_20)


    
    x = [40,50,60,70,80]
    x_major_locator=MultipleLocator(4)
    # print(y3)
    sns.set_style("whitegrid")
    matplotlib.rcParams.update({'font.size': 20, "font.weight": "bold"}) 
    plt.xticks(None, weight='bold')
    plt.xlim((40, 80))
    
    my_x_ticks = np.arange(40, 81, 10)
    # my_y_ticks = np.arange(-2, 2, 0.3)
    # plt.xticks(my_x_ticks,weight='bold')
    
    # my_y_ticks = np.arange(10000000, 40000000, 10000000)
    # plt.yticks(my_y_ticks)
    shapes = ["ro-", "g*-", "k^-", "ys-", "bp-"]
    for i, mode in enumerate(modes):
        plt.plot(x, tops_20[mode], shapes[i], label=mode, linewidth=2.5, markersize=8)
        
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
    plt.legend(loc='upper left' )
    plt.tight_layout()
    # plt.tight_layout()
    # plt.show()
    plt.savefig("fc2.png")
    
#     mywang@tian-609-11:~/TianWu$ python3 a.py 
# letflow :
# 16366204.060495535
# 3312744584
# 1612758142
# ecmp :
# 16546095.770280467
# 3140461259
# drill :
# 19111474.617972583
# 3384930689
# clove :
# 15020501.284398189
# 2726312917
