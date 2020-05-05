def partition_1(arr, low, high):
    # 把基准元素取出来，留出一个空位，这里是在首位，这种留出空位的方式，比较容易理解
    pivot = arr[low]

    # 循环体终止条件，因为是先走右边再走左边，终止的时候一定是两个指针重合在一起
    # 也可以交叉，但是可以控制循环他们重合在一起跳出循环
    # 这里解释以下low,high这两个指针代表什么，low，high代表从其实到low都是小于基准的元素
    # 从high到end都是大于基准的元素，当low和high重合时，那左边都是小的，右边都是大的
    # 重合的位置是空的（实际上有值），因为每个时刻都有一个位置都是空的，重合剩下最后一个位置，
    # 这个位置也必然是空的，也可以用一个小的实例分析一下
    while low < high:
        # 首先右边一直往左走，直到遇到小于基准的元素，这里控制一下，不让他们交叉
        # 不添加的low <high，往左走不会越界，但是可能小于low
        while arr[high] > pivot and low < high:
            high -= 1
        # 避免他们两交叉，只要相等就退出，右边遇到小于基准的元素，把左边的那个空位填上，左边的指针更新一下
        if low < high:
            arr[low] = arr[high]
            low += 1
        # 左指针往左就是小于基准的元素，这时右边空出来一个位置，左指针往右扫描
        while arr[low] < pivot and low < high:
            low += 1
        # 找到大于基准的元素，放到右边空出来的位置，那右指针往右全部都是大于基准元素的
        if low < high:
            arr[high] = arr[low]
            high -= 1
    # 当只剩下唯一的空位置时，把基准元素放待空的位置上
    arr[low] = pivot

    return low

#%%
def partition_2(arr, low, high):
    # 这时另外一种考虑方式，而且他是不需要额外空间的，他只使用一个指针来区分小于基准和大于基准的
    # pointer_less_than代表这个指针的左边全部都是小于基准的（包括自己，不包括首元素）
    # 然后从左往右扫描，遇到小于基准的元素，就把小于基准元素区域的后面紧接着的一个元素和他交换
    # 那么小于基准元素区域就多了一个元素，。。。就这样小于基准的元素就连在了一起
    # 首元素是基准元素，小于基准元素区域块，大于基准元素区域块，现在分成了三个部分
    # 把首元素和小于基准元素区域块最后一个元素交换，那三部分就变成，小于的，基准，大于的

    # 刚开始小于基准的元素为0，暂且指向首位值
    pointer_less_than = low
    # 然后一次扫描后面所有元素
    for i in range(pointer_less_than + 1, high + 1):
        # 遇到小于基准的，就把小于基准元素区域的后面紧接着的一个元素和他交换，小于的块相当于也更新了
        if arr[i] < arr[low]:
            pointer_less_than += 1
            arr[pointer_less_than], arr[i] = arr[i], arr[pointer_less_than]
    #  把首元素和小于基准元素区域块最后一个元素交换，那三部分就变成，小于的，基准，大于的
    arr[low], arr[pointer_less_than] = arr[pointer_less_than], arr[low]

    return pointer_less_than
#%%
def partition_3(arr, start, end):
    # 这个方式也是不需要额外的辅助空间的
    # 他的思想是：从左（或者右也可以）扫描到第一个大于基准的元素，然后从右往左扫描到第一个小于基准的
    # 元素，将他们两交换，然后再重复上述操作，直到两个指针重合位置
    # 这两个指针分别代表：前面（除了首元素）到low为小于基准，high到end为大于基准元素
    # 他们是可能会交叉的，也有可能重合，这时数组分成三个部分：首元素基准，小于的，大于的
    # 这个地方可能会交叉的，也有可能重合，分3种情况：第一种情况[大于,小于]，然后他们两个交换
    # [小于，大于]，low-->大于，high-->小于，这时首元素需要和high互换
    # [小于]，high-->小于，没有大于的元素和他互换，low一直加直到等于high,这时这时首元素需要和high互换
    # [大于]，low-->大于，没有小于的元素和他互换，high会一直减，直到比low小1，这时这时这时首元素需要和high互换
    # 不管是那种情况下，high指向肯定是最后一个小于基准的元素
    # 这里不能利用两者指针重合，因为两个指针重合指向的元素，可能大于基准也可能小于基准，
    # 要使用high指向的元素

    # 初始化左指针和右指针
    low = start
    high = end + 1

    # 循环体退出条件为两指针重合或者交叉
    while True:
        # 需要先-1，因为交换之后，指针需要更新一下，不更新的话，循环体会多运算一步
        high -= 1
        # 这里就是需要两指针交叉，这样high才能指向小于区域里面的最后一个元素
        while arr[high] > arr[start]:
            high -= 1

        low += 1
        while arr[low] < arr[start] and low < end:
            low += 1

        # 在这个时候，数组分成三个部分：首元素是基准元素，小于基准元素区域块，大于基准元素区域块
        if low >= high:
            break
        # 把这两个元素交换，小的跑到左边，大的跑到右边
        arr[low], arr[high] = arr[high], arr[low]
    # 把首元素和小于基准元素区域块最后一个元素交换，那三部分就变成，小于的，基准，大于的
    arr[start], arr[high] = arr[high], arr[start]

    return high
#%%
# %%
def quickSort(arr, low, high):
    if low < high:
        index = partition_1(arr, low, high)
        quickSort(arr, low, index - 1)
        quickSort(arr, index + 1, high)


def quickSort1(arr, low, high):
    if low < high:
        index = partition_2(arr, low, high)
        quickSort1(arr, low, index - 1)
        quickSort1(arr, index + 1, high)


def quickSort2(arr, low, high):
    if low < high:
        index = partition_3(arr, low, high)
        quickSort2(arr, low, index - 1)
        quickSort2(arr, index + 1, high)


arr = [7, 3, 66, 33, 22, 66, 99, 0, 1]
print(arr)
quickSort(arr, 0, len(arr) - 1)
print(arr)

arr1 = [7, 3, 66, 33, 22, 66, 99, 0, 1]
# print(arr1)
quickSort1(arr1, 0, len(arr1) - 1)
print(arr1)

arr2 = [7, 3, 66, 33, 22, 66, 99, 0, 1]
# print(arr2)
quickSort2(arr2, 0, len(arr2) - 1)
print(arr2)

# [7, 3, 66, 33, 22, 66, 99, 0, 1]
# [0, 1, 3, 7, 22, 33, 66, 66, 99]
# [0, 1, 3, 7, 22, 33, 66, 66, 99]
# [0, 1, 3, 7, 22, 33, 66, 66, 99]
