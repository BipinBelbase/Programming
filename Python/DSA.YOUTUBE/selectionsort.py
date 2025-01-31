
def selection_sort(arr):

    for i in range(len(arr)-1):
      
        print("Pass ",i+1)
        print(".............................................")
        for j in range(i+1, len(arr)):
            print(f"Comparing {arr[j]} and {arr[i]}")
          
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
             
            print(arr)
        


    return arr


listt = [1,2,3,4,5,6,7,8,9,8]
print(selection_sort(listt))