def merge_sorted(a, b,arr):
    if a is None:  # Ensure `a` is a valid list
        a = []
    if b is None:  # Ensure `b` is a valid list
        b = []
    
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    # Add remaining elements from 'a' and 'b'
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1
    


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge_sorted(left, right, arr)

listt = [1,2,3,2,3]
print("this is the original list before changing",listt)
check = merge_sort(listt)
print("this is the return value",check)
print("this is the value after changing",listt)
