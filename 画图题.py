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
