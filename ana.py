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
modes = [ "tianwu","letflow"]
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


def read_file(file, mode):
    with open(file, "r") as f:
        for line in f:
            try:
                data = [int(i) for i in line.split()]
                fcts[mode].append(data[1]-data[0])
            except:
                pass
            
if __name__ == '__main__':
    
    for mode in modes:
        print(mode, ":")
        fcts[mode] = []
        for seed in ["100"]:
            for load in loads:
                for f in freq:
                    for t in to:
                        read_file("test-"+mode+"-simulation-"+seed+"-" + str(t)+"-"+str(f), mode) 
                        fcts[mode].sort()
                    # print(fcts)
                        print(f,t, load, sum(fcts[mode])/len(fcts[mode]), fcts[mode][int(0.999*len(fcts[mode]))])
                        fcts[mode] = []

    # for mode in modes:
    #     print(mode)
    #     print(sum(fcts[mode])/len(fcts[mode]), fcts[mode][int(0.999*len(fcts[mode]))])
    # plt.legend(loc='upper left' )
    # plt.tight_layout()
    # plt.savefig("fc2.png")
    
    