# 状态转移方程:
# F [i, v] = max {F [i − 1, v], F [i − 1, v − C i ] + W i }
# 后来仔细考虑出后之后，做了如下修正：
def pack_0_1_Top_down(N, V, C, W):
    list = [[-1] * (V + 1) for i in range(N + 1)]
    #    mins = min(C)
    #    for i in range(N+1):
    #        for j in range(V+1):
    #            if i == 0 or j< mins:
    #                list[i][j] =0
    list[0] = [0] * (V + 1)

    def pack_0_1_Top_down_(N, V):
        #        if list[N][V] == -1 and N >=1 and V >=mins:
        if list[N][V] == -1 and N >= 1:
            A = pack_0_1_Top_down_(N - 1, V)
            if V < C[N - 1]:
                return A
            else:
                list[N][V] = max(A, pack_0_1_Top_down_(N - 1, V - C[N - 1]) + W[N - 1])

        return list[N][V]

    return pack_0_1_Top_down_(N, V)


def pack_0_1_bottom_up(N, V, C, W):
    list = [[-1] * (V + 1) for i in range(N + 1)]
    list[0] = [0] * (V + 1)

    for i in range(1, N + 1):
        for j in range(0, V + 1):
            A = list[i - 1][j]
            if j < C[i - 1]:
                list[i][j] = A
            else:
                list[i][j] = max(A, list[i - 1][j - C[i - 1]] + W[i - 1])
    #    print list
    return list[N][V]

#%%
def pack_0_1_first(N, V, C, W):
    def ZeroOnePack(F, ci, wi):
        for v in range(V, ci - 1, -1):
            F[v] = max(F[v], F[v - ci] + wi)
        return F

    F = [0] * (V + 1)

    for i in range(1, N + 1):
        ZeroOnePack(F, C[i - 1], W[i - 1])
    return F[V]
#%%
def pack_0_1_yes_or_no(N, V, C):
    def ZeroOnePack(F, ci):
        for v in range(V, ci - 1, -1):
            F[v] = F[v - ci] or F[v]
        return F

    F = [-1] * (V + 1)
    F[0] = True

    for i in range(1, N + 1):
        ZeroOnePack(F, C[i - 1])

    return F[V]
