def parse_file(f):
    lines = f.readlines()
    i = 0
    times = [[],[],[],[],[]]
    times2 = [[],[],[],[],[]]
    ans = {}
    cur = 0
    for l in lines:
        if i % 3 == 0:
            nums = l.split(" ")
            nums = list(filter(lambda x: x!="", nums))
            cur = int(nums[0])
            del nums[0]
            del nums[0]
            for j,n in enumerate(nums):
                
                try:
                    # print(n, len(n))
                    temp = float(n)
                    # print(temp)
                    nums[j] = temp
                except:
                    if len(n) and n!="\n": nums[j] = int(n.split(':')[0])
                    else: del nums[j]
            print(nums)
            for j in range(0, len(nums),2):
                if not cur in ans.keys():
                    ans[cur] = {}
                if not nums[j] in ans[cur].keys():
                    ans[cur][nums[j]] = []
                ans[cur][nums[j]].append(nums[j+1])            
        elif i % 3 == 1:
            pass
        else:
            pass
        i += 1
    for i,t in enumerate(times):
        for j in ans[8].keys():
            t.append(ans[8][j][i*2])
            times2[i].append(ans[8][j][i*2+1])
    print(times, ",",times2)

    # print(ans)    


if __name__ == "__main__":
    f = open("result")
    parse_file(f)
    


