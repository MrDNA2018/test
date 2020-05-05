# d[k][i][j] = min(d[k-1][i][j], d[k-1][i][k]+d[k-1][k][j])（k,i,j∈[1,n]）
#
# 初始条件：d[0][i][j]=w(i, j)，d[k][0][j]=0,d[k][i][0]=0

# d[k][i][j] = min(d[k-1][i][j], d[k-1][i][k]+d[k-1][k][j])（k,i,j∈[1,n]）

# d[k][i][j]定义：“只能使用第1号到第k号点作为中间媒介时，点i到点j之间的最短路径长度。”
# 在动态规划算法中，处于首要位置、且也是核心理念之一的就是状态的定义
# 这个大家喜欢把它叫做“松弛操作”，也就是relax
import numpy as np


def floyd_original(graph):
    vertex_num = len(graph)

    list = np.full((vertex_num + 1, vertex_num + 1, vertex_num + 1), np.inf)
    list[:, 0, :] = 0
    list[:, :, 0] = 0

    for i in range(1, vertex_num + 1):
        for j in range(1, vertex_num + 1):
            list[0, i, j] = graph[i - 1, j - 1]

    for k in range(1, vertex_num + 1):
        for i in range(1, vertex_num + 1):
            for j in range(1, vertex_num + 1):
                list[k, i, j] = min(list[k - 1, i, j], list[k - 1, i, k] + list[k - 1, k, j])

    return list[vertex_num, 1:, 1:]
#%%
import numpy as np


def floyd(graph):
    vertex_num = len(graph)
    list = np.zeros((vertex_num + 1, vertex_num + 1))

    for i in range(1, vertex_num + 1):
        for j in range(1, vertex_num + 1):
            list[i, j] = graph[i - 1, j - 1]

    for k in range(1, vertex_num + 1):
        for i in range(1, vertex_num + 1):
            for j in range(1, vertex_num + 1):
                list[i, j] = min(list[i, j], list[i, k] + list[k, j])

    return list[1:, 1:]
graph = np.full((7,7),np.inf)
graph[0,:3] = [0,1,2]
graph[1,:4] = [1,0,3,4]
graph[2,:4] = [2,3,0,6]
graph[3,1:5] = [4,6,0,7]
graph[4,3:6] = [7,0,9]
graph[5,4:7] = [9,0,10]
graph[6,5:7] = [10,0]
