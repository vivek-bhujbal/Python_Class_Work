# A dictionary is a built-in data structure in Python that allows you to store
# a collection of key-value paris.

#dictionary is mutable and it is unordered

my_dict = {
            "stud_id":1001,
            "stud_name":"Vivek",
            "course":"BCA"
}
print(my_dict)

#Accessing Elements

x=my_dict["course"]

print(x)

x=my_dict.get("stud_name")

print(x)


# Get all the keys from specified dictionary
y=my_dict.keys()
print(y)


# To update particular value

my_dict.update({"stud_name":"Vivek"})
print(my_dict)

# adding items in the dictionary

my_dict["fees"]=45000
print(my_dict)

my_dict["stud_add"]="Navi Mumbai"
print(my_dict)


# removing items in the dictionary using pop()

my_dict.popitem()
print(my_dict)

# looping over dictionary

for i in my_dict:
    print(i)

# looping over items in list
for i in my_dict:
    print(my_dict[i])


# looping by the method values() and keys()
print("Use of values() method")
for i in my_dict.values():
    print(i)


print("Use of keys() method")
for i in my_dict.keys():
    print(i)


# traversing dictionary
for x,y in my_dict.items():
    print(x,y)



