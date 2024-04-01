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
modes = [ "letflow","ecmp", "drill", "clove" ]
bottoms_20 = {}
tops_20 = {}
mid_20 = {}
mid_40 = {}
mid_60 = {}
p99 = {}
# loads = [0.3,0.4,0.5,0.6,0.7, 0.8]
loads = [0.05]
workloads = ["ml", "datamining"]
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
            
            if  int(t1[1:-4]) == 200:
                fcts[mode].append(int(t2[1:-4]) - int(t1[1:-4]))
                # print(b, int(t2[1:-4]) - int(t1[1:-4]))
            
if __name__ == '__main__':
    
    for mode in modes:
        print(mode, ":")
        fcts[mode] = []
        for seed in ["7","8","9"]:
            for load in loads:
                if mode+str(load) not in bottoms_20.keys():
                    bottoms_20[mode+str(load)] = []
                    tops_20[mode+str(load)] = []
                    p99[mode+str(load)] = []
                    mid_20[mode+str(load)] = []
                    mid_40[mode+str(load)] = []
                    mid_60[mode+str(load)] = []
                
                
                read_xml("12-asydatamining-1-large-load-4X4-"+str(load)+"-DcTcp-"+mode+"-simulation-"+seed+"-capacity-asym2-b600.xml", mode) 
                fcts[mode].sort()
                print(sum(fcts[mode])/len(fcts[mode]))
                print(fcts[mode][int(0.999*len(fcts[mode]))])
                # print(fcts[mode][-1])
                # print(fcts[mode][-10:])
                # p99[mode+str(load)].append(fcts[mode][int(0.999*len(fcts[mode]))])
                # bottom_20 = int(0.2*len(fcts[mode]))
                # bottoms_20[mode+str(load)].append(sum(fcts[mode][-bottom_20:])/bottom_20)
                # tops_20[mode+str(load)].append(sum(fcts[mode][:bottom_20])/bottom_20)
                # mid_20[mode+str(load)].append(sum(fcts[mode][bottom_20:2*bottom_20])/bottom_20)
                # mid_40[mode+str(load)].append(sum(fcts[mode][2*bottom_20:3*bottom_20])/bottom_20)
                # mid_60[mode+str(load)].append(sum(fcts[mode][3*bottom_20:4*bottom_20])/bottom_20)
    # print(tops_20,"\n",mid_20,"\n",mid_40,"\n",mid_60,"\n",bottoms_20,"\n", p99)
    for mode in modes:
        print(mode)
        print(sum(fcts[mode])/len(fcts[mode]), fcts[mode][int(0.999*len(fcts[mode]))])
        # print()

    # x = [30,40,50,60,70,80]
    # x_major_locator=MultipleLocator(4)
    # # print(y3)
    # sns.set_style("whitegrid")
    # matplotlib.rcParams.update({'font.size': 20, "font.weight": "bold"}) 
    # plt.xticks(None, weight='bold')
    # plt.xlim((40, 80))
    
    # my_x_ticks = np.arange(40, 81, 10)
    # # my_y_ticks = np.arange(-2, 2, 0.3)
    # # plt.xticks(my_x_ticks,weight='bold')
    
    # # my_y_ticks = np.arange(10000000, 40000000, 10000000)
    # # plt.yticks(my_y_ticks)
    # shapes = ["ro-", "g*-", "k^-", "ys-", "bp-"]
    # for i, mode in enumerate(modes):
    #     plt.plot(x, tops_20[mode], shapes[i], label=mode, linewidth=2.5, markersize=8)
        
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
    # # plt.tight_layout()
    # # plt.show()
    # plt.savefig("fc2.png")
    


# drill = [.92857143, ]
# clove = [.97619048, ]

 
# drill
# .1388889 
# clove
# .75 

# drill
#  
# clove
# .8 


# drill
# .04166666 
# clove
# .20833334 



# lf50 = [167001954,167001054,178027929,190384398,203404967]
# lf99 = [168173731,170164598,230143406, 250013194,291500746 ]
# ecmp50 = [167001254,167148336, 167582610, 188814701,189889522]
# ecmp99 = [168289221,170475864,184031682,239120283, 252312591]
# drill50 = [167002054,167008950,167636912,167984441,178771013]
# drill99 = [168028292,170337175,184038171,185169539,257909278]
# clove50 = [167001054,167010243,179562295,191954457,210284656]
# clove99 = [168393983,170390337,229505857,250692432,353817866]
# Reunion50 = [167002054,167043836, 167982390, 170327742,171899292]
# Reunion99 = [168233932,170663998, 180727777,192938283,195833991]


