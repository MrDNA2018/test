# 给定数组arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]，返回第一个1的下标
def binarySearch(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        if arr[mid] == 0:
            # 这个是递归的出口之一
            if arr[mid + 1] == 1:
                return mid + 1
            else:
                return binarySearch(arr, mid + 1, right)

        else:
            # 这个是递归的出口之一
            if arr[mid - 1] == 0:
                return mid
            else:
                return binarySearch(arr, left, mid - 1)
