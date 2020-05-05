# 题目
# 有 N 种物品和一个容量为 V 的背包。第 i 种物品最多有 M i 件可用,每件耗费的空间是 C i ,价值是 W i 。求解将哪些物品装入背包可使这些物品的耗费的空间总和不超过背包容量,且价值总和最大。
#
# 状态转移方程:
# F [i , v] = max {F [i − 1, v − k ∗ C i ] + k ∗ W i | 0 ≤ k ≤ M i }
# 复杂度是 O(V ΣM i ) 。

# F [i , v] = max {F [i − 1, v − k ∗ C i ] + k ∗ W i | 0 ≤ k ≤ M i }
import numpy as np


def pack_multiple_Bottom_up(N, V, C, W, M):
    list = np.zeros((N + 1, V + 1), dtype=int)

    for i in range(1, N + 1):
        for j in range(0, V + 1):
            t = min(j // C[i - 1], M[i - 1])
            result = -1000
            for k in range(t + 1):
                A = list[i - 1, j - k * C[i - 1]] + k * W[i - 1]
                if A > result:
                    result = A
            list[i, j] = result

    return list[N, V]

#%%
import numpy as np


def change_multiple_to_01_yes_or_no(N, V, C, M):
    C_ = []

    for i in range(N):
        t = min(V // C[i], M[i])
        k = 1
        j = t
        while 2 * k <= t:
            C_.append(k * C[i])
            j -= k
            k *= 2
        C_.append(j * C[i])

    def pack_0_1_first(N, V, C):
        F = [False] * (V + 1)
        F[0] = True

        for i in range(1, N + 1):
            for v in range(V, C[i - 1] - 1, -1):
                F[v] = F[v] or F[v - C[i - 1]]
        return F[V]

    N_ = len(C_)
    return pack_0_1_first(N_, V, C_)

#%%
def pack_multiple_yes_or_no(N, V, C, M):
    list = np.zeros((N + 1, V + 1), dtype=int)
    list[:, :] = -1
    list[0, 0] = 0
    for i in range(1, N + 1):

        for j in range(V + 1):
            if list[i - 1, j] >= 0:
                list[i, j] = M[i - 1]
            else:
                list[i, j] = -1

        for j in range(V - C[i - 1] + 1):
            if list[i, j] > 0:
                list[i, j + C[i - 1]] = max(list[i, j + C[i - 1]], list[i, j] - 1)  # list[i,j]-1 #

    return list[N, V]
