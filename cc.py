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
fcts2 = {}


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
        fcts2[mode] = []
        for seed in ["100"]:
            for load in loads:
                read_file("test-"+mode+"-simulation-"+seed+"-", mode) 
                fcts[mode].sort()
                print(len(fcts[mode]))
                print(mode, load, sum(fcts[mode])/len(fcts[mode]))
                print(fcts[mode][int(0.9999*len(fcts[mode]))])
    # for mode in modes:
    #     print(mode)
    #     print(sum(fcts[mode])/len(fcts[mode]), fcts[mode][int(0.999*len(fcts[mode]))])
        # print()

    # write fcts data
    # f = open("fcts", "w")
    # f.write(str(fcts))
    # f.close()
    # exit(0)
    # x_nums = 10
    # y_modes = {}
    # xs = []
    # y_fcts = {}
    # sizes = [x[0] for x in fcts["ecmp"]]
    # for mode in modes:
    #     y_fcts[mode] = []
    #     y_modes[mode] = [x[1] for x in fcts[mode]]
    # l = int(len(sizes)/10)-1
    # for i in range(x_nums):            
    #     if i == 9:
    #         res = len(sizes)
    #     else:
    #         res = (i+1)*l
    #     cur = sizes[i*l:res]
    #     xs.append(int(sum(cur)/len(cur)))
    #     for mode in modes:
    #         cur_y = int(sum(y_modes[mode][i*l:res])/len(y_modes[mode][i*l:res]))
    #         y_fcts[mode].append(cur_y)

    



    # x_major_locator=MultipleLocator(4)
    # # print(y3)
    # sns.set_style("whitegrid")
    # matplotlib.rcParams.update({'font.size': 20, "font.weight": "bold"}) 
    # plt.xticks(None, weight='bold')
    # # plt.xlim((40, 80))
    
    # # my_x_ticks = np.arange(40, 81, 10)
    # shapes = ["ro-", "g*-", "k^-"]
    # for i, mode in enumerate(modes):
    #     plt.plot(xs, y_fcts[mode], shapes[i], label=mode, linewidth=2.5, markersize=8)

    # plt.legend(loc='upper left' )
    # plt.tight_layout()
    # # plt.tight_layout()
    # # plt.show()
    # plt.savefig("fc2.png")
    



