
l1 = input().split()
N = int(l1[0])
l2 = [int(i)-1 for i in input().split()]
#%%
res = 0
temp = [[i] for i in range(N)]
temp1 = [[] for i in range(N)]
flag = True
while flag:
    res += 1
    for i in range(N):
        for _ in temp[i]:
            temp1[l2[i]].append(_)

    temp[:] = temp1[:]
    temp1 = [[] for i in range(N)]
    print(temp)

    for i in range(N):
        if i in temp[i]:
            flag = False
            break

print(res)