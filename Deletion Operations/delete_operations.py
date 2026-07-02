"""
1. Remove a key using pop().
2. Remove the last inserted item using popitem().
3. Delete a key using del.
4. Clear all dictionary items.
5. Remove multiple keys.
6. Delete keys with empty values.
7. Delete a nested key.
8. Remove duplicate values.
9. Remove keys starting with a specific letter.
10. Remove keys with values less than 10.
"""

"""1. Remove a key using pop()."""
my_dict={"Orange": 10, "apple": 20, "grapes": 25, "cherry":12}
fruit_dict=my_dict.copy()
my_dict.pop("apple")

print(my_dict)

"""2. Remove the last inserted item using popitem()."""
my_dict.popitem()
print(my_dict)

"""3. Delete a key using del."""
my_dict["apple"]=10
print("Before deletion",my_dict)
del my_dict["apple"]
print("After Deletion", my_dict)

"""4. Clear all dictionary items."""
my_dict.clear()
print(my_dict)

"""5. Remove multiple keys."""
keys_to_Keep = ["apple", "grapes"]
cleaned_fruits = {k: v for k, v in fruit_dict.items() if k in keys_to_Keep}

print(cleaned_fruits)

"""6. Delete keys with empty values."""
fruit_dict["cherry"]=""
print(fruit_dict)
cleaned = {k: v for k, v in fruit_dict.items() if v}
print(cleaned)

"""7. Delete a nested key."""
data = {"user": {"profile": {"name": "Sam", "age": 30, "status": "active"}}}
print(data)

del data["user"]["profile"]["age"]
print("after del: ",data)

del_v = data["user"]["profile"].pop("status")
print(del_v)

print("after pop: ",data)

"""8. Remove duplicate values."""
skincare_products = {"face wash": "derma-co", "sun screen": "derma-co", "moisturiser": "dot and key", "body lotion":"nivea"}

print(skincare_products)
seen = set()
cleaned_prod = {k: v for k, v in skincare_products.items() if v not in seen and not seen.add(v)}

print(cleaned_prod)

"""9. Remove keys starting with a specific letter."""

remove_starts_with_n = {}
for k, v in skincare_products.items():
    if k.startswith("f"):
        continue
    remove_starts_with_n.update({k: v})
print(remove_starts_with_n)

"""10. Remove keys with values less than 10."""
  
squares = {'1': 1, '2': 4, '3': 9, '4': 16, '5':25}
 
less_than_ten = {k: v for k, v in squares.items() if not v<10}

print(less_than_ten)