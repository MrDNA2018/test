# -*- coding: utf-8 -*-

# 构造一棵树
# 首先需要定义结点
class BinTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# =============================================================================
# 结合这几个例子，体会一下树形结构
# 树本来就是一个天然的递归结构，每一个递归都对应着一个递归树
# 就二叉树而言，每一个二叉树对应着一个左子树，一个右子树
# 都不用我们思考怎么划分子问题，现在两个子问题就已经划分好了
# 那么每一棵树对应三部分：当前结点，左子树，右子树
# 那么我们处理原问题，只需要对应处理这三部分就可以了
# 递归实现的出口是什么，出口就是叶子结点的左右子树，也就是空树，出口就是空树return
# =============================================================================

# 我们统计树的结点，当前结点1个+左子树的结点和+右子树的结点和
def count_TreeNodes(root):
    if not root:
        return 0
    else:
        return 1 + count_TreeNodes(root.left) + count_TreeNodes(root.right)


# 我们统计树的权值和，当前结点权值+左子树的权值和+右子树的权值和
def sum_TreeValues(root):
    if not root:
        return 0
    else:
        return root.data + sum_TreeValues(root.left) + sum_TreeValues(root.right)

    # 同样的道理，获取树的高度


def height_Tree(root):
    if not root:
        return 0
    else:
        return 1 + max(height_Tree(root.left), height_Tree(root.right))
    # 合并子树


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        else:
            t1 = t1 or t2
        return t1
