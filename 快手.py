# 一年一度的快手运动会又要开始了，同学们终于有一天可以离开鼠标键盘显示器，全身心的投入到各种体育项目中。UED设计师小红虽然没有参加体育项目，但她的责任重大，因为她是拉拉队的队长，她需要在每个项目中为参赛的同学们加油助威。
#
# 因为运动会的项目众多，很多项目在同一时间会同时进行着。作为拉拉队长，小红需要遵守以下规则：
#
# 不能同时给多个体育项目加油助威
#
# 给每个体育项目加油的时长必须超过项目时长的一半，每个体育项目只能加油一次
#
# 体育项目的开始和结束时间都是整点，如果项目进行到一半想要离开，也只能选择整点离开
#
# 不考虑往返于各个体育项目比赛场地中花费的时间
#
# 请帮小红设计一个算法，在已知所有体育项目日程的前提下，计算是否能在每个体育项目中为参赛的同学们加油。
#
#
# 说明：
#
# 如果体育项目时长为2，超过时长的一半为2;
#
# 如果体育项目时长为3，超过时长的一半为2;
#
# 如果体育项目时长为4，超过时长的一半为3；

def f():
    n=int(input())
    events=[]
    for i in range(n):
        line=[int(item) for item in input().split()]
        events.append(line)
    events=sorted(events,key=lambda x:x[1]-(x[1]-x[0])//2-1)
    start=events[0][0]
    for i in range(n):
        if start>events[i][1]-(events[i][1]-events[i][0])//2-1:
            return -1
        end=start+(events[i][1]-events[i][0])//2+1
        if i==n-1:
            return 1
        start=max(end,events[i+1][0])
    return 1
ans=f()
print(ans)

#%%
# 有位老铁设计了一个跳格子游戏，游戏有N个格子顺序排成一行，编号从1到N，每个格子有点数Qi，有标记Li（标记的范围是1-M），每次跳格子，要选择一个格子a，以任意正偶数距离x跳到格子b，如果格子b在游戏区域内，且La=Lb，则称为一次合法跳跃，获得的分数是(a + b) * (Qa + Qb)。
#
#
# 在继续设计游戏玩法时，这位老铁纠结了很久，于是他决定放弃……但是他想知道所有合法跳跃总共能获得多少分。

n, m = list(map(int, input().split()))
Q = list(map(int, input().split()))
L = list(map(int, input().split()))
li = [[] for _ in range(2 * m)]
result = 0
for i in range(n):
    li[L[i] - 1 + i % 2 * m].append(i + 1)
for l in li:
    q = a = c = 0
    for i in l:
        q += Q[i - 1]
        a += i
        c += i*Q[i - 1]
    result += q*a + c * (len(l) - 2)
print(result % 10007)


#%%

# 有n 个老铁（编号为 1 到n）正在玩丢手绢。在游戏里每人会把当前手里的手绢丢给一个固定的人，编号为Ti。 游戏开始时，每人手里有自己的手绢。之后每一轮中，所有人会同时将自己当前手里的手绢全部丢给接收的对象。当有人重新拿到自己的手绢时，游戏结束。
#
# 那么游戏几轮会结束呢？

def f():
    n = int(input())

    to = [int(item) - 1 for item in input().split()]
    in_degree = [0] * n
    for i in range(n):
        in_degree[to[i]] += 1
    stack = []
    for i in range(n):
        if in_degree[i] == 0:
            stack.append(i)
    while len(stack) != 0:
        top = stack[-1]
        in_degree[top] -= 1  # in_degree==-1,则代表删除了
        stack.pop(-1)
        in_degree[to[top]] -= 1
        if in_degree[to[top]] == 0:
            stack.append(to[top])
    min_num = 200000
    for i in range(n):
        if in_degree[i] == -1:
            continue
        else:
            start = i
            num = 1
            while to[i] != start:
                i = to[i]
                num += 1
                in_degree[i] = -1  # 同一个圈内的就不重复计算环了
            min_num = min(min_num, num)
    return min_num


ans = f()
print(ans)

#%%
# 最近月神需要在移动端部署一个卷积神经网络模型,但是月神碰到了一个问题,即月神使用了一个核非常大的最大池化(max-pooling)操作,但现有推理引擎不支持这一操作,作为月神的好朋友,你能帮帮月神么。
# 所谓max-pooling,指的是给定一个数组（为了简化问题,暂定数组为一维）,在每一个滑动窗口内找出最大的那个数,举例如下：
# 假设数组为[16, 19, 15, 13, 16, 20],且核大小为3,则当窗口依次滑过数组时,取出如下4个子数组：
# [16, 19, 15], [19, 15, 13], [15, 13, 16], [13, 16, 20],这4个子数组中的最大值分别为19, 19, 16, 20,故该数组经过大小为3的核的max-pooling的结果为19 19 16 20.

while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        ks = int(input())
        res = []
        res.append(max(nums[:ks]))
        for i in range(1, n - ks + 1):
            if nums[i-1] == res[-1]:
                res.append(max(nums[i:i+ks]))
            else:
                res.append(max(res[-1], nums[i + ks - 1]))
        res = [str(i) for i in res]
        print(' '.join(res))
    except:
        break
