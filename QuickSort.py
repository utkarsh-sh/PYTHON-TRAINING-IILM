'''def hoare_partition(arr, low, high):
    pivot = arr[low]  # Choosing the first element as pivot
    p = low + 1
    q = high

    while True:
        while p <= q and arr[p] < pivot:
            p += 1
        while p <= q and arr[q] > pivot:
            q -= 1

        if p >= q:
            break

        arr[p], arr[q] = arr[q], arr[p]

    arr[low], arr[q] = arr[q], arr[low]  # Swap pivot with partition index
    return q  # Return the partition index


def quick_sort(arr, low, high):
    if low < high:
        pi = hoare_partition(arr, low, high)  # Get partition index
        quick_sort(arr, low, pi - 1)  # Sort the left partition
        quick_sort(arr, pi + 1, high)  # Sort the right partition


# Example usage:
arr = [10, 7, 8, 9, 1, 5]
print("Unsorted array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)'''






def QuickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x<pivot]
        middle = [x for x in arr if x==pivot]
        right = [x for x in arr if x>pivot]
    return QuickSort(left)+middle+QuickSort(right)
    
arr = 10,5,2,3,7,6,9,1,8,4
sorted_array = QuickSort(arr)
print("Sorted array:", sorted_array)