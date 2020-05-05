#%%
strs = 'bac'
num = len(strs)
res = set()
for i in range(num):
    for j in range(i+1,num+1):
        if strs[i:j] not in res:
            res.add(strs[i:j])

print(' '.join(sorted(res,key = lambda x:(len(x),x))))

#%%
# 给定一个字符串的数组strs，
# 请找到一种拼接顺序，使得所有的字符串拼接起来组成的字符串是所有可能性中字典序最小的，并返回这个字符串。
n = int(input())
res = []
for i in range(n):
    res.append(input())
def compare(x,y):
    if x+y == y+x:
        return 0
    else:
        return [-1,1][x+y>y+x]
from functools import cmp_to_key
print(''.join(sorted(res,key = cmp_to_key(compare))))