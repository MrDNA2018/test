# 题目：
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
#
# 实现起来比较简单，状态方程：
# LCS F[i,v] = (max{F[i-1,v],F[i,v-1]},F[i-1,v-1] +1)[X[i] == Y[v]]
import numpy as np


def LCS(X, Y, N, V):
    #    L = [[None]*(n+1) for i in xrange(m+1)]
    list = np.zeros((N + 1, V + 1), dtype=int)
    list[1:, 1:] = -1
    G = np.full((N + 1, V + 1), '0')

    for i in range(1, N + 1):
        for v in range(1, V + 1):
            if X[i - 1] == Y[v - 1]:
                list[i][v] = list[i - 1, v - 1] + 1
                G[i][v] = '7'
            else:
                if list[i - 1, v] > list[i, v - 1]:
                    list[i][v] = list[i - 1, v]
                    G[i][v] = '^'
                else:
                    list[i][v] = list[i, v - 1]
                    G[i][v] = '<'
    return list, G

#%%
# 使用递归的方式
def print_LCS_Rec(X, Y, G, N, V):
    if N == 0 or V == 0:
        return
    elif G[N, V] == '7':
        print_LCS_Rec(X, Y, G, N - 1, V - 1)
        print
        X[N - 1],
    elif G[N, V] == '^':
        print_LCS_Rec(X, Y, G, N, V - 1)
    else:
        print_LCS_Rec(X, Y, G, N - 1, V)
    return
    # 使用非递归方式


def print_LCS_(X, Y, G, N, V):
    i = N
    v = V
    result = []

    while i > 0 and v > 0:
        if G[i, v] == '7':
            result += X[i - 1]
            i -= 1
            v -= 1

        elif G[i, v] == '^':
            i -= 1
        else:
            v -= 1
    return result[::-1]
    # 直接使用DP表来追踪也可以实现


def print_LCS(X, Y, list, N, V):
    i = N
    v = V
    result = []

    while i > 0 and v > 0:
        if X[i - 1] == Y[v - 1]:
            result += X[i - 1]
            i -= 1
            v -= 1

        elif list[i - 1, v] > list[i, v - 1]:
            i -= 1
        else:
            v -= 1
    return result[::-1]

