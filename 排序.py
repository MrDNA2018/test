# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("%d" %arr[i])

# This code is contributed by Mohit Kumra
#%%
# Python program for implementation of Selection
# Sort
import sys

A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

        # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i]),
#%%
# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i]),
#%%

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

# This code is contributed by Mohit Kumra

    def quickSorting(self, arry):
        def qsort_rec(arry, start, end):
            if start >= end:
                return
            i = start
            j = end
            pivot = arry[start]
            while i < j:
                while i < j and arry[j] >= pivot:
                    j -= 1
                if i < j:
                    arry[i] = arry[j]
                    i += 1
                while i < j and arry[i] <= pivot:
                    i += 1
                if i < j:
                    arry[j] = arry[i]
                    j -= 1
            arry[i] = pivot
            qsort_rec(arry, start, i - 1)
            qsort_rec(arry, i + 1, end)

        qsort_rec(arry, 0, len(arry) - 1)


    def quickSorting2(self, arry):
        def qsort_rec(arry, start, end):

            if start >= end:
                return

            i = start
            for j in range(start + 1, end + 1):
                if arry[j] < arry[start]:
                    i += 1
                    arry[i], arry[j] = arry[j], arry[i]
            arry[i], arry[start] = arry[start], arry[i]
            qsort_rec(arry, start, i - 1)
            qsort_rec(arry, i + 1, end)

        qsort_rec(arry, 0, len(arry) - 1)
#%%
    def mergeSorting(self, arry):

        def two_part_sort(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result += [left[i]]
                    i += 1
                else:
                    result += [right[j]]
                    j += 1

            result += left[i:]
            result += right[j:]

            return result

        def msort_rec(arry):

            n = len(arry)
            mid = n // 2

            if mid < 1:
                return arry

            left = msort_rec(arry[:mid])
            right = msort_rec(arry[mid:])
            result = two_part_sort(left, right)

            return result

        return msort_rec(arry)


    def mergeSorting3(self, arry):
        def two_sorted_arrys_sorting_in_place(arry, left, mid, right):
            result = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if arry[i] <= arry[j]:
                    result += [arry[i]]
                    i += 1
                else:
                    result += [arry[j]]
                    j += 1

            result += arry[i:mid + 1]
            result += arry[j:right + 1]

            arry[left:right + 1] = result[0:right - left + 1]

        cur_size = 1
        while cur_size < len(arry) - 1:
            left = 0
            while left < len(arry) - 1:
                mid = left + cur_size - 1
                right = ((left + 2 * cur_size - 1, len(arry) - 1)[left + 2 * cur_size - 1 > len(arry) - 1])
                two_sorted_arrys_sorting_in_place(arry, left, mid, right)
                left = left + cur_size * 2

            cur_size = 2 * cur_size


    def mergeSorting2(self, arry):
        def two_part_sort(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result += [left[i]]
                    i += 1
                else:
                    result += [right[j]]
                    j += 1

            result += left[i:]
            result += right[j:]

            return result

        def binary_function(arry):
            result = []
            i = 0
            while i <= len(arry) - 2:
                result += [two_part_sort(arry[i], arry[i + 1])]
                i += 2

            if i == len(arry) - 1:
                result += [arry[i]]

            return result

        i = len(arry) + 1
        result = [[val] for _, val in enumerate(arry)]

        while i >= 1:
            result = binary_function(result)
            i //= 2
        return result[0]

#%%
# Python program for implementation of Shell Sort

def shellSort(arr):

	# Start with a big gap, then reduce the gap
	n = len(arr)
	gap = n/2

	# Do a gapped insertion sort for this gap size.
	# The first gap elements a[0..gap-1] are already in gapped
	# order keep adding one more element until the entire array
	# is gap sorted
	while gap > 0:

		for i in range(gap,n):

			# add a[i] to the elements that have been gap sorted
			# save a[i] in temp and make a hole at position i
			temp = arr[i]

			# shift earlier gap-sorted elements up until the correct
			# location for a[i] is found
			j = i
			while j >= gap and arr[j-gap] >temp:
				arr[j] = arr[j-gap]
				j -= gap

			# put temp (the original a[i]) in its correct location
			arr[j] = temp
		gap /= 2


# Driver code to test above
arr = [ 12, 34, 54, 2, 3]

n = len(arr)
print ("Array before sorting:")
for i in range(n):
	print(arr[i]),

shellSort(arr)

print ("\nArray after sorting:")
for i in range(n):
	print(arr[i]),

# This code is contributed by Mohit Kumra
#%%
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
   largest = i # Initialize largest as root
   l = 2 * i + 1	 # left = 2*i + 1
   r = 2 * i + 2	 # right = 2*i + 2

   # See if left child of root exists and is
   # greater than root
   if l < n and arr[i] < arr[l]:
   	largest = l

   # See if right child of root exists and is
   # greater than root
   if r < n and arr[largest] < arr[r]:
   	largest = r

   # Change root, if needed
   if largest != i:
   	arr[i],arr[largest] = arr[largest],arr[i] # swap

   	# Heapify the root.
   	heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
   n = len(arr)

   # Build a maxheap.
   for i in range(n, -1, -1):
   	heapify(arr, n, i)

   # One by one extract elements
   for i in range(n-1, 0, -1):
   	arr[i], arr[0] = arr[0], arr[i] # swap
   	heapify(arr, i, 0)

# Driver code to test above
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
   print ("%d" %arr[i]),
# This code is contributed by Mohit Kumra
