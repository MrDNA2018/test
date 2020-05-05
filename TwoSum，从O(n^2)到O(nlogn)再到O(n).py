# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# 双针模型，蛮力算法，时间复杂度O(n^2)
def twoSum_two_pointer(arr, target):
    n = len(arr)
    # i为第一个数的位置，j为第二个数的位置
    for i in range(n - 1):
        rest = target - arr[i]
        for j in range(i + 1, n):
            if arr[j] == rest:
                return True, [arr[i], rest]

    return False
#%%
# 利用有序的数组，寻找第二个数时，可以使用二分查找法为logn,整个时间复杂度为O(nlogn)
def twoSum_sorted_binary_Serach(arr, target):
    n = len(arr)
    # 排序O(nlogn)
    arr = sorted(arr)

    # 二分查找，logn
    def binary_Serach_recursive(arr, left, right, target):

        middle = (left + right) // 2
        # 递归出口
        if left > right:
            return False

        if arr[middle] == target:
            return True

        elif arr[middle] < target:
            # 这里没有return的话，结果就没法return出来
            return binary_Serach_recursive(arr, middle + 1, right, target)

        else:
            return binary_Serach_recursive(arr, left, middle - 1, target)

    # 遍历第一个数，查询第二个数
    for i in range(n - 1):
        rest = target - arr[i]
        if binary_Serach_recursive(arr, i + 1, n - 1, rest):
            return True, [arr[i], rest]

    return False
#%%
# python里面set使用的是哈希方式实现，查找时间复杂度O(1)，整体时间复杂度O(n)
def twoSum_hash(arr, target):
    n = len(arr)
    # 哈希表
    visit = set()

    # 遍历第一个数，需要遍历n个，查询第二个数是否在哈希表里
    for i in range(n):
        rest = target - arr[i]
        if rest in visit:
            return True, [arr[i], rest]
        # 假如这个数不再哈希表里，就添加到哈希表里面，这种操作步骤，已经保证
        # 任意两个数都组合过
        # 当遇到ab比较，ba就没必要比较时，指针对应的就是i,j =i+1,而在哈希里，对应的
        # 就是逐步加入元素
        visit.add(arr[i])

    return False
#%%
