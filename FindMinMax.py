def find_min_max(arr, low, high):
    if low==high:
        return arr[low], arr[high]
    elif high==low+1:
        if arr[low]<arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    else:
        mid=(low+high)//2
        left_min, left_max=find_min_max(arr, low, mid)
        right_min, right_max=find_min_max(arr, mid+1, high)
        return min(left_min,right_min), max(left_max,right_max)

arr=[3,5,1,8,2,7,6,4]
min_val, max_val=find_min_max(arr, 0, len(arr)-1)
print(f"min:{min_val}")
print(f"max:{max_val}")        
    