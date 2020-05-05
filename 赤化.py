
N =  int(input().split()[0])
l2 = [int(i) for i in input().split()]
k = int(input().split()[0])
#%%
res = []
for i in range(N-k+1):
    j = i + k-1
    res.append(str(max(l2[i:j+1])))

print(' '.join(res))