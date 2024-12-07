#learning File handeling 
#session 10 CampusX DSMP 2022-23
#What is open ???
#open is class so we have to create OBJECT OR INTANCES for it then using function inside it like read write readlines so on 

# 1
# #using normally writing , if file doesn't exist then it created new ones , if something is already written there then it override it
# f = open('/home/bipin/Programming/Python/Practice/sample.txt','w')
# f.write('Hello world \n hi how you doin')
# #we have to close the FILE from RAM 
# f.close()


#2
# #now we don't wanna override it just want to append or add extra something
# c = open('/home/bipin/Programming/Python/Practice/sample.txt','a')
# c.write('Hello world \n hi how you doin')
# #we have to close the FILE from RAM 
# c.close()

#3
# # use WITH function so you dont have to use .close function always .. like with open('fileLocation'),'awr') as var:
# with open ('/home/bipin/Programming/Python/Practice/sample.txt','w') as abc:
#     abc.write('writing using with funcion')

#4
# #Now lets say you have 20 GB data which you need to read but you only have 8 GB RAM so how can you do that 
# # so we just load data in chunks like lets say 10000 character once in our memory RAM ,, one by one 
# #Lets imagine for now we have file sample.txt 20GB and we want to load 2 char once in out memory
# with open ('/home/bipin/Programming/Python/Practice/sample.txt','r') as abc:
#     chunk_size = 2

#     while len(abc.read(chunk_size)) > 0:
#         chunks = abc.read(chunk_size)
#         print(chunks,end='*')
        


#5
#we can also use f.tell() so it tell what is the next char gonna print from .. like output: 10 so it means next char will printed from 10 position and there is anothor function called seek .. f.seek(0) so it tell GOTO 0th position .. so if f.read(10) then seek to 0 .. then print .. it means always first 10 char will printed out..  not only 0 . we can say seek(1500) it will go to 1500 char then it goto that position then it printed from 1500 .. so like printing from anywhere ....

   
#so we can only read or write plain text or binaryds

