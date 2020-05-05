#%%
l1 = input().split()
N = int(l1[0])
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
#%%
res = 0
for i in range(N):
    for j in range(i + 2, N, 2):
        if l3[i] == l3[j]:
            res += (i + 1 + j + 1) * (l2[i] + l2[j])

print(res % 10007)