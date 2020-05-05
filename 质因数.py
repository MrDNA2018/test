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