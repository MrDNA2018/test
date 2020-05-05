from heapq import *
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.father = None

    def is_left(self):
        return self.father.left == self


def init_heapq(strs, strs_set):
    hq = []

    for i in strs_set:
        i_num = strs.count(i)
        heappush(hq, (i_num, Node(i)))

    return hq



def create_tree(hq):

    hqq = hq[:]
    nodes =[]

    while len(hqq) > 1:
        (left_num,left) = heappop(hqq)
        if len(left.data) == 1:
            nodes.append(left)
        (right_num,right) = heappop(hqq)
        if len(right.data) == 1:
            nodes.append(right)
        left_right_father = Node(left.data + right.data)
        left_right_father.left = left
        left_right_father.right = right
        left.father = left_right_father
        right.father = left_right_father
        father_num = left_num + right_num
        heappush(hqq,(father_num,left_right_father))


    root = heappop(hqq)[1]
    return nodes, root


def encode_huffman(nodes, root):

    en_dicts = {}
    for node in nodes:
        while node is not root:
            if node.is_left():
                en_dicts[node.data] = '0' + en_dicts.setdefault(node.data, '')
            else:
                en_dicts[node.data] = '1' + en_dicts.setdefault(node.data, '')
            node = node.father
    return en_dicts



if __name__ == '__main__':
    strs = 'abbcccdddd'
    strs = [i for i in strs]
    strs_set = set(strs)
    hq = init_heapq(strs, strs_set)
    nodes,root = create_tree(hq)
    result = encode_huffman(nodes, root)




#%%
from heapq import *
# 输入，转化为list
strs = input()
strs = [i for i in strs]

# 去重
str_single = set(strs)

# 按照词频入优先级队列
hq =[]
for s in str_single:
    heappush(hq,(strs.count(s),s))

# 初始化明文字典
result = {}
for i in str_single:
    result[i] = ''

# 从树叶往上构建哈夫曼编码
while hq:
    left = heappop(hq)
    if hq:
        right = heappop(hq)
        # 取两个最小词频的节点，单个字母优先在左边
        if left[0] == right[0]:
            if len(left[1]) > len(right[1]):
                left,right = right,left
        # 左边对应编码加0，非单个单词比如‘cd',那么对应的c和d的哈夫曼编码均需要加0
        for i in left[1]:
            result[i] +=  '0'
        # 右边对应编码加1
        for i in right[1]:
            result[i] +=  '1'
        # 把合成节点放入优先队列
        heappush(hq,(left[0]+right[0],left[1]+right[1]))
    else:
        break

# 最后结果对应哈夫曼编码是反的，故反转一下
for k,v in result.items():
    v = [i for i in v]
    result[k] = ''.join(v[::-1])
# 输出结果
for i in strs:
    print(''.join(result[i]),end='')
    #%%
# 树节点类构建
class TreeNode(object):
    def __init__(self, data):
        self.val = data[0]
        self.priority = data[1]
        self.leftChild = None
        self.rightChild = None
        self.code = ""
# 创建树节点队列函数
def creatnodeQ(codes):
    q = []
    for code in codes:
        q.append(TreeNode(code))
    return q
# 为队列添加节点元素，并保证优先度从大到小排列
def addQ(queue, nodeNew):
    if len(queue) == 0:
        return [nodeNew]
    for i in range(len(queue)):
        if queue[i].priority >= nodeNew.priority:
            return queue[:i] + [nodeNew] + queue[i:]
    return queue + [nodeNew]
# 节点队列类定义
class nodeQeuen(object):

    def __init__(self, code):
        self.que = creatnodeQ(code)
        self.size = len(self.que)

    def addNode(self,node):
        self.que = addQ(self.que, node)
        self.size += 1

    def popNode(self):
        self.size -= 1
        return self.que.pop(0)
# 创建哈夫曼树
def creatHuffmanTree(nodeQ):
    while nodeQ.size != 1:
        node1 = nodeQ.popNode()
        node2 = nodeQ.popNode()
        r = TreeNode([None, node1.priority+node2.priority])
        r.leftChild = node1
        r.rightChild = node2
        nodeQ.addNode(r)
    return nodeQ.popNode()
# 各个字符在字符串中出现的次数，即计算优先度
def freChar(string):
    d ={}
    for c in string:
        if not c in d:
            d[c] = 1
        else:
            d[c] += 1
    return sorted(d.items(),key=lambda x:x[1])


string = "AAGGDCCCDDDGFBBBFFGGDDDDGGGEFFDDCCCCDDFGAAA"
t = nodeQeuen(freChar(string))
tree = creatHuffmanTree(t)
codeDic1 = {}
codeDic2 = {}
# 由哈夫曼树得到哈夫曼编码表
def HuffmanCodeDic(head, x):
    global codeDic, codeList
    if head:
        HuffmanCodeDic(head.leftChild, x+'0')
        head.code += x
        if head.val:
            codeDic2[head.code] = head.val
            codeDic1[head.val] = head.code
        HuffmanCodeDic(head.rightChild, x+'1')

# 字符串编码
def TransEncode(string):
    global codeDic1
    transcode = ""
    for c in string:
        transcode += codeDic1[c]
    return transcode
# 字符串解码
def TransDecode(StringCode):
    global codeDic2
    code = ""
    ans = ""
    for ch in StringCode:
        code += ch
        if code in codeDic2:
            ans += codeDic2[code]
            code = ""
    return ans
