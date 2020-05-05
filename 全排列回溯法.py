strs = "acc"
# strs = input()
strs = [i for i in strs]
res = []
visited = set()
def perm_backtracking(depth,lst):
    size = len(lst)
    if depth == size:
        temp = ''.join(lst)
        visited.add(temp)
    else:
        for i in range(depth,size):
            lst[depth],lst[i] = lst[i],lst[depth]
            perm_backtracking(depth+1,lst)
            lst[depth],lst[i] = lst[i],lst[depth]

perm_backtracking(0,strs)
print(list(', '.join(sorted(visited))))

#%%
# 题目描述
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
strs = input()
strs = [i for i in strs]

visit = set()
N = len(strs)

def backjacking(depth,lst):
    if depth == N:
        visit.add(''.join(lst))
    else:
        for i in range(depth,N):
            lst[i],lst[depth] = lst[depth],lst[i]
            backjacking(depth+1,lst)
            lst[i],lst[depth] = lst[depth],lst[i]

backjacking(0,strs)
print('['+', '.join(sorted(visit))+ ']')