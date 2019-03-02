DIRS = [[1,0],[-1, 0], [0, 1],[0, -1], [1, 1], [1, -1], [-1, -1],[-1, 1]]
class Solution:
    def gridIllumination(self, N, lamps, queries):
        if N <= 0 or not queries:
            return []
        
        turnoff = []
        lamp_set = set()
        for lamp in lamps:
            lamp_set.add((lamp[0], lamp[1]))
        
        for q in queries:
            tmp = []
            for d in DIRS:
                if (q[0] + d[0], q[1] + d[1]) in lamp_set:
                    lamp_set.remove((q[0] + d[0], q[1] + d[1]))
                    tmp.append((q[0] + d[0], q[1] + d[1]))
                    
            turnoff.append(tmp)
            
        grid = [[0 for _ in range(N)] for _ in range(N)]
        cols = set()
        rows = set()
        diags = set()
        
        for i in lamp_set:
            cols.add(i[1])
            rows.add(i[0])
            diags.add(i[1] - i[0])
        
        # print(grid)
        # print(turnoff)
        # print(lamp_set)
        
        ans = []
        for index in range(len(queries) -1, -1, -1):
            for i in turnoff[index]:
                cols.add(i[1])
                rows.add(i[0])
                diags.add(i[1] - i[0])
            
            r = queries[index][0]
            c = queries[index][1]
            if r in rows or c in cols or c - r in diags:
                ans.append(1)
            else:
                ans.append(0)
                
        return ans[::-1]

        
                    
sl = Solution()
N = 10000
lamps =[[6781,8653],[2624,6531],[7485,1378],[3819,4964],[7741,343],[9960,5],[83,1173],[9533,9441],[1763,8712],[2082,6100],[4538,9471],[9093,9315],[3415,1120],[8646,7698],[7660,4705],[6683,9643],[3665,9248],[685,6302],[8082,4077],[9369,91],[9404,5771],[7233,9561],[3236,8674],[6280,3683],[4672,272],[9098,7894],[9051,7955],[6721,5461],[1525,4768],[2305,3189],[1425,1664],[7277,5281],[5270,94],[9135,1047],[1423,2026],[9364,2504],[1387,9993],[4382,9260],[1981,9858],[7104,6716],[4844,7154],[1974,1734],[5252,1305],[122,6845],[6148,6059],[7072,4871],[5503,9185],[2443,8877],[6763,4757],[1733,270],[7044,953],[2843,7884],[3418,7137],[3455,1437],[8334,1716],[1941,3179],[5258,2367],[3446,3109],[1750,4210],[6160,7724],[995,3633],[2915,5399],[6484,6788],[2869,1759],[7072,4567],[7647,5011],[6274,9931],[2319,6246],[1785,7459],[2916,7772],[9800,1224],[1349,3521],[6343,5734],[7690,3297],[4464,4156],[4481,4577],[5123,8000],[9307,5493],[434,3497],[156,2584],[3350,9427],[9518,8519],[6584,9086],[8670,3110],[5609,704],[8206,9545],[234,2094],[2546,5708],[1748,775],[6867,3292],[418,8985],[2143,8460],[9026,4618],[6422,8113],[776,7424],[4863,246],[9547,9529],[7281,3801],[1158,756],[3594,6972],[2104,8230],[6284,9381],[8005,663],[4891,7678],[5986,6802],[7632,5781],[252,1032],[6553,1117],[6802,2078],[7254,6108],[8183,6906],[4270,779],[7025,5290],[8568,3721],[5037,5117],[3762,936],[5608,7927],[1806,239],[311,7986],[2336,2070],[5936,3448],[2625,3869],[3151,3786],[8015,4709],[9602,3628],[9979,8901],[1230,4326],[7385,1126],[4807,8996],[8851,3992],[8683,4647],[2647,8763],[8057,7091],[6324,6119],[2194,6463],[6001,116],[7471,3912],[695,5827],[1466,2573],[8290,8915],[6643,964],[6323,2508],[6348,8692],[65,1256],[3502,9145],[7699,8757],[7314,1844],[3271,2660],[1193,632],[5871,6397],[4997,1054],[2783,2249],[6893,6290],[7360,102],[1517,627],[3728,1143],[8739,6919],[9280,5474],[4628,2357],[228,7040],[501,5529],[2103,816],[1410,3635],[2532,4676],[9930,1336],[4702,1074],[1792,4768],[8121,1924],[332,294],[2014,3097],[6920,8347],[9979,1698],[1124,1460],[6289,1525],[2915,7575],[5605,2174],[8012,6466],[1183,921],[7881,5492],[3485,3321],[315,5026],[6193,292],[5492,1956],[2111,7093],[9995,9861],[9793,7785],[12,9430],[4259,7394],[3270,8235],[9558,1799],[3531,460],[6737,322],[2659,7894],[4699,9552],[1449,3896],[8499,5173],[396,6550],[1769,198],[6528,4682],[6130,460],[5227,462],[1143,1800],[3752,8579],[6214,7897],[9623,4844],[6368,8903],[5291,6804],[4505,9788],[458,260],[3388,4934],[6833,4846],[2436,87],[1086,1797],[3092,7125],[2628,9746],[5904,2234],[4650,5985],[5250,9780],[9164,5137],[6726,4422],[5561,520],[4030,3670],[6003,3517],[9966,8589],[6498,636],[97,554],[7217,2598],[9522,6511],[5071,9806],[7012,3394],[2384,4573],[3595,3294],[5002,9070],[2241,5584],[7704,7891],[6674,7178],[5770,1054],[4864,4851],[1795,3449],[6943,116],[8634,639],[9930,8509],[154,7040],[5772,1086],[7602,9185],[3224,6686],[3749,9433],[6626,1384],[490,9302],[5188,5225],[6477,6470],[7722,6323],[7165,8446],[9894,5902],[3324,3383],[4493,8417],[3042,3611],[8999,6029],[9498,1661],[8915,1603],[7364,8270],[2657,2536],[5777,3673],[3078,8],[9146,5080],[5627,7425],[2298,4460],[5071,8675],[1503,9017],[9393,9495],[445,1479],[7958,837],[2699,3826],[3961,5356],[3779,7915],[1413,846],[6134,5782],[5597,1889],[9750,6650],[2470,8911],[1835,6724],[4823,9159],[6015,68],[3007,4122],[5426,5949],[1791,2750],[6726,2505],[3916,6447],[3971,9812],[863,1833],[245,2972],[1684,7871],[7673,8904],[318,5543],[6260,7149],[2162,3020],[2588,1706],[3255,2907],[988,2270],[9372,3622],[4213,2732],[9602,4788],[4200,2110],[1310,4719],[5964,7535],[8105,2500],[5198,8880],[2048,6247],[9740,7652],[8931,3532],[7897,8163],[7546,1375],[6605,2779],[8731,1869],[5570,458],[3478,2169],[4984,4294],[778,7288],[3073,1717],[7404,3605],[3526,3141],[5623,7086],[2016,6469],[8791,788],[6063,42],[1501,6271],[2327,4747],[2158,6952],[8366,6934],[6196,8766],[2048,537],[9419,8882],[2699,1465],[6069,90],[6531,2846],[1559,1665],[2879,5109],[8458,2757],[9002,7949],[2091,888],[3379,731],[9819,9121],[4253,758],[9807,5656],[1312,3355],[5105,7725],[8134,8266],[541,5857],[3423,2439],[3573,2907],[7965,9658],[1518,4452],[8489,559],[1425,27],[4476,4551],[1130,2435],[7415,8389],[5212,2528],[6667,8146],[7084,5134],[7378,6186],[8498,3450],[20,5565],[5515,758],[5667,2847],[3977,6921],[6928,6328],[9137,1581],[4963,4132],[5452,7456],[3767,6595],[1527,803],[1483,3482],[915,46],[1794,5649],[8517,3034],[4308,9060],[3527,1669],[6091,2994],[9653,2482],[2087,4577],[7489,3750],[7354,5719],[4320,332],[7101,3522],[5531,8162],[5449,9074],[2831,7322],[5615,8154],[1821,6090],[6865,3666],[3194,9916],[1878,7672],[3456,1615],[7354,8810],[9820,8548],[9291,2685],[1166,9665],[5229,5466],[9324,898],[7015,6267],[3647,9987],[4612,3779],[5444,5015],[7812,2419],[5580,6212],[2024,4262],[7708,4629],[7529,6246],[9742,3719],[1345,3956],[2574,572],[7296,5764],[7535,7323],[4569,4718],[6804,8445],[9074,5503],[5030,2626],[5800,4022],[7268,2570],[8520,87],[8239,1933],[4823,5979],[2282,3636],[6428,334],[5712,1325],[9392,8608],[3197,2394],[69,6421],[2116,1683],[1628,1621],[8392,2191],[4557,2476],[6947,7855],[8483,5211],[7858,8404],[8429,3125],[2278,3780],[4415,1443],[8132,4409],[1631,8065],[3446,1025],[5720,6030],[4041,3455],[6554,8496],[1053,2889],[2056,3502],[104,9720],[4216,4404],[1923,1595],[3607,450],[107,1444],[8131,9533],[3953,5001],[7999,1197],[6747,9860],[4498,9086],[769,6084],[184,2831],[9984,6442],[735,8677],[9626,4269],[3132,9705],[3541,2726],[9620,694],[4040,9332],[339,4012],[8689,9722],[4392,7520],[849,3020],[215,9738],[701,6102],[4230,229],[2927,8437],[5152,578],[2100,1291],[9621,4853],[2124,2991],[3960,5623],[5837,59],[2559,1426],[9248,9085],[9031,3224],[1794,9062],[2446,7485],[4981,5662],[7495,9944],[4780,5726],[6185,7062],[1138,1380],[8560,2631],[5092,4931],[6891,3631],[4882,8416],[5612,8966],[658,694],[219,3353],[9021,787],[3172,2423],[6257,3369],[2980,9236],[5677,9566],[783,8937],[2776,9980],[1917,850],[4058,833],[617,2159],[1552,8832],[273,3203],[3517,1183],[5305,2792],[5092,7799],[2760,7785],[8591,8919],[5384,6103],[4507,6209],[874,133],[41,396],[624,2028],[991,9392],[2658,2472],[8837,5917],[3802,1064],[9337,3044],[5383,7682],[219,7436],[7022,3740],[3841,4319],[9924,2068],[9300,5354],[6357,6890],[3138,6720],[8337,4385],[634,2952],[6281,9985],[8483,3579],[8774,3368],[5765,3143],[7331,4164],[7662,4750],[3054,7082],[1470,9351],[6843,387],[5099,7932],[5169,4010],[6638,5691],[6299,7519],[9381,38],[183,183],[2223,4947],[7803,6025],[6851,876],[5067,3842],[9241,1103],[9412,3986],[5055,2351],[9301,2109],[405,6305],[3216,3036],[5329,9696],[6926,8025],[4428,9866],[952,1974],[2724,9889],[959,7191],[3992,3275],[2244,6675],[815,6035],[16,6919],[4401,3365],[8926,6899],[5276,4517],[3404,3003],[5648,1545],[8846,5655],[9028,379],[5371,707],[1167,3576],[5710,7696],[8879,451],[6646,337],[1350,5554],[5382,6383],[8887,4528],[1846,4966],[46,2026],[2464,9477],[5333,9602],[1332,4930],[1616,463],[9284,7764],[162,8539],[4296,7591],[629,8804],[604,2043],[919,8459],[637,6310],[3895,8504],[2048,77],[6028,4756],[1051,5487],[590,2845],[7178,906],[5243,1110],[1979,5140],[2548,5732],[2178,9011],[1869,6098],[918,8517],[2608,702],[3938,4026],[4683,7977],[4965,7828],[3773,2779],[6850,9742],[621,3646],[3169,2434],[1763,7086],[3020,9153],[3821,287],[7427,7888],[7052,5063],[649,2613],[420,8495],[388,5406],[5199,4438],[1425,2058],[4699,2030],[6477,2221],[8567,477],[8493,7969],[4762,3262],[3399,432],[2780,1053],[3351,3835],[5547,7071],[9243,5430],[728,1159],[855,9305],[3735,8594]]
queries = [[930,7824],[1683,1180],[1207,76],[2087,3113],[6101,8065],[2438,6525],[7984,5702],[6964,9156],[5661,1016],[7498,8283],[4154,166],[6950,8261],[8276,3574],[5640,9831],[8302,6271],[8007,8268],[8289,9069],[9658,6081],[5238,5905],[288,5178],[8622,3550],[2584,4508],[9643,5997],[4825,3137],[5924,6938],[2188,1015],[501,3236],[1517,1681],[4924,1777],[6525,388],[6109,6984],[9523,3291],[9727,4373],[4454,3268],[8701,824],[7493,1089],[1863,9558],[3023,8776],[9662,1127],[5499,7891],[3899,9958],[3682,4497],[9368,6229],[6288,483],[4293,934],[3446,608],[1941,5986],[2283,2561],[1902,7062],[1446,5637],[3885,3937],[1206,7103],[576,7416],[42,771],[2442,7651],[6121,6461],[5906,7773],[1100,2985],[3188,8679],[3855,7500],[5438,1253],[7380,3930],[9605,9087],[5855,9837],[3054,5330],[4011,1541],[8853,5869],[5763,1491],[8281,7828],[7386,6460],[9085,753],[6532,8956],[6345,9982],[2586,3280],[7320,7052],[7402,1803],[5768,2799],[4965,8690],[348,1583],[6720,720],[2701,216],[9667,4659],[853,5627],[4797,4749],[6610,3195],[5437,7987],[9754,5441],[2059,5058],[1057,7945],[6445,6773],[2740,7938],[9250,2144],[9697,8578],[4043,4312],[4941,7168],[3597,7017],[6589,712],[8112,2751],[3165,6811],[3539,3021],[3580,4684],[1733,3097],[862,3668],[5070,941],[2905,398],[8052,2088],[8440,8300],[38,5643],[4059,1376],[4933,8701],[4773,6772],[4678,1912],[9037,2739],[1,4649],[7613,3725],[3125,9187],[1510,1527],[1026,1149],[7242,9912],[4205,6448],[3041,3902],[8239,698],[2005,1687],[5830,7357],[7493,1896],[4435,4240],[6694,1578],[6411,5741],[2413,2967],[1398,1378],[8278,9394],[2947,1632],[9937,604],[1682,8703],[7519,2032],[1800,5176],[3177,7864],[2031,6153],[5066,9653],[5219,933],[4848,6475],[6230,785],[6895,7218],[4444,424],[3453,4758],[192,5480],[4711,8264],[318,6739],[267,6316],[9591,2495],[668,2169],[64,6726],[2866,2636],[194,6215],[2471,1013],[8924,5139],[2314,2055],[9117,9985],[3248,9948],[9898,9626]]

print(sl.gridIllumination(N, lamps, queries))