#%%
# 7. 回文子字符串个数
# dp[i][j]表示str[i:j+1]是否是回文字符串
# dp[i][j] = dp[i+1][j-1] and strs[i] == str[j]
def countSubstrings( s: str) -> int:
    length = len(s)
    dp = [[False] * length for i in range(length)]
    count = 0
    for i in range(length):
        for j in range(length):
            if i == j:
                dp[i][j] = True
                count += 1

    for i in range(length - 1,-1,-1):
        for j in range(i + 1, length):
            if j - i == 1:
                if s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
            else:
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

    return count

print(countSubstrings('aaaaa'))

#%%
# 8. 判断一个整数是否是回文数
def isPalindrome(self, x: int) -> bool:
    if x == 0:
        return True
    if x < 0 or x % 10 == 0:
        return False

    right = 0
    while x > right:
        right = x % 10 + right * 10
        x //= 10

    return right == x or x == right // 10