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


#%%
inp = input().strip()
print(eval(inp))
