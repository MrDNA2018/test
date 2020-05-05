# 对于kSum的问题，很容易想到使用动态规划，问题规模由3个方面：元素个数n,kSum的k,以及目标target
# 状态方程为：dp[n][k][target] = dp[n-1][k-1][target-arr[n]] (选第n个数）+ dp[n-1][k][target](不选第n个数）
# 为可能性问题，最后必须装满，也就是k=0时，target =0才能时找到了一个方案，所以dp[n][k][target] = dp[n-1][k-1][target-arr[n]] or dp[n-1][k][target]
import numpy as np


def kSum(arr, target, k):
    n = len(arr)

    dp = np.full((n + 1, k + 1, target + 1), False)

    # 初始化,为可能性问题，也就是最后必须k和target都用完了，才是最后的解
    # 不能使用dp[:][0][0] = True,这两个的赋值不一样，这里是一个容易出错的地方
    for i in range(n + 1):
        dp[i][0][0] = True

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # 这里是一个剪枝，假如k小于元素个数就没有必要考虑了
            if j <= i:
                for l in range(1, target + 1):
                    # 注意边界，假如l-arr[i-1]<0，就没有意义了，只能取左边
                    if l - arr[i - 1] >= 0:
                        dp[i][j][l] = dp[i - 1][j][l] or dp[i - 1][j - 1][l - arr[i - 1]]
                    else:
                        dp[i][j][l] = dp[i - 1][j][l]

    return dp[n][k][target]


arr = [16, 7, 8, 44, 2, 4, 5, 97, 5, 3]
print(kSum(arr, 99, 3))
print(kSum(arr, 102, 3))

False
True
