
#error stage
#during compilation -> syntax Error
#when converting from human readable format to machine language .... it detect error...

#during execution -> Exceptions
#when compilation is completed it converted into machine language but now when execution or running it give us error ... so it called exceptions .. so we have to handel exceptions





#Syntax Error

#code not written in according to the program grammar, error is raised by interpreter/compiler
#example of syntax error
# print 'hello world' 
#missing colon , bracket misspling keyword , incorrect indentation , empty if/else, class, funcion


#indexError 
#index error -->when trying to access an item at an invalid index.


#ModuleNotFoundError 
#when module not found 
#import mathee 


#keyError
#the keyerror is thrown they key is not found like in dictionary...


#TypeError
#like inappropriate error
#1 + 'a'
# not expected data type


#ValueError
#when function argument is of an inappropriate type
#int is a function
#int('a')



#nameError
#print(k)


#AttributeError
#l = [1,2,3]
#l.upper()
#attribute(data) doesnot exist in this type of function like upper is not not list attribute .. is the string atributes








#Exception .................
#it raised by python runtime
#when something goes wrong in execution or runtime 
# examples
# a = 1 , b = 0, a/b
#gramatically written well but give the error on execution
#memory overflow
#database Error



# #Exception Handeling 

# #using Try except block
# #Try
# #except

# with open('sample.txt','w') as f:
#     f.write('hello world')
    

# #what if we write sample111.txt instead of sample.txt .... so we dont want to show all pythonic error .. so we make custume message when , something goes wrong it show out message , simple
# try:
#     with open('sample111.txt','r') as a:
#          print(a.read())
# except:
#     print('sorry file not found')



#..we can detect multiple errors also  



try:
    with open('sample.txt','r') as a:
         print(a.read())
         print(m)
#now we write different error message for different error wiith multiple except command and error name 
except FileNotFoundError:
    print('sorry file not found')

#if  name error occured then
except NameError:
    print('variable not defined') 
#exception error or exception means something error in while executing code
#we can also set exception as e (e is object of exception error) now using ....
except Exception as e:
    print(e.with_traceback)

#we also have else   
# Try

#except

#else
#when there is no error in except funcions . then else bluck runs.. runs when no error in except

#finally
#it runs even when it gets error .. anyhow it will runs ,, it will runs anytime .. error or noerror ...... 
#when in file error comes it goes to it goes to except 
#when in file no error it goes to else
#when in file anything happened finally runs ....




#raise Exception (raise error )
#we can throw an error or custom error
# raise NameError('aise hi try kar raha hu')

#any error we can throw custume

#we can make custume exceptions 