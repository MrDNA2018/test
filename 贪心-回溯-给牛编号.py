#%%
# 题目描述
# 牛牛养了n只奶牛,牛牛想给每只奶牛编号,这样就可以轻而易举地分辨它们了。 每个奶牛对于数字都有自己的喜好,第i只奶牛想要一个1和x[i]之间的整数(其中包含1和x[i])。
# 牛牛需要满足所有奶牛的喜好,请帮助牛牛计算牛牛有多少种给奶牛编号的方法,输出符合要求的编号方法总数。
# #%%
N = int(input())
x = [int(i) for i in input().split()]

count = [0]
temp = [0]*N
def backjacking(arr, depth):

    if depth == N:
        count[0] +=1

    else:
        for i in range(1, x[depth] + 1):
            if i not in temp:
                temp[depth] = i
                backjacking(arr, depth + 1)
                temp[depth] = 0


backjacking(x, 0)
print(count[0] % 1000000007)
#%%
N = int(input())
x = [int(i) for i in input().split()]

x = sorted(x)

res = x[0]
for i in range(1, N):
    res *= (x[i] - i)
print(res % 1000000007)