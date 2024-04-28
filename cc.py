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

modes = ["tianwu"]
bottoms_20 = {}
tops_20 = {}
mid_20 = {}
mid_40 = {}
mid_60 = {}
p99 = {}
loads = [0.8]
workloads = [""]
fcts = {}


def read_xml(xml_file, mode):
    tree = minidom.parse(xml_file)
    objs = tree.getElementsByTagName('Flow')
    for _, obj in enumerate(objs):
        t1 = obj.getAttribute('timeFirstTxPacket')
        t2 = obj.getAttribute('timeLastTxPacket')
        b = obj.getAttribute('txBytes')
        timeFirstTxPacket = obj.getAttribute('timeFirstTxPacket')
        if t1 and t2 and b:
            fcts[mode].append(int(t2[1:-4]) - int(t1[1:-4]))
            
if __name__ == '__main__':
    
    for mode in modes:
        print(mode, ":")
        fcts[mode] = []
        for seed in ["100"]:
            for load in loads:
                if mode+str(load) not in bottoms_20.keys():
                    bottoms_20[mode+str(load)] = []
                    tops_20[mode+str(load)] = []
                    p99[mode+str(load)] = []
                    mid_20[mode+str(load)] = []
                    mid_40[mode+str(load)] = []
                    mid_60[mode+str(load)] = []
                
                
                read_xml("test-1-large-load-8X8-"+str(load)+"-DcTcp-"+mode+"-simulation-"+seed+"-b600.xml", mode) 
                fcts[mode].sort()
                print(len(fcts[mode]))
                print(mode, load, sum(fcts[mode])/len(fcts[mode]))
                print(fcts[mode][int(0.999*len(fcts[mode]))])
    for mode in modes:
        print(mode)
        print(sum(fcts[mode])/len(fcts[mode]), fcts[mode][int(0.999*len(fcts[mode]))])
        # print()

    x = [30,40,50,60,70,80]
    x_major_locator=MultipleLocator(4)
    # print(y3)
    sns.set_style("whitegrid")
    matplotlib.rcParams.update({'font.size': 20, "font.weight": "bold"}) 
    plt.xticks(None, weight='bold')
    plt.xlim((40, 80))
    
    my_x_ticks = np.arange(40, 81, 10)
    shapes = ["ro-", "g*-", "k^-", "ys-", "bp-"]
    for i, mode in enumerate(modes):
        plt.plot(x, tops_20[mode], shapes[i], label=mode, linewidth=2.5, markersize=8)

    plt.legend(loc='upper left' )
    plt.tight_layout()
    # plt.tight_layout()
    # plt.show()
    plt.savefig("fc2.png")
    



