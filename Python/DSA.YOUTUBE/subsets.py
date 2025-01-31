

#########chatgpt
#lets dry run with [1,2]
def find_subsets_iterative(listt): # two times first 1 and second time 2
    result = [[]]  # Start with the empty subset
    for i in listt: # for loop to list i.e 1 and 2 .......
        new_list = []
        for j in result: # j is the value inside result 
            new_list.append(j + [i])  # Add current number to each subset like if 1 then 
        result.extend(new_list) # one is added to result 
    return result

# Test
nums = [1,2]
print("Subsets:", find_subsets_iterative(nums))
