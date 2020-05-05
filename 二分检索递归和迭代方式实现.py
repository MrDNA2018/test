# %%
# 注意递归的返回值，递归的要返回的话，要前后一致，或者直接基于某一层考虑，把递归看成结果
def binary_Serach_recursive(arr, left, right, target):
    middle = (left + right) // 2
    # 递归出口
    if left > right:
        return (-1)

    if arr[middle] == target:
        return (middle)

    elif arr[middle] < target:
        # 这里没有return的话，结果就没法return出来
        return binary_Serach_recursive(arr, middle + 1, right, target)

    else:
        return binary_Serach_recursive(arr, left, middle - 1, target)


def binary_Serach_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    # 循环体条件
    while left <= right:

        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


# %%
arr = [7, 3, 66, 33, 22, 66, 99, 0, 1]
sort_arr = sorted(arr)
print(sort_arr)
print(binary_Serach_recursive(sort_arr, 0, len(arr) - 1, 22))
print(binary_Serach_recursive(sort_arr, 0, len(arr) - 1, 100))
print(binary_Serach_iterative(sort_arr, 22))
print(binary_Serach_iterative(sort_arr, 100))

# [0, 1, 3, 7, 22, 33, 66, 66, 99]
# 4
# -1
# 4
# -1
