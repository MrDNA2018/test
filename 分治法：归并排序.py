def MergeSort(arr, N):
    # 递归出口，出口需要返回当前的那个数
    if N == 1:
        return arr

    # 以下当作某一层的处理
    middle = N // 2
    # 获取待排序的两个已排序的数组
    left_list = MergeSort(arr[:middle], len(arr[:middle]))
    right_list = MergeSort(arr[middle:], len(arr[middle:]))

    # 如下是针对两个已排序的数组合并成一个有序数组的排列方法，为最基本的双针模型
    i, j = 0, 0
    result = []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1

    result += left_list[i:]
    result += right_list[j:]

    # 返回已排序的结果，用于上一层获取待排序的有序数组
    return result
