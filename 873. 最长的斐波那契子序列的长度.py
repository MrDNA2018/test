#%%
class Solution:
    def lenLongestFibSubseq(self, A) -> int:

        n = len(A)
        max_count = 0
        S = set(A)
        for i in range(n):
            for j in range(i + 1, n):
                x,y = A[j],A[i]+A[j]
                count = 2
                while y in S:
                    x,y = y,x+y
                    count += 1
                if count > max_count:
                    max_count = count

        return [0, max_count][max_count >= 3]

A = [1,2,3,4,5,6,7,8]
res = Solution().lenLongestFibSubseq(A)
print(res)