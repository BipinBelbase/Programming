

def getperm(arr,index , result ):
    if len(arr) == index:
        result.extend([arr[:]])
        return 
    
    for i in range(index,len(arr)):
    
        arr[index],arr[i] =arr[i],arr[index]
        getperm(arr,index +1,result)
        arr[index],arr[i] =arr[i],arr[index]
        

    



def perm(arr):
    
    answer = []
    if type(arr) is str:
        getperm(list(arr),0,answer)


    else:
        getperm(arr,0,answer)
    
    print(answer)

 







arr = input("what do you want to show subsets of ")

perm(arr)