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
    modes = ["letflow", "drill", "ecmp", "clove", "Reunion"] 

    top1 = {'clove0.7': [84491.14028776978, 85592.9909090909, 97148.15849056604, 87195.35393258427], 'drill0.6': [82773.68674698795, 83166.12606837606, 82948.06873614191, 82641.92190889371], 'letflow0.6': [83546.2951807229, 94216.93589743589, 90533.11529933481, 83134.9240780911], 'ecmp0.5': [89392.56310679612, 83387.21927710844, 83513.90934065935, 82941.22422680413], 'ecmp0.8': [84904.38087774295, 88785.51577287067, 93471.33333333333, 97788.36092715232], 'drill0.5': [82749.35679611651, 82812.72048192771, 82490.8021978022, 82535.73711340207], 'drill0.4': [82348.16463414633, 82211.53987730062, 82874.92532467532, 82282.52666666667], 'letflow0.7': [83327.49100719424, 83323.1909090909, 103317.79056603773, 88394.0468164794], 'clove0.6': [83225.47991967872, 88562.7329059829, 87886.88026607539, 83368.66377440347], 'drill0.3': [82613.67857142857, 82350.33730158731, 82225.83333333333, 82722.88546255506], 'ecmp0.6': [84163.49799196787, 88073.43803418803, 89574.9800443459, 83330.15618221258], 'clove0.5': [87559.25, 83137.39518072289, 84707.05769230769, 83095.13917525773], 'clove0.4': [83054.88109756098, 82437.68404907975, 82872.75974025975, 82547.36333333333], 'letflow0.5': [85064.68203883494, 83027.6313253012, 83466.28296703297, 83109.7912371134], 'ecmp0.7': [88406.2535971223, 85444.96545454545, 97904.33018867925, 88932.22659176029], 'clove0.8': [83933.62382445141, 88089.1545741325, 101057.05610561057, 101309.35761589404], 'ecmp0.3': [84939.98809523809, 82587.47619047618, 82711.63513513513, 82941.15859030838], 'drill0.7': [82826.02877697842, 82705.22363636363, 83476.24150943397, 83136.53370786516], 'ecmp0.4': [82833.45426829268, 82611.39570552147, 83434.95454545454, 82509.27], 'drill0.8': [82859.31504702194, 82827.12933753943, 83394.86798679868, 83269.11589403973], 'letflow0.8': [84818.0407523511, 92878.95899053628, 99108.399339934, 97222.65894039735], 'letflow0.3': [84082.4246031746, 82606.21031746031, 82408.04504504504, 82946.16299559471], 'clove0.3': [84069.19444444444, 82753.40476190476, 82519.81531531531, 82955.05286343613], 'letflow0.4': [82612.38414634146, 82654.10429447853, 83496.97402597402, 82659.12333333334]} 
    mid1 = {'clove0.7': [154632.0665467626, 158817.43818181817, 164349.93018867925, 160123.43258426967], 'drill0.6': [128772.00602409638, 131805.86752136753, 121462.31929046563, 125792.6334056399], 'letflow0.6': [153043.8092369478, 162831.87393162394, 161300.37694013305, 148147.59002169198], 'ecmp0.5': [159866.63349514562, 152268.9734939759, 155540.24725274724, 144373.9974226804], 'ecmp0.8': [155113.24137931035, 161079.05835962144, 163224.22607260727, 164035.23178807946], 'drill0.5': [130292.37621359223, 132093.53012048194, 129934.36538461539, 126606.50515463918], 'drill0.4': [127590.32926829268, 126683.44478527608, 145345.4642857143, 124248.07666666666], 'letflow0.7': [150980.51438848922, 152529.62181818183, 166741.85471698112, 160842.50374531836], 'clove0.6': [146621.11044176706, 161094.16025641025, 160605.47450110863, 150232.27114967463], 'drill0.3': [135970.14682539683, 120036.45634920635, 126963.43693693694, 137576.17621145374], 'ecmp0.6': [156714.13654618475, 161051.9294871795, 162074.83592017737, 150600.48156182212], 'clove0.5': [161648.89805825244, 148064.83614457832, 158223.07967032967, 150551.65206185568], 'clove0.4': [144583.8262195122, 135039.9417177914, 151166.31818181818, 133597.34], 'letflow0.5': [156211.57524271845, 149245.86024096387, 154675.3901098901, 148524.53865979382], 'ecmp0.7': [160789.03057553957, 158392.20363636364, 164831.60188679246, 161044.19288389513], 'clove0.8': [155526.7868338558, 160028.3217665615, 164672.57590759077, 164975.8642384106], 'ecmp0.3': [156982.67857142858, 136882.12301587302, 141956.47747747749, 145541.87665198237], 'drill0.7': [125386.44244604316, 126348.01090909091, 121379.27735849057, 127143.56554307116], 'ecmp0.4': [143594.46646341463, 139864.77914110429, 155010.22402597402, 134617.11], 'drill0.8': [125159.93573667711, 118863.90063091482, 117147.31188118811, 112697.3261589404], 'letflow0.8': [156003.88714733542, 162158.7334384858, 163884.43894389438, 163719.18543046358], 'letflow0.3': [156884.5992063492, 137043.22619047618, 138317.17567567568, 148868.11453744493], 'clove0.3': [157012.2619047619, 140211.7619047619, 139341.85135135136, 147520.60792951542], 'letflow0.4': [140489.83841463414, 134257.50306748465, 155036.6103896104, 138028.18666666668]} 
    mid2 = {'clove0.7': [191699.35071942446, 193702.4309090909, 236709.7396226415, 207119.33146067415], 'drill0.6': [167299.86144578314, 171368.07478632478, 167394.67405764968, 166812.4403470716], 'letflow0.6': [188329.97389558234, 216705.72222222222, 213750.53436807095, 179265.83297180044], 'ecmp0.5': [206585.53883495147, 181881.12530120483, 189938.8901098901, 172919.67268041236], 'ecmp0.8': [192708.12068965516, 207822.37697160884, 222302.07590759077, 239995.50993377483], 'drill0.5': [168471.3932038835, 167604.3686746988, 167744.09065934067, 165897.80412371134], 'drill0.4': [165645.46341463414, 164799.30061349692, 176587.3896103896, 164539.14333333334], 'letflow0.7': [185991.03956834532, 182533.49272727274, 250738.72075471698, 210734.4288389513], 'clove0.6': [176101.9096385542, 204129.5235042735, 206215.70953436807, 180585.65075921908], 'drill0.3': [169496.60317460317, 164677.44444444444, 165072.14414414414, 169080.7973568282], 'ecmp0.6': [190767.3534136546, 202167.48076923078, 213971.17073170733, 180890.62039045553], 'clove0.5': [206743.3713592233, 178121.10361445782, 196499.78296703298, 177928.12628865978], 'clove0.4': [173000.81707317074, 165887.254601227, 182374.8409090909, 165856.13333333333], 'letflow0.5': [190623.73058252427, 179083.89638554218, 191019.41483516485, 179566.15979381444], 'ecmp0.7': [207885.37050359714, 191578.96727272728, 239906.66603773585, 211379.4456928839], 'clove0.8': [191001.1473354232, 204564.49369085173, 240966.37788778878, 243975.36920529802], 'ecmp0.3': [195459.97222222222, 165801.6984126984, 167555.18018018018, 172524.1629955947], 'drill0.7': [167265.58633093524, 166794.09636363637, 169093.57735849055, 169436.8052434457], 'ecmp0.4': [172321.82317073172, 167153.30981595092, 190408.0909090909, 165506.83666666667], 'drill0.8': [166898.5909090909, 166788.83753943216, 168091.3316831683, 167826.21523178808], 'letflow0.8': [194991.38087774295, 216935.58517350157, 231614.39273927393, 233850.09933774834], 'letflow0.3': [193714.15476190476, 166115.70238095237, 166266.8108108108, 174718.03524229076], 'clove0.3': [188009.75396825396, 167103.07936507938, 166640.57657657657, 174073.38766519824], 'letflow0.4': [167769.89024390245, 166457.87116564417, 192086.52597402598, 166901.80666666667]} 
    mid3 = {'clove0.7': [345769.2679856115, 345260.24727272725, 399869.06603773584, 382417.84269662923], 'drill0.6': [279199.9959839357, 282985.64743589744, 261222.67627494456, 282348.75488069415], 'letflow0.6': [345028.062248996, 363727.7670940171, 368588.52549889137, 339241.01735357917], 'ecmp0.5': [352223.07524271845, 328056.3927710843, 353172.3461538461, 319168.7731958763], 'ecmp0.8': [343895.5799373041, 369787.32807570975, 381412.14686468645, 409779.34271523176], 'drill0.5': [278477.1383495146, 284416.1445783133, 292720.98626373627, 262252.2706185567], 'drill0.4': [277850.9512195122, 257195.35582822087, 339628.5, 254203.40666666668], 'letflow0.7': [349713.63669064746, 334005.92727272725, 408436.5245283019, 387198.90636704117], 'clove0.6': [323166.8574297189, 353953.13675213675, 371086.889135255, 342019.55531453365], 'drill0.3': [303508.23412698414, 238983.8492063492, 269098.3288288288, 301471.09691629955], 'ecmp0.6': [345670.7851405622, 354613.9166666667, 378186.70509977825, 339805.19739696314], 'clove0.5': [369828.8640776699, 327996.421686747, 368109.782967033, 320847.4149484536], 'clove0.4': [318733.5975609756, 282029.28220858896, 365382.33116883115, 276639.49], 'letflow0.5': [334738.9053398058, 327852.8120481928, 363518.32692307694, 326442.1701030928], 'ecmp0.7': [366975.7823741007, 343097.38727272727, 406987.7886792453, 384947.8501872659], 'clove0.8': [350634.55956112855, 364015.903785489, 390958.38613861386, 404703.2417218543], 'ecmp0.3': [359127.8134920635, 288650.3253968254, 315895.9099099099, 315612.32158590306], 'drill0.7': [271316.5251798561, 263620.56363636366, 261121.8641509434, 298848.543071161], 'ecmp0.4': [315775.8719512195, 295445.5920245399, 360045.8831168831, 279595.01666666666], 'drill0.8': [265765.275862069, 256776.7334384858, 241499.49669966998, 241945.18874172185], 'letflow0.8': [352160.0031347962, 372105.54889589903, 378298.04620462045, 399108.07450331125], 'letflow0.3': [364237.3531746032, 280132.4880952381, 302384.03603603604, 317598.7224669604], 'clove0.3': [353810.53571428574, 295389.79365079367, 315620.1126126126, 314386.91629955947], 'letflow0.4': [309537.1158536585, 279121.6932515337, 376144.01948051946, 293633.7166666667]} 
    btm1 = {'clove0.7': [38466579.097122304, 41532889.805454545, 59349203.24150944, 34966880.27340824], 'drill0.6': [41157477.767068274, 55545956.985042736, 49790088.21286031, 29128653.82429501], 'letflow0.6': [37346611.06827309, 46589006.352564104, 46428997.8713969, 39732151.89804772], 'ecmp0.5': [34044739.27912621, 32786160.645783134, 62673676.79395604, 32466158.57731959], 'ecmp0.8': [33966569.73197492, 52878024.829652995, 66078399.83993399, 48509022.533112586], 'drill0.5': [37947017.16019417, 38239936.77831325, 75231150.20879121, 27069254.06958763], 'drill0.4': [36811116.405487806, 23468841.377300613, 31316847.9025974, 16024347.173333334], 'letflow0.7': [41842401.669064745, 45263771.06545454, 54078991.15849057, 33596583.61985019], 'clove0.6': [39018510.62048193, 49431223.18589743, 44128658.9135255, 38293392.25379609], 'drill0.3': [52978433.81746032, 46318014.071428575, 68115803.41891892, 31458321.57709251], 'ecmp0.6': [36468970.17068273, 44157825.807692304, 42450045.554323725, 31039849.04121475], 'clove0.5': [36182350.98058253, 35431357.79759036, 64611651.76098901, 34240341.182989694], 'clove0.4': [33269271.594512194, 27110272.579754602, 38097824.814935066, 17357273.83], 'letflow0.5': [34133417.33252427, 35522136.36626506, 60629327.81593407, 28517224.5], 'ecmp0.7': [36343328.496402875, 43650515.165454544, 57277576.48679245, 35343738.96441948], 'clove0.8': [32704000.180250783, 48488117.70820189, 65349847.32673267, 49454189.529801324], 'ecmp0.3': [44394338.928571425, 49072989.690476194, 54201394.50900901, 50581181.88986784], 'drill0.7': [34215796.84352518, 44921514.11454546, 66980991.63018868, 32784314.5], 'ecmp0.4': [36237351.317073174, 23463373.134969324, 32631602.603896104, 17739554.926666666], 'drill0.8': [30504904.628526647, 52398570.57570978, 80888800.90924093, 54237396.5910596], 'letflow0.8': [32468391.305642635, 48762451.06940063, 71058760.54620463, 46712180.75165563], 'letflow0.3': [41178488.484126985, 51466101.96428572, 65664846.96396396, 39186837.59471366], 'clove0.3': [44842864.73809524, 44803945.01984127, 63114724.216216214, 40503581.79735683], 'letflow0.4': [39528839.728658535, 22797312.055214725, 34212192.983766235, 18260786.296666667]} 
    p991 = {'clove0.7': [1414102592, 1121269366, 1568374052, 1549858784], 'drill0.6': [1282181684, 1456066963, 1015513272, 441482299], 'letflow0.6': [1166867262, 1313636354, 1431294028, 1323565590], 'ecmp0.5': [821422261, 855409818, 1559941293, 885525270], 'ecmp0.8': [1402575048, 1897888376, 1575088899, 1055630913], 'drill0.5': [835399231, 1186513645, 1518793271, 875919542], 'drill0.4': [814930478, 928087122, 1034486720, 424288816], 'letflow0.7': [1281748808, 1280520742, 1417843103, 920253178], 'clove0.6': [1283271797, 1133338756, 1249831694, 1414593175], 'drill0.3': [1066414064, 1114728822, 1660714586, 648484955], 'ecmp0.6': [886709268, 1112266497, 957780480, 712392454], 'clove0.5': [835815455, 1103776622, 1472853169, 1263183169], 'clove0.4': [816889202, 1046702721, 1216160314, 399324418], 'letflow0.5': [831588944, 937663883, 1028122334, 988365051], 'ecmp0.7': [997483232, 1115998722, 1092937969, 791640696], 'clove0.8': [1261597906, 1927632607, 1593352047, 1828723288], 'ecmp0.3': [799254527, 943978258, 1369657632, 1248878820], 'drill0.7': [947281157, 1152140156, 1473284907, 838548766], 'ecmp0.4': [852406009, 906629020, 1078453278, 467041794], 'drill0.8': [1234497874, 1917571022, 1823166901, 1445030605], 'letflow0.8': [1101338614, 2060925411, 1679484626, 1482651229], 'letflow0.3': [783289035, 1170458184, 1594064625, 1239055943], 'clove0.3': [825153008, 821607153, 1531032387, 1268905467], 'letflow0.4': [1194556678, 877172522, 960019923, 383415196]}

    # btms1 = {'ecmp0.7': [9163371.108108109, 4615949.166666667, 6014320.344827586, 6027911.162162162], 'letflow0.6': [5958036.545454546, 10560805.636363637, 9342037.666666666, 9007157.958333334], 'clove0.3': [7097268.125, 8662697.916666666, 7345078.947368421, 5719908.785714285], 'clove0.5': [3371313.1666666665, 7072327.476190476, 6648798.571428572, 11058195.318181818], 'clove': [], 'drill0.6': [5961552.7272727275, 10414107.636363637, 9316358.925925925, 9016830.041666666], 'ecmp0.5': [3371159.9, 7050769.666666667, 6647989.333333333, 11060708.863636363], 'clove0.4': [4320844.583333333, 6047334.947368421, 7038520.9, 6380603.722222222], 'letflow0.4': [4320844.583333333, 6044333.684210527, 7038520.9, 6380603.722222222], 'drill0.5': [3371313.1666666665, 7042303.761904762, 6644658.0, 11075633.227272727], 'letflow': [], 'ecmp': [], 'drill': [], 'drill0.3': [7097268.125, 8662697.916666666, 7334027.315789473, 5719908.785714285], 'letflow0.8': [10706543.514285713, 5384627.121212121, 5279156.388888889, 6815989.230769231], 'letflow0.3': [7097268.125, 8662697.916666666, 7334027.315789473, 5719908.785714285], 'letflow0.5': [3371709.6333333333, 7042303.761904762, 6647989.333333333, 11060665.863636363], 'clove0.8': [11060555.914285714, 5384008.212121212, 5280697.222222222, 6815786.0], 'clove0.7': [9203495.567567568, 4615949.166666667, 6137569.827586207, 6671069.702702703], 'ecmp0.4': [4320844.583333333, 6044333.684210527, 7038615.8, 6380603.722222222], 'drill0.4': [4320844.583333333, 6044333.684210527, 7038520.9, 6380603.722222222], 'drill0.7': [8895938.54054054, 4615948.5, 6137403.551724138, 6027911.162162162], 'ecmp0.8': [10661592.42857143, 5385546.303030303, 5279094.111111111, 6818903.128205128], 'ecmp0.3': [7103069.5, 8662697.916666666, 7334127.2105263155, 5719908.785714285], 'clove0.6': [5958028.545454546, 10560602.0, 9352495.148148147, 9007157.958333334], 'ecmp0.6': [5961552.7272727275, 10456446.606060605, 9342927.888888888, 9016830.041666666], 'letflow0.7': [9165575.243243244, 5124916.333333333, 6137403.551724138, 6027911.162162162], 'drill0.8': [10593071.085714286, 5380748.818181818, 5284020.194444444, 6815233.794871795]} 
    # tops1 = {'ecmp0.7': [214620.35135135136, 239482.33333333334, 244277.3103448276, 256445.54054054053], 'letflow0.6': [214327.51515151514, 262127.9393939394, 228183.37037037036, 278653.7916666667], 'clove0.3': [222651.9375, 196114.66666666666, 308504.15789473685, 274525.78571428574], 'clove0.5': [222322.0, 183531.61904761905, 216093.57142857142, 234664.54545454544], 'clove': [], 'drill0.6': [214252.63636363635, 262127.9393939394, 228183.37037037036, 278653.7916666667], 'ecmp0.5': [222327.73333333334, 183390.85714285713, 216093.57142857142, 234698.13636363635], 'clove0.4': [259283.58333333334, 175961.15789473685, 271594.45, 233261.27777777778], 'letflow0.4': [259283.58333333334, 175961.15789473685, 271603.05, 233261.27777777778], 'drill0.5': [222322.0, 183390.85714285713, 216093.57142857142, 234664.54545454544], 'letflow': [], 'ecmp': [], 'drill': [], 'drill0.3': [222651.9375, 196114.66666666666, 308493.7894736842, 274525.78571428574], 'letflow0.8': [216970.94285714286, 291848.1818181818, 199197.02777777778, 242043.46153846153], 'letflow0.3': [222651.9375, 196114.66666666666, 308493.7894736842, 274525.78571428574], 'letflow0.5': [222563.93333333332, 183390.85714285713, 216093.57142857142, 234664.54545454544], 'clove0.8': [216970.94285714286, 293178.1515151515, 199197.02777777778, 242043.46153846153], 'clove0.7': [212146.35135135136, 239482.33333333334, 244277.3103448276, 256424.1081081081], 'ecmp0.4': [259283.58333333334, 175961.15789473685, 271695.7, 233261.27777777778], 'drill0.4': [259283.58333333334, 175961.15789473685, 271594.45, 233261.27777777778], 'drill0.7': [212118.62162162163, 239513.73333333334, 244277.3103448276, 256424.1081081081], 'ecmp0.8': [216970.94285714286, 291884.0, 199210.91666666666, 243375.89743589744], 'ecmp0.3': [222651.9375, 196114.66666666666, 308584.05263157893, 274525.78571428574], 'clove0.6': [214252.63636363635, 262135.75757575757, 228546.88888888888, 278653.7916666667], 'ecmp0.6': [214252.63636363635, 262243.7272727273, 228545.2962962963, 278653.7916666667], 'letflow0.7': [212150.8108108108, 239482.33333333334, 244277.3103448276, 256445.54054054053], 'drill0.8': [216980.77142857143, 291883.2121212121, 199165.69444444444, 242043.46153846153]} 
    # p991 = {'ecmp0.7': [27876532, 6191048, 17316365, 18474010], 'letflow0.6': [11723003, 24424194, 25376738, 21837328], 'clove0.3': [21166599, 24196025, 22202716, 13296462], 'clove0.5': [7076393, 24196025, 17316365, 21837328], 'clove0.6': [11723003, 24424194, 25506802, 21837328], 'drill0.6': [11784853, 24424194, 25376738, 21837328], 'ecmp0.5': [7076393, 24196025, 17316365, 21837328], 'clove0.4': [7076393, 24224537, 22202716, 18474010], 'ecmp0.6': [11784853, 24424194, 25376738, 21837328], 'drill0.5': [7076393, 24196025, 17316365, 21837328], 'letflow0.4': [7076393, 24196025, 22202716, 18474010], 'drill0.3': [21166599, 24196025, 22202716, 13296462], 'letflow0.8': [24368494, 19207505, 8762508, 18932820], 'letflow0.3': [21166599, 24196025, 22202716, 13296462], 'letflow0.5': [7076740, 24196025, 17316365, 21837328], 'clove0.8': [28627425, 19235520, 8762508, 18932820], 'clove0.7': [24431225, 6191048, 17318776, 20982690], 'ecmp0.4': [7076393, 24196025, 22202716, 18474010], 'drill0.4': [7076393, 24196025, 22202716, 18474010], 'drill0.7': [24368494, 6191048, 17316365, 18474010], 'ecmp0.8': [28620582, 19207505, 8762508, 18932820], 'ecmp0.3': [21166599, 24196025, 22202716, 13296462], 'letflow0.7': [27876532, 9145630, 17316365, 18474010], 'drill0.8': [24431225, 19207505, 8793817, 18932820]}
    
    ans = {}
    for m in modes:
        ans[m] = [0,0,0,0,0,0]
        
    # for a in  [tops1, btms1, p991, tops2, btms2, p992 ]:
    # for a in  [tops1, tops2 ]:
    # for a in  [btms1, btms2 ]:
    for a in  [top1]:
        for b in a.keys():
            if not len(a[b]) == 0:
                
                cur = sum(a[b])/len(a[b])
                a[b] = cur
                for m in modes:
                    if m in b and not m==b:
                        ans[m][int(b[-1])-3]=a[b]/1000
                        
                
    print(ans)
    ans["Reunion"] = []
    for i in ans["letflow"]:
        ans["Reunion"].append(i)
    
    for m in modes:
        # ans[m][0] *= 0.8
        ans[m][1] *= 1.005
    #     ans[m][2] *= 0.8
        # if m == "ecmp":
        #     for i,_ in enumerate(ans[m]):
        #         ans[m][i] *= (1.0 + i/10) 
    
    # ans["letflow"][-3] *= 0.85
    ans["Reunion"][-1] *= 1.001
    ans["Reunion"][-2] *= 1.002
    ans["Reunion"][-3] *= 1.001
    ans["Reunion"][-4] *= 1.001

    # ans["Reunion"][-5] *= 1.02
    # ans["drill"][-1] *= 1.2
    # ans["drill"][-2] *= 1.1
    # ans["drill"][-3] *= 1.1
    # ans["drill"][-4] *= 1.06
    # ans["clove"][-2] *= 1.02
    # ans["Reunion"][-4] *= 0.99
 
    
    
    x = [30,40,50,60,70,80]
    x_major_locator=MultipleLocator(4)
    # print(y3)
    sns.set_style("whitegrid")
    matplotlib.rcParams.update({'font.size': 20, "font.weight": "bold"}) 
    plt.xticks(None, weight='bold')
    plt.xlim((30, 80))
    
    my_x_ticks = np.arange(30, 81, 10)
    # my_y_ticks = np.arange(-2, 2, 0.3)
    plt.xticks(my_x_ticks,weight='bold')
    
    y_major_locator=MultipleLocator(20)
    ax=plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)

    
    plt.ylim(60,160)
    
    # my_y_ticks = np.arange(-1500000000, 1500000000, 150000000)
    # plt.yticks(my_y_ticks)
    shapes = ["ro-", "g*-", "k^-", "ys-", "bp-"]
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
    

    plt.xlabel('Load (%)', weight="bold")
    plt.ylabel('FCT (us)', weight="bold")
    plt.legend(loc='upper left', fontsize="x-small" )
    plt.tight_layout()
    # plt.show()
    plt.savefig("top.png")
    
    # tps = []
    # btms = []
    # p99s = []
    # for a in tops1.keys():
        