#A dictionary is a built-in data structure in
#Python that allows you to store a collection
#of key_value pairs.

#dictionary is mutable and it is unordered


my_dict={
    "std_id":123,
    "std_name":"Sameera",
    "course":"BCA"
}

print(my_dict)

x=my_dict["course"]
print(x)
print("The course selected is",x)

x=my_dict.get("std_name")

print(x)

x=my_dict.get("std_id")
print(x)

#Get all the keys from specified dictionary
y = my_dict.keys()
print(y)
print("The keys present are:",y)

#to update particular value
my_dict.update({"std_name":"Sameer"})
print(my_dict)

#adding items in the dictionary

my_dict["fees"]=76000
print(my_dict)

my_dict["std_Addr"]= "thane"
print(my_dict)

#To remove certain element from the dictionary
my_dict.popitem()

print(my_dict)

#looping over dictionary

for i in my_dict:
    print(i)

#to GET keys from the dictionary
print("Use of values() method")
for i in my_dict.keys():
    print(i)
    

#to get values from the list
print("Use of keys() method")
for i in my_dict.values():
    print(i)

#travesing dictionary
for x,y in my_dict.items():
    print(x,y)

my_dict.pop("std_name")
print(my_dict)

'''WAP to create dictionaries for below task and perform all the above operations on
Each product in a supermarket is associated with its price.
Each student in a school is associated their grade.
Each customer ID in a company is associated with a customer name.
'''

































