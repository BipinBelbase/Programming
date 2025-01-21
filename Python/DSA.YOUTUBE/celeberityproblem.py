# solving celebety problem using stack
#stack
from stack import stack

# you are given a array
# 0 is  A  and 1 is b and 2 is c and 3 is d 
# so 0 means dont know and 1 means knows ..\
# so celebrety is who  dont know anyone or all people know him .... 2 possibility
# we solve using stack ..  
# we maek 2 array and 

list =[
         [0,1,1,1],
         [0,0,1,1],
         [0,0,0,0],
         [0,0,1,0]
      ]
#search for one person .. all others know him .. 
def knows(a,b):
            
            return list[a][b]==0
    
   
      

firststack = stack(list)

for i in list:
    firststack.push(i)

#....................

while len(stack)>1:
    a = firststack.pop()
    b = firststack.pop()
    if knows(a,b):
           firststack.push(b)
    else:
           firststack.push(a)

lastperson = firststack.pop()




    # Verify: Candidate must satisfy both conditions
for i in range(len(list)):
    if i !=lastperson:
        if knows(lastperson, i) or not knows(i,lastperson):
            print("No celebrity found.")
        
print(f"Celebrity is person {lastperson}.")