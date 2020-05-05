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