def parse_file(f):
    lines = f.readlines()
    i = 0
    times = [[],[],[],[],[]]
    times2 = [[],[],[],[],[]]
    ans = {}
    cur = 0
    for l in lines:
        if i % 3 == 0:
            cur = int(l.split(" ")[0])
            pass
        elif i % 3 == 1:
            nums = l.split(" ")
            for j,n in enumerate(nums):
                try:
                    nums[j] = int(n)
                except:
                    if n!="\n": nums[j] = int(n.split(':')[0])
                    else: del nums[j]
            # print(nums)
            for j in range(0, len(nums),2):
                if not cur in ans.keys():
                    ans[cur] = {}
                if not nums[j] in ans[cur].keys():
                    ans[cur][nums[j]] = []
                ans[cur][nums[j]].append(nums[j+1])
        else:
            pass
        i += 1
    for i,t in enumerate(times):
        for j in ans[10].keys():
            t.append(ans[10][j][i*2])
            times2[i].append(ans[10][j][i*2+1])
    print(times, ",",times2)

    # print(ans)    


if __name__ == "__main__":
    f = open("result")
    parse_file(f)
    


