# 以01背包为例:
# 首先看01背包求最优解的状态转移方程: F [i, v] = max {F [i − 1, v], F [i −1, v − C i ] + W i } 。如果要求第 K 优解,那么状态 F [i, v] 就应该是一个大小为 K 的队列 F [i, v, 1 . . . K] 。其中 F [i, v, k] 表示前 i 个物品中,背包大小为 v 时,第 k 优解的值。这里也可以简单地理解为在原来的方程中加了一维来表示结果的优先次序。显然 f [i, v, 1 . . . K] 这 K 个数是由大到小排列的,所以它可看作是一个有序队列。
#
# 为什么这个方法正确呢?实际上,一个正确的状态转移方程的求解过程遍历了所有可用的策略,也就覆盖了问题的所有方案。只不过由于是求最优解,所以其它在任何一个策略上达不到最优的方案都被忽略了。如果把每个状态表示成一个大小为 K 的数组,并在这个数组中有序地保存该状态可取到的前 K 个最优值。那么,对于任两个状态的max运算等价于两个由大到小的有序队列的合并。
import numpy as np


def pack_01_Bottom_up(N, V, C, W, K):
    list = np.zeros((K, V + 1), dtype=int)
    A = [0] * (K + 1)
    B = [0] * (K + 1)
    for i in range(1, N + 1):
        for v in range(V, C[i - 1] - 1, -1):
            for k in range(K):
                A[k] = list[k, v]
                B[k] = list[k, v - C[i - 1]] + W[i - 1]
            A[K], B[K] = -1, -1
            x, y, k = 0, 0, 0
            # 因为去重，所以x<K,y<K就无法保证k取到K了，所以用到了一个trick,这里是归并排序归并操作的改进
            while k < K and (A[k] != -1 or B[k] != -1):
                if A[x] > B[y]:
                    list[k, v] = A[x]
                    x += 1
                else:
                    list[k, v] = B[y]
                    y += 1
                # 去重
                if list[k, v] != list[k - 1, v]:
                    k += 1

    return list[:, V]
