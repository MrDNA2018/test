#%%
# 1. 字符串循环移位包含
s1 = 'AABCD'
s2 = 'CDAA'
print(s2 in s1+s1)
#%%
# 2. 字符串循环移位
s = "abcd123"
k = 3
print(s[-k:]+s[:-k])

#%%
# 3. 字符串中单词的翻转
s = "I am a student"
print(' '.join(s.split()[::-1]))

#%%
# 4. 两个字符串包含的字符是否完全相同
s = "rat"
t = "car"

def isAnagram(self, s: str, t: str) -> bool:
    s_dic = {}
    for i in s:
        s_dic[i] = s_dic.setdefault(i, 0) + 1

    t_dic = {}
    for i in t:
        t_dic[i] = t_dic.setdefault(i, 0) + 1

    return s_dic == t_dic

#%%
# 5. 计算一组字符集合可以组成的回文字符串的最大长度
def longestPalindrome(self, s: str) -> int:
    chars = set(s)
    num = 0
    flag = 0
    for i in chars:
        if s.count(i) % 2 == 0:
            num += s.count(i)
        else:
            flag = 1
            num += (s.count(i) - 1)

    return [num, num + 1][flag]