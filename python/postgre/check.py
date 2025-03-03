

arr = [1,2,3,4,4]


def is_sorted(arr)->bool:
    
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1] :
            return False
        else:
            is_sorted(arr[i+1:])
    
    return True





print("the return value is ",is_sorted(arr))