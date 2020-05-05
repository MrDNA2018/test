#%%
# ■题目描述
# 给定一个正整数数组，最大为100个成员，从第一个成员开始，走到数组最后一个成员最少的步骤数，
# 第一步必须从第一元素开始，1<=步长<len/2, 第二步开始以所在成员的数字走相应的步数，如果目标不可达返回-1，只输出最少的步骤数量

# strs = "7 5 9 4 2 6 8 3 5 4 3 9"
strs = "1 1 1 1 1 1 1 1 1 1 1"
strs = [int(i) for i in strs.split()]

res = []
N = len(strs)

for i in range(1,N//2):
    step = 1
    while i < N-1:
        i += strs[i]
        step +=1
    if i == N-1:
        res.append(step)
print(res)
print(min(res))