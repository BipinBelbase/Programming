def binarysearch(arr, value, start, end ):
    if start <= end:

        mid = (start + end) // 2

        if arr[mid] == value:
            return "index number : " + str(mid)

        elif arr[mid] < value:
            return binarysearch(arr, value, mid + 1, end)

        elif arr[mid] > value:
            return binarysearch(arr, value, start, mid - 1)
        
    return "NOT FOUND...."

arr = [1,2,3,4,5,6]
print(binarysearch(arr, 0,0,len(arr)-1))
print(binarysearch(arr, 7,0,len(arr)-1))

