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

#%%
# 6. 字符串同构
def isIsomorphic(self, s: str, t: str) -> bool:

    maps = {}

    for k, v in zip(s, t):

        if k in maps and v != maps[k]:
            return False
        elif k not in maps and v in maps.values():
            return False
        else:
            maps[k] = v

#%%
# 7. 回文子字符串个数
# dp[i][j]表示str[i:j+1]是否是回文字符串
# dp[i][j] = dp[i+1][j-1] and strs[i] == str[j]
def countSubstrings( s: str):
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
#%%
#9. 统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数

class Solution:
    def countBinarySubstrings(self, s: str):
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

#%%
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


#%%
S = '00010001'
T = '00??'
p = T.replace('?','[01]{1}')

res = set()
import re
for i in range(len(S)):
    t = re.findall(re.compile(p),S[i:])
    for _ in t:
        res.add(_)
print(res)
print(len(res))

#%%
S = input()
T = input()
p = T.replace('?','.')

res = set()
import re
for i in range(len(S)):
    t = re.findall(re.compile(p),S[i:])
    for _ in t:
        res.add(_)
print(len(res))
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

#%%
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def dfs(self,grid,r,c):
        grid[r][c] = 0
        rows = len(grid)
        cols = len(grid[0])
        for x,y in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]:
            if 0<=x<rows and 0<=y<cols and grid[x][y] == '1':
                self.dfs(grid,x,y)


    def numIslands(self, grid: List[List[str]]) -> int:

        nums = 0
        rows = len(grid)
        if rows == 0:
            return nums
        cols = len(grid[0])



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    nums +=1
                    self.dfs(grid,i,j)

        return nums


#%%
# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
#
# 最后一个数后面也要有空格

a = int(input())

for i in range(2,int(a**0.5+2)):
    while True:
        if a % i == 0:
            a = int(a/i)
            print(i,end=' ')
        else:
            break
if a >1:
    print(a, end=' ')

#%%
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n= len(nums)
        rightmore = 0

        for i in range(n):
             if i <= rightmore:
                 rightmore = max(rightmore,i + nums[i])

                 if rightmore >= n-1:
                     return True
        return False

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

#%%
# 题目描述
# 牛牛养了n只奶牛,牛牛想给每只奶牛编号,这样就可以轻而易举地分辨它们了。 每个奶牛对于数字都有自己的喜好,第i只奶牛想要一个1和x[i]之间的整数(其中包含1和x[i])。
# 牛牛需要满足所有奶牛的喜好,请帮助牛牛计算牛牛有多少种给奶牛编号的方法,输出符合要求的编号方法总数。
# #%%
N = int(input())
x = [int(i) for i in input().split()]

count = [0]
temp = [0]*N
def backjacking(arr, depth):

    if depth == N:
        count[0] +=1

    else:
        for i in range(1, x[depth] + 1):
            if i not in temp:
                temp[depth] = i
                backjacking(arr, depth + 1)
                temp[depth] = 0


backjacking(x, 0)
print(count[0] % 1000000007)
#%%
N = int(input())
x = [int(i) for i in input().split()]

x = sorted(x)

res = x[0]
for i in range(1, N):
    res *= (x[i] - i)
print(res % 1000000007)
#%%
# ■题目描述
# 给定一个正整数数组，最大为100个成员，从第一个成员开始，走到数组最后一个成员最少的步骤数，
# 第一步必须从第一元素开始，1<=步长<len/2, 第二步开始以所在成员的数字走相应的步数，如果目标不可达返回-1，只输出最少的步骤数量

# strs = "7 5 9 4 2 6 8 3 5 4 3 9"
strs = "1 1 1 1 1 1 1 1 1 1 1"
strs = [int(i) for i in strs.split()]

res = []
N = len(strs)

for i in range(1,N//2):
    step = 1
    while i < N-1:
        i += strs[i]
        step +=1
    if i == N-1:
        res.append(step)
print(res)
print(min(res))

#%%
# 做了一道华为的笔试题，题目如下：
#
# 举办一场8小时的聚会，时间段从12：00到20：00点，让来访的客人事先填好到达的时间和离开的时间，为了掌握聚会期间的座位数目，需要先估计不同时间的最大客人数量。
# 1.到达和离开的时间，以整点计算，输入为整数，比如“12，18”表示客人到达的时间为12点后13点前，离开的时间是17点后18点前。
# 2.按小时区间统计客人的数量，需要统计[12，13),[13,14)….[19，20)共有8个时间段的最大客人数量。
# 3.假设邀请的客人最多100个。
inputs = [[12,15],[16,17],[12,20]]

res = [0]*(20-12)
for pair in inputs:
    for i in range(pair[0]-12,pair[1]-12):
        res[i] +=1
print(res)

#%%
class Solution:
    def year_run(self, year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False

    def dayOfYear(self, date: str) -> int:
        date = date.split('-')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month_days_run = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = 0
        if self.year_run(year):
            for i in range(month - 1):
                res += month_days_run[i]

        else:
            for i in range(month - 1):
                res += month_days[i]

        res += day

        return res
#%%
import time
def dayOfYear(date):
    return time.strptime(date, "%Y-%m-%d")
print(dayOfYear("2019-02-10"))
#%%
import calendar

cal = calendar.month(9999, 1)
print(type(cal))

#%%
strs = [int(i) for i in '2000 02 4 6'.split()]
year = strs[0]
months = strs[1]
weeks = strs[2]
days = strs[3]
if weeks > 5:
    print('0')
import calendar
cal = calendar.month(year,months)


res = cal.split('\n')[2:7]

li = []
for i in res:
    li.append(i.split())

for i in range(7-len(li[0])):
    li[0].insert(0,'0')

for i in range(7-len(li[-1])):
    li[-1].append('0')


day = li[weeks-1][days-1]

print("{}-{}-{}".format(year,months,day))

#%%
strs = 'A={1,3,5},B={2,4,6},R=1'
p = 'A={(.*?)},B={(.*?)},R=(\d+)'
import re
t = re.findall(re.compile(p),strs)
A = [int(i) for i in t[0][0].split(',')]
B = [int(i) for i in t[0][1].split(',')]
R = int(t[0][2])

res = []
for ai in A:
    flag = 0
    for bj in B:
        if bj >= ai:
            if bj -ai <= R:
                flag = 1
                res.append((ai,bj))
            else:
                if flag ==0:
                    flag = 1
                    res.append((ai, bj))
                    break
print(res)

for item in res:
    print('({},{})'.format(item[0],item[1]), end='')

