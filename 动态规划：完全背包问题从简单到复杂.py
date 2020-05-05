# 状态方程为：
# F [i, v] = max {F [i − 1, v − kC i ] + kW i | 0 ≤ kC i ≤ v}
# another way: F [i, v] = max {F [i − 1, v − kC i ] + kW i | 0 ≤ kC i ≤ v}
def pack_complete_Rec2(N, V, C, W):
    if N == 0:
        return 0
    k = V // C[N - 1]
    result = -1
    for i in range(k + 1):
        A = pack_complete_Rec2(N - 1, V - i * C[N - 1], C, W) + i * W[N - 1]
        if A > result:
            result = A
    return result


import numpy as np


# 注意if list[N,V] == -1 的未知，因为它确定了剪枝；
def pack_complete_Top_down2(N, V, C, W):
    list = np.zeros((N + 1, V + 1), dtype=int)
    list[1:, :] = -1

    def complete_Top_down(N, V):
        t = V // C[N - 1]
        if list[N, V] == -1:
            result = -1000
            for k in range(t + 1):
                if N >= 1:
                    A = complete_Top_down(N - 1, V - k * C[N - 1]) + k * W[N - 1]
                    if A >= result:
                        result = A
            list[N, V] = result
        return list[N, V]

    return complete_Top_down(N, V)


def pack_complete_Bottom_up2(N, V, C, W):
    list = np.zeros((N + 1, V + 1), dtype=int)
    #    list[1:,:] = -1

    for i in range(1, N + 1):
        for j in range(0, V + 1):
            t = j // C[i - 1]
            result = -1000
            for k in range(t + 1):
                A = list[i - 1, j - k * C[i - 1]] + k * W[i - 1]
                if A > result:
                    result = A
            list[i, j] = result

    return list[N, V]
#%%
# 不选：可以看成i-1的问题，二选，就可以看成第i类的01背包问题，因为V是一定的，此时的i实际上不是无限的，是受V限制的，就可以把有限的i看成不同的物品，等价于一个01背包问题，状态方程如下：
# F [i, v] = max (F [i − 1, v], F [i, v − C i ] + W i )
def pack_complete_Rec(N, V, C, W):
    if N == 0:
        return 0
    if V < C[N - 1]:
        return pack_complete_Rec(N - 1, V, C, W)
    return max(pack_complete_Rec(N - 1, V, C, W), pack_complete_Rec(N, V - C[N - 1], C, W) + W[N - 1])


import numpy as np


def pack_complete_Top_down(N, V, C, W):
    list = np.zeros((N + 1, V + 1), dtype=int)
    list[1:, :] = -1

    def complete_Top_down(N, V):
        if list[N, V] == -1 and N >= 1:
            A = complete_Top_down(N - 1, V)
            if V < C[N - 1]:
                return A
            else:
                list[N, V] = max(A, complete_Top_down(N, V - C[N - 1]) + W[N - 1])

        return list[N, V]

    return complete_Top_down(N, V)


def pack_complete_Bottom_up(N, V, C, W):
    list = np.zeros((N + 1, V + 1), dtype=int)
    list[1:, :] = -1

    for i in range(1, N + 1):
        for j in range(0, V + 1):
            A = list[i - 1, j]
            if j < C[i - 1]:
                list[i, j] = A
            else:
                list[i, j] = max(A, list[i, j - C[i - 1]] + W[i - 1])

    return list[N, V]
#%%
def pack_complete_first(N, V, C, W):
    def CompletePack(F, ci, wi):
        for v in range(ci, V + 1):
            F[v] = max(F[v], F[v - ci] + wi)
        return F

    F = [0] * (V + 1)

    for i in range(1, N + 1):
        CompletePack(F, C[i - 1], W[i - 1])
    return F[V]

#%%
def pack_complete_first_yes_or_no(N, V, C):
    def CompletePack_or(F, ci, wi):
        for v in range(ci, V + 1):
            F[v] = F[v] or F[v - ci]
        return F

    F = [False] * (V + 1)
    F[0] = True

    for i in range(1, N + 1):
        CompletePack_or(F, C[i - 1], W[i - 1])
    return F[V]


def pack_complete_Bottom_up_yes_or_no(N, V, C):
    list = np.zeros((N + 1, V + 1), dtype=bool)
    list[0, 0] = True

    for i in range(1, N + 1):
        for j in range(0, V + 1):
            A = list[i - 1, j]
            if j < C[i - 1]:
                list[i, j] = A
            else:
                list[i, j] = A or list[i, j - C[i - 1]]

    return list[N, V]
