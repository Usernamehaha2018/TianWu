#             {'ecmp0.3': [36388995.818930045, 36557615.48917749, 47563539.54938272, 22109964.51002227], 'letflow0.3': [36475920.09670782, 41407396.872294374, 50010409.666666664, 24560907.975501113], 'drill0.4': [18496562.331699345, 41956727.115771815, 68701480.63664596, 36536262.704791345], 'letflow0.4': [19560348.97385621, 38980703.5385906, 54421134.44409938, 32238993.061823804], 'clove': [], 'drill': [], 'letflow': [], 'ecmp': [], 'drill0.3': [44907250.78395062, 29677679.954545453, 58547413.20164609, 20973851.082405344], 'clove0.4': [24179849.27124183, 42559391.944630876, 56739234.38043478, 33419407.035548687], 'clove0.3': [36163263.343621396, 32909446.456709955, 60605955.42386831, 27236937.815144766], 'ecmp0.4': [19981536.810457516, 45763302.66442953, 58525824.24068323, 37646083.08037094]} 
#  {'ecmp0.3': [83273.05349794238, 83832.75757575757, 86196.23045267489, 82596.26280623607], 'letflow0.3': [83776.13580246913, 82980.91991341992, 83417.5, 82374.71937639198], 'drill0.4': [82346.08823529411, 82974.05201342281, 83096.21739130435, 82676.56105100464], 'letflow0.4': [82742.7794117647, 86167.7701342282, 89477.43167701863, 84585.71097372488], 'clove': [], 'drill': [], 'letflow': [], 'ecmp': [], 'drill0.3': [82759.51234567902, 82845.53463203463, 82630.27777777778, 82254.49443207127], 'clove0.4': [82681.60620915033, 83982.5167785235, 89126.73447204969, 83853.03863987635], 'clove0.3': [83247.33539094651, 84389.21212121213, 83328.61728395062, 82451.58574610246], 'ecmp0.4': [82742.03594771241, 84755.4966442953, 87671.12577639752, 83347.8145285935]} 
#  {'ecmp0.3': [765159627, 1508305534, 903494999, 701576101], 'drill0.3': [983241327, 859055264, 1311768253, 651682907], 'drill0.4': [613606943, 1359964750, 1465404770, 1078481283], 'letflow0.4': [590060158, 1226015522, 1208545009, 956294097], 'clove0.4': [981452297, 1315024900, 1163285784, 926308661], 'letflow0.3': [763541790, 1691309462, 1176573351, 770025874], 'clove0.3': [771471445, 871427549, 1627777990, 872003502], 'ecmp0.4': [729433279, 1430509617, 1435252333, 901907081]}

# {'ecmp0.5': [37492388.48582474, 51242529.34149484, 39772149.1126071, 20681270.598214287], 'drill0.6': [33263492.502590675, 32615339.676130388, 41994374.12839249, 73437282.82266527], 'drill': [], 'letflow': [], 'ecmp0.6': [31075906.259067357, 31033295.108307045, 37471737.04592902, 58936988.64113326], 'letflow0.5': [33306570.534793813, 53392098.328608245, 38294192.0624235, 20724477.049744897], 'clove0.6': [30573686.60207254, 29610572.36382755, 40868060.306889355, 62111587.572927594], 'clove': [], 'drill0.5': [38195364.797680415, 47260176.206185564, 41837655.67074663, 21484339.13392857], 'letflow0.6': [28575849.402072538, 29375371.079915877, 36058853.798538625, 65857674.451206714], 'ecmp': [], 'clove0.5': [30656221.44201031, 50130839.541237116, 42496162.28641371, 20811243.089285713]} 
#  {'ecmp0.5': [82857.79896907216, 88246.55798969071, 90286.81150550795, 83162.96428571429], 'drill0.6': [82813.13989637306, 82832.73606729758, 82828.8350730689, 83262.94648478489], 'drill': [], 'letflow': [], 'ecmp0.6': [85497.05595854922, 85299.94006309149, 85760.24634655533, 94482.13536201468], 'letflow0.5': [82952.40206185567, 86126.57731958762, 87078.13953488372, 83447.10841836735], 'clove0.6': [86583.09119170984, 84950.73080967403, 84291.34133611691, 100813.6610703043], 'clove': [], 'drill0.5': [82436.45360824742, 82872.39304123711, 83140.35618115055, 82819.0612244898], 'letflow0.6': [85271.08911917098, 84296.7476340694, 86155.14822546973, 98185.3242392445], 'ecmp': [], 'clove0.5': [82994.25386597938, 87072.47551546391, 89626.85556915545, 83707.48979591837]} 
#  {'letflow0.5': [1034232605, 1663577141, 1120906027, 847017044], 'clove0.6': [935285658, 836677995, 1154187365, 1730899905], 'drill0.6': [974074927, 1060743973, 1006969597, 1947219902], 'ecmp0.5': [1208370880, 1355688998, 1059755498, 977188174], 'letflow0.6': [882250417, 872194937, 975833582, 1702954164], 'ecmp0.6': [892777114, 1093964198, 967173459, 1410452735], 'drill0.5': [1422979839, 1737791740, 1077025153, 788390275], 'clove0.5': [1050067702, 1739262750, 1099328703, 781218344]}
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
if __name__ == "__main__":
    modes = ["letflow", "ecmp","Reunion"] 

    lf50 = [121221954,132001054,150384398,163404967]
    lf99 = [158173731,180164598,250013194,331500746 ]
    ecmp50 = [121202254,137148336, 140582610, 157378722 ]
    ecmp99 = [180289221,204031682,239120283, 282312591]
    Reunion50 = [121202054,124023836, 130982390, 135899292]
    Reunion99 = [150233932,150663998, 161727777,165833991]
    ans = {"letflow": lf99,"ecmp":ecmp99,"Reunion":Reunion99}
    # ans = {"letflow": lf50,"ecmp":ecmp50,"Reunion":Reunion50}
    # ans = {"letflow": lf99, "drill":drill99,"ecmp":ecmp99,"clove":clove99,"Reunion":Reunion99}
    # ans["letflow"][2]*=0.95
    
    # for a in  [btms1, btms2 ]:
    for m in modes:
        for b in range(0,len(ans[m])):
            ans[m][b]=ans[m][b]/1000000
                        
                

    
    
    x = [5,6,7,8]
    x_major_locator=MultipleLocator(2)
    # print(y3)
    sns.set_style("whitegrid")
    matplotlib.rcParams.update({'font.size': 20, "font.weight": "bold"}) 
    plt.xticks(None, weight='bold')
    plt.xlim((5, 8))
    
    # my_x_ticks = np.arange(40, 81, 10)
    # my_y_ticks = np.arange(-2, 2, 0.3)
    # plt.xticks(my_x_ticks,weight='bold')
    
    y_major_locator=MultipleLocator(80)
    ax=plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)

    
    plt.ylim(0,400)
    
    # my_y_ticks = np.arange(-1500000000, 1500000000, 150000000)
    # plt.yticks(my_y_ticks)
    shapes = ["ro-",  "k^-",  "bp-"]
    for i, mode in enumerate(modes):
        plt.plot(x, ans[mode], shapes[i], label=mode, linewidth=2.5, markersize=8)
        
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
    

    plt.xlabel('Server pair', weight="bold")
    plt.ylabel('FCT (ms)', weight="bold")
    plt.legend(loc='upper left', fontsize="x-small" )
    plt.tight_layout()
    # plt.show()
    plt.savefig("rdma99.png")
    
    # tps = []
    # btms = []
    # p99s = []
    # for a in tops1.keys():
        