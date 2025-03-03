def isSafe(matrix,row,i):
    for j in range(len(matrix[row])):
        if matrix[row][j] == 'Q':
            return False
        if matrix[j][i] == 'Q':
            return False
    for i , j in zip(range(row,-1,-1),range(i,-1,-1)):
        if matrix[i][j] == 'Q':
            return False
    for i , j in zip(range(row,-1,-1),range(i,len(matrix))):
        if matrix[i][j] == 'Q':
            return False
    return True
    
def function(matrix,row = 0):
    if (row == len(matrix)):
        return True
    for i in  range(len(matrix[row])):
        if isSafe(matrix,row,i):
           matrix[row][i] = 'Q'
           if function(matrix,row+1):
               return True
           matrix[row][i]='--'


num = 4
matrix = [['--']*num for i in range(num)]
function(matrix)
for i in range(len(matrix)):
        print(matrix[i])