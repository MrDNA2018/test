# "ababcdec" d
# "a..b..abcdec" d

#%%
# 方法一：
inputs = 'a'*100000 + 'b'*100000 + 'abcdec'
for i in range(len(inputs)):
    if inputs[i] not in set(inputs[i+1:]) and inputs[i] not in set(inputs[:i]):
        print(inputs[i])
        break
#%%
# inputs = "ababcdec"
# 方法二：
inputs = 'a'*100000 + 'b'*100000 +  'c'*100000 + 'abcdec'
temp = set()
length = len(inputs)
for i in range(length):
    if inputs[i] not in temp:
        temp.add(inputs[i])
        flag = 0
        for j in range(i+1,length):
            if inputs[j] == inputs[i]:
                flag = 1
                break
        if flag == 0:
            print(inputs[i])
            break
# 已完成
#%%
# 方法三
inputs = 'a'*100000 + 'b'*100000 + 'c'*100000 + 'abcdec'
result = {}
for char in inputs:
    result[char] = result.setdefault(char, 0) + 1

for char in inputs:
    if result[char] == 1:
        print(char)
        break




#%%
if __name__ == '__main__':
    pass