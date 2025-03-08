#sericliazation and Deserialiazation and json pickle
#why serialiazation needed
#we can only read or write text or binary data in normal file handelling
#we cannot read write (using JSON >> list , dictionary )(using pickling >> tuple , object ddclasses , custom class)
# In Conclusion :
# normal file handeling : Plain text or binary(picture) [problem: cannot do list dic , c object , tuple]
# JSON file handelling : list , dictionary ,(only serialiazation of custome object, DEserialiaztion not work ) (we can do tuple but it goes only serialize list )
# Pickling : tuple , custome object , (serialiazation and deserialiazation )

import json

#1
#serialiazation using JSON module
# L = [1,2,3,4]
# example = '/home/bipin/Programming/Python/Practice/json.demo'
# with open(example,'w') as f:
#     json.dump(L,f)


# #2
# #We can't write complex thing in normal text .. like dictionay , list so on  ... so we can do it by using json
# example = '/home/bipin/Programming/Python/Practice/json.demo'
# d = {
#     'name':'nitish',
#     'age':33,
#     'gender':'male'
# }

# with open(example, 'w') as f:
#     json.dump(d,f,indent=4)




# #3
# # deserialization
# #this is why we use json 
# #dictionary type
# example = '/home/bipin/Programming/Python/Practice/json.demo'
# with open(example, 'r') as f:
#     d = json.load(f)
#     print(d)
#     print(type(d))




#Now lets say we want to pass custom object(class) ..  we can serialize it using json but we cannot deserialiaze it ....... lets see how serialiazation work  and how can we solve deserialiazation problem using pickling 
#first lets do sesrialiazation of custome object using json 


# #this will not work , python dont know how to serialize ,, so we have to tell python how to serialize this custome object 
# class PersonDetail:

#     def __init__ (self,fname,lname,age,gender):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.gender = gender

# person = PersonDetail('Bipin','Belbase', 23 ,'male')

# #lets serialiaze it in dictionary

# with open('demo.json','w') as f:
#     json.dump(person,f)







# # Now we have to tell python how it can be serialize 
# #we have to make function to tell 
# class PersonDetail:

#     def __init__ (self,fname,lname,age,gender):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.gender = gender

# person = PersonDetail('Bipin','Belbase', 23 ,'male')

# #lets serialiaze it in dictionary proper way 

# def show_object(person):
#     #first check is person object is PersonDetail class
#     if isinstance(person,PersonDetail):
#         return {'name':person.fname + ' '+ person.lname ,'age':person.age,'gender':person.gender}

# with open('demo.json','w') as f:
#     #Now we have to tell how object can be shown
#     json.dump(person,f,default= show_object,indent = 4)


# #now lets do deserialiazation 
# with open('demo.json','r') as a:
#     b = json.load(a)
#     print(b)
#     print(type(b))



#what we have did is we have print the custom object in different method like dic or custom 
# But what if we want to print exact custom object as it is
#WE CANNOT DO SO WE HAVE TO USE PICKLING


#PICKLING 
# its process of converting any object into binary form so we can transfer in different files 
# so we can use object AS IT IS 


class Person:

    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print('hi my name is ',self.name,'and I am ',self.age,'year old')
#object
p = Person('bipin',25)


#we have to import pickle
#we do in binary form
import pickle
with open('person.pkl','wb') as f:
    pickle.dump(p,f)




#Now we can use that object as it is 

with open('person.pkl','rb') as a:
    c = pickle.load(a)

#remember last time we make p object .. but now we are excessing using c 
c.display_info()