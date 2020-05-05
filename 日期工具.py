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