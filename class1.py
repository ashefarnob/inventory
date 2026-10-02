#dictionary and crud
#create
#read
#update 
#delete

#important topic
#json(javascript object notation)er sathe related this topic....
#when we connect towars the sever,json plays an important role

#they are two terminology in dictionary 1.key and 2.value
#we use curly braket for create dictionary
#python dictionaries store data in key value pairs.the are ordered and do not allow duplicate value
#mutablity

person1={
  "name":"mohtasim ashef",
  "age":30,
  "gender":"male",
  "monthly income":43
 # "age":50
}
person2={
"name":"mohtasim ashef",
  "age":30,
  "gender":"male",
  "monthly income":43

}
person3={
  "name":"mohtasim ashef",
  "age":32,
  "gender":"female",
  "monthly income":44
}
print(person1)
print(person2)
print(person3)
print(person1["name"])
print(person2["age"])
print(person3["gender"])


print(person1["age"])
#age change and update change is print
person1['age']=57
print(person1["age"])

#print(person[1]) it shows an error

#delete command
del person3['name']
print(person3)

#out
person3.pop('age')
print(person3)

# contact1=
# {
# "name":"arnob"
# "email":mohtasim.ashef@gmail.com
# "number":0934567

# }
# contact2=
# {
# "name":"asdf"
# "email":ashef@gmail.com
# "number":123456
# }




#part 3 of code

