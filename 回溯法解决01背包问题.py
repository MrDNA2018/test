def pack_01_back(N, V, C, W):
    BestResult = [0] * N
    x = [0] * N
    BestValue = [0]
    CurCost = [0]
    CurValue = [0]

    def pack_01_back_tracking(depth):
        # 递归出口
        if depth > N - 1:
            if CurValue[0] > BestValue[0]:
                BestValue[0] = CurValue[0]
                # x为可行解，在叶子处把可行解记录下来
                BestResult[:] = x[:]
                BestValue
            # 注意ｅｌｓｅ的含义
        else:
            for i in range(2):
                x[depth] = i

                if i == 0:
                    pack_01_back_tracking(depth + 1)
                else:
                    if CurCost[0] + C[depth] <= V:
                        CurCost[0] += C[depth]
                        CurValue[0] += W[depth]
                        pack_01_back_tracking(depth + 1)
                        # 　回溯时的处理，就是往上回溯时，要把吃进去的吐出来
                        CurCost[0] -= C[depth]
                        CurValue[0] -= W[depth]

    pack_01_back_tracking(0)

    return BestResult, BestValue
