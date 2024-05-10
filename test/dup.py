import matplotlib.pyplot as plt
def parse_file(f):
    lines = f.readlines()
    maps = {}
    cnt = 0
    for l in lines:
        
        lis = l.split(" ")
        if len(lis) == 3:
            if lis[2] not in maps.keys():
                maps[lis[2]] = []
            try:
                if lis[1] != "0":
                    maps[lis[2]].append([int(lis[0]), int(lis[1])])
                    print(lis)
                    cnt += 1
            except:
                pass
        elif len(lis) == 2:
            print(lis)
    ans = []
    for i in maps.keys():
        ans = maps[i]
        break

    print(cnt)
    flow_sizes = [i[0] for i in ans]
    out_of_order_packets = [i[1] for i in ans]

    # 绘制散点图
    plt.figure(figsize=(8, 6))
    plt.scatter(flow_sizes, out_of_order_packets, color='blue', alpha=0.5)
    plt.title('Scatter Plot of Flow Sizes vs Out of Order Packets')
    plt.xlabel('Flow Size')
    plt.ylabel('Out of Order Packets')
    plt.grid(True)
    plt.show()
    # plt.savefig("dups.png")
            
    print(cnt)

    # print(ans)    


if __name__ == "__main__":
    f = open("dups")
    parse_file(f)
    


