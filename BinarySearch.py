def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return 1

number=[1,3,5,7,11,13,15,17,19,21]
target=13
result=binarysearch(number,target)
if result!=-1:
    print(f"target found at index {result}")
else:
    print("target not found")


