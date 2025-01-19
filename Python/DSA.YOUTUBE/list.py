#efficiency in programming
#how can we canculate efficiency in programming
#we can calculated using two ways ..two method
#1. Time complexity
#2. Space(storage) complexity

#lets start 
#Time Complexity or Time Efficiency 
#technique 
#a. measurint with time
#b. counting with operations 
#c. order of groth

#a. this method is not used in market because it depent on the computer because of different processor used by user so this method is not good way, also even logic is same using different method different time, and we cannot make relation with input ...XXXXXXXXXXXXX
# import time
# start = time.time()
# for i in range (1,101):
#     print(i)
# print(time.time()-start)

#b. counting operation this is also not good because .
# time varies if implementation changes
#no clear definition of which operation to count
#cannot establish relation 
# def c_to_f(c):
#   return c*9.0/5 + 32 
# so this give 3 operation


#c . Orders of Groth
#best and used in all places
#goals
# evaluate programs efficincy when input is very big
# we want relationship between input and time 
# the growth of programm's runtime as input size grows
#do not need precise . we want "order of" not "exact" growth
#we will look at largest factors in time or worse case factor 

# we calculate using big O notation 
# O()
# def fact_iter(n):
    #answer =1
    #while n>1:
    #answer*=n
    #n-=1
    #return answer
# we will do count operation in the 1+5n
#now remover 1 and 5 
#O(n)
#when input grows time grows
#n2 + 2n + 2
# n2 is nested loop
#2n is 2 operation inside loop 
# 2 is outside loop 2 operation
# now we do 
#remove 2 and 2 so n2 +n now also have to remover n because we look the largest factor 
# so time complexity is n2
# O(n2)
# when time grows input grown n times , times grows n2
# n is input and O n2 is the time complexity so O(n2)
# order of growth is 6 
# constant o(1)
#not depent on input
# liner o(n)
#when input icrease time increase
#quadratic
# double the input square 
#O(n2)
#logarithmic log n
# output slowly increase 
# after constant logarithmic is best
#binary search
# nlogn
# exponential
# not good 
# 2^n



# NOW LETS START WITH PRACTICE QUESTIONS


#lets create out own list
# use use C-programming data type ungin c type
import ctypes

class MeroList:

    def __init__(self):
        self.size = 1 # size of array , initially start with one .. if someone make array it would be the 1
        # we will make array size double each time like
        # 1 , 2 , 4 , 8 , 16 .... so we dont have to make another arry eacdh time list cnanged .. 
        # like if size of array is 16 we can stored 16 things there but when n or size of actually values became equal to the size ..
        # then we have to make another array size of double i.e 32 and store that old value and then we can add things there others stuff also
        # arr have  1,2,3
        # arry size is specific like 8 bit size like 8+8+8+8+ so on not 1 by one 
        # if we want to store 1,2,3 it created 8 size array but only stored the 1,2,3 and again if we add another one we dont have to make another array , until 8 after watd again we make array of size 16 thne so on like; this
        # we have 5 space but we only used 3
        # we did not make 
        # but in python every time new array is created in new memory location ,,, 
        self.n = 0 #  real items in array actually we have.we can have the array size of 8 but store only 5 items in it 
        # create a C type array with size =  self.size

        self.A = self.__make_arary(self.size)



    def __make_arrar(self,capacity):
        # creates a c type array(static, referential) with size capacity
        return (capasity*ctypes.py_opject)()
    
    def __len__(self):
        return self.n
    #self.n is actually values stored in list .. list can be big but value in it is not

    
    #adding append function of list
    def append(self,item):
        #check if vacant yes or not .. if no . resize ..
        # if value became eqqual to size of arry it means arry full with values so we make another list
        # and we will do append in the A[n] because n is the vacant 
        # like if size is equal it means no size available so we have to make another array
        if self.size == self.size:
            #resize addddddddddddddd
            self.__resize(self.size*2)



        # after resize we do append 
        self.A[self.n] = item
        self.n = self.n + 1
    
    def resize(self,new_capacity):
    
        self.__make_array(new_capacity)
        self.size = new_capacity

        #copythe content of A to B 
        for i in range(self.n):
            B[i] = self.A[i]

            #reassign A
            self.A = B 
    def __str__(self):
        restul = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
            
            return '['+result[:-1]+']'
        
    def __getitem__(self,index):
        if 0<= index < self.n :
            return self.A[index]
        else:
            return 'IndexError-Index is out of range'
        

    # do it by yourself
    # POP list(pop)
    # last items in list is n-1
    #clear --reset size and n
    #find-- index---loop until that item , if found break and return the index
    #insert
    #delete --- delete by index
    #remove --- remove by value
    # sort / min / max/ sum/ extend / negative/ indexing/ slicing/ merge self do 