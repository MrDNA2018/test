#%%
t = int(input())
n,k = [int(i) for i in input().split()]
def wash(arr):
    left = arr[:n]
    right = arr[n:]
    res = []
    for i in range(n - 1, -1, -1):
        res.append(right[i])
        res.append(left[i])
    return res[::-1]

for _ in range(t):
    nums = input().split()
    s = nums[:2*n]
    for _ in range(k):
        s = wash(s)
    print(' '.join(s))
    n=int(nums[-2])
    k=int(nums[-1])