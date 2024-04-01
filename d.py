import random
if __name__ == "__main__":
    a = 8
    bucket = [0,0]
    bk_size = 4
    rate = []
    for i in range(100):
        bucket = [0,0]
        j = 0
        for k in range(a):
            chosen = 0
            if random.random()>=0.5:
                chosen = 1
            bucket[chosen] += 1
        # while j < 3 and (bucket[0] > 4 or bucket[1] > 4):
        #     j += 1
        #     if bucket[0] > 4:
        #         in_bk0 = 0
        #         for k in range(bucket[0]):
        #             if random.random() < 0.5:
        #                 in_bk0 += 1
        #         in_bk1 = bucket[0] - in_bk0
        #         bucket[0] = in_bk0
        #         bucket[1] += in_bk1
        #     else:
        #         in_bk0 = 0
        #         for k in range(bucket[1]):
        #             if random.random()%2 < 0.5:
        #                 in_bk0 += 1
        #         in_bk1 = bucket[1] - in_bk0
        #         bucket[0] += in_bk0
        #         bucket[1] = in_bk1
                        
        
        for m in bucket:
            if m < 4:
                for k in range(m):
                    rate.append(1)
            else:
                for k in range(m):
                    rate.append(4/m)
        # print(rate)
    rate.sort()
    print(len(rate))
    print(sum(rate)/len(rate))
    print(rate[int(0.001*(len(rate)))])
    
    
# 0.9287499999999997
# 0.5
# 0.9842857142857143
# 0.5714285714285714



# 800
# 0.8600000000000033
# 0.5
# 700
# 0.9242857142857146
# 0.5714285714285714
# 600
# 0.9666666666666665
# 0.6666666666666666
# 500
# 0.992
# 0.8