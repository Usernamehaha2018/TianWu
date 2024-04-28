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

# modes = ["clove","ecmp" ]
modes = [ "tianwu"]
bottoms_20 = {}
tops_20 = {}
mid_20 = {}
mid_40 = {}
mid_60 = {}
p99 = {}
loads = [0.8]
# loads = [0]
workloads = [""]
fcts = {}
freq = [0.5,0.6,0.7]
to = [0.2,0.3,0.4,0.5]


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
            # ml
            if  int(t1[1:-4]) == 200:
                fcts[mode].append(int(t2[1:-4]) - int(t1[1:-4]))
                # print(b, int(t2[1:-4]) - int(t1[1:-4]))
    print(len(fcts[mode]))
            
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
                for f in freq:
                    for t in to:
                        read_xml(str(f)+"-"+str(t)+"-test-1-large-load-8X8-"+str(load)+"-DcTcp-"+mode+"-simulation-"+seed+"-b600.xml", mode) 
                        fcts[mode].sort()
                    # print(fcts)
                        print(f,t, load, sum(fcts[mode])/len(fcts[mode]), fcts[mode][int(0.999*len(fcts[mode]))])
                        fcts[mode] = []

    for mode in modes:
        print(mode)
        print(sum(fcts[mode])/len(fcts[mode]), fcts[mode][int(0.999*len(fcts[mode]))])
    plt.legend(loc='upper left' )
    plt.tight_layout()
    plt.savefig("fc2.png")
    
    