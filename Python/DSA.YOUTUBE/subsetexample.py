

def subset(arr,newarr=[],level = 0):
    
    if len(arr) == level:
        print(newarr,end=" ")
        return 
    

    #  include in the subset
    newarr.extend([arr[level]])
    subset(arr,newarr,level+1)

    #backtracking before not include 
    newarr.pop()

    #not include
    subset(arr,newarr,level+1)



#driver code

subset([1,2])