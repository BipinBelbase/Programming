

def subsets(list,summ):
    result = []
    sumofk = []
    for i in range(2**len(list)):
        eachsubset = []
        
        for j in list:

            if i ==0:
                exit
            if i&1 :
                eachsubset.append(j)
            
            i = i>>1 
        # if sum(eachsubset) == summ:
        #     sumofk.extend([eachsubset])
            
        
        result.extend([eachsubset])

    if len(sumofk) == 0 or summ == 0:
        sumofk = "NOT FOUND IN THE SUBSETS!!!!"

    print(f"The sum subsets which is equal to {summ} is :{sumofk}")

    return result



#drive code
subset = ["coffee","donuts","time","toffee"]
sumofk = 1
print(f"the subsets of {subset} are :",subsets(subset,sumofk))
