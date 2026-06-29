"""
1. Add a new key-value pair.
2. Update an existing value.
3. Add multiple key-value pairs.
4. Update dictionary using another dictionary.
5. Change all values to a specific value.
6. Insert a key only if it doesn't exist.
7. Add a key with a default value.
8. Merge two dictionaries.
9. Replace a value based on a condition.
10. Update nested dictionary values.
"""

""" 1. Add a new key-value pair. """
employee_dictionary = {
    "name": "Jim",
    "employee_number": 101,
    "Designation": "AI Developer",
    "joining_date": "2026-06-25"    
}

# adding values via keys
employee_dictionary['age']=24

print(employee_dictionary)

""" 2. Update an existing value. """
employee_dictionary.update({"age":25})
print(employee_dictionary)

""" 3. Add multiple key-value pairs. """

employee_dictionary.update(blood_group='A +ve', marital_status='Single')


""" 4. Update dictionary using another dictionary."""

address_dict = {
   "street": "123, Gama Street",
   "city": "Chennai",
   "State": "Tamil Nadu",
   "Pin": "621216",
   "Country": "India"
}

employee_dictionary.update(address_dict)
print(employee_dictionary)

""" 5. Change all values to a specific value"""

my_dict = {"orange": 20, "apple": 10, "lichy": 10}

for k, v in my_dict.items():
    my_dict[k]=10
    
print(my_dict)

"""6. Insert a key only if it doesn't exist."""

k = "Cherry"
v = 40

if k not in my_dict:
    my_dict[k]=v
    
print(my_dict)


"""7. Add a key with a default value."""

my_dict.setdefault("grapes", 10)
print(my_dict)

"""8. Merge two dictionaries."""

dict1 = {"name": "Peter"}
dict2 = {"age": 20}

dict1 |= dict2
print(dict1)

dict3 = {"name": "Shreya"}
dict4 = {"age": 21}

merged = dict3 | dict4
print(merged)

dict5 = {"name": "Sharan"}
dict6 = {"age": 22}

merged1 = {**dict5, **dict6}
print(merged1)

"""9. Replace a value based on a condition."""
for k, v in my_dict.items():
    if v==10:
        my_dict[k]=20
print(my_dict)

"""10. Update nested dictionary values."""
data = {"user": {"id": 101, "info": {"name": "Alice", "role": "Admin"}}}

# Updates "role" and adds "status" inside the "info" dictionary
data["user"]["info"].update({"role": "Superadmin", "status": "active"})

print(data)