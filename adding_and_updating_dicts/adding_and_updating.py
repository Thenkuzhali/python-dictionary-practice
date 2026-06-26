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

