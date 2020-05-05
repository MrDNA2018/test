#9. 统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1, ]

        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        res = 0

        for i in range(1, len(groups)):
            res += min(groups[i - 1], groups[i])

        return res