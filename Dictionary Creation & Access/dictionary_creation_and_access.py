'''
Dictionary Creation & Access
1. Create an empty dictionary.
2. Create a dictionary with employee details.
3. Access a value using a key.
4. Print all keys in a dictionary.
5. Print all values in a dictionary.
6. Print all key-value pairs.
7. Check if a key exists in a dictionary.
8. Get a value using get().
9. Access a nested dictionary value.
10. Print the length of a dictionary.
'''

""" 1. Create an empty dictionary """

my_dict = {}
my_dict_2 = dict()

""" 2. Create a dictionary with employee details. """
employee_dictionary = {
    "name": "Jim",
    "employee_number": 101,
    "Designation": "AI Developer",
    "joining_date": "2026-06-25"    
}

# add values via keys
my_dict["name"] = "Sara"

# .update() is used to update the dictionary. we can update another dict into a dict 

my_dict.update({"age": 25})

print(my_dict)

""" 3. Access a value using a key. """

print(employee_dictionary["name"])

for k,v in employee_dictionary.items():
    print(v)
    
res = {v for k,v in my_dict.items()}
print(res)

""" 4. Print all keys in a dictionary. """
for k,v in employee_dictionary.items():
    print(k)
    
print(my_dict.keys())

"""6. Print all key-value pairs."""

print(my_dict)

print(employee_dictionary)

"""7. Check if a key exists in a dictionary."""

for k,v in employee_dictionary.items():
    if k in "name":
     print("exists,", k)
     
print("name" in my_dict)

""" 8. Get a value using get(). """

print(my_dict.get("age"))

""" 9. Access a nested dictionary value."""

inventory = {
    "fruits":{
        "orange":10, 
        "apple": 10
        },
    "vegetables":{
        "potato":20,
        "brinjal":15
    }
}

for k,v in inventory.items():
    for p,q in v.items():
        print(q)
        
print("orange=", inventory["fruits"]["orange"])

"""10. Print the length of a dictionary."""
print("len of my_dict:", len(my_dict))
print("len of employee_dict:", len(employee_dictionary))
print("len of inventory:", len(inventory))