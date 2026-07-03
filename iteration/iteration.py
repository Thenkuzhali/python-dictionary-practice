"""
1. Iterate through all keys.
2. Iterate through all values.
3. Iterate through key-value pairs.
4. Print keys in sorted order.
5. Print values in sorted order.
6. Count the number of items while iterating.
7. Print only keys whose values are even.
8. Print only values greater than 50.
9. Iterate through a nested dictionary.
10. Create a new dictionary while iterating.
"""

"""1. Iterate through all keys. """
user = {"name": "Priya", "age":25, "role": "Developer", "city": "Chennai" }

for k in user.keys():
    print(k)
    
"""2. Iterate through all values. """

for v in user.values():
    print(v)

""" 3. Iterate through key-value pairs. """
for k, v in user.items():
    print(k, v)

"""4. Print keys in sorted order. """
for k in sorted(user.keys()):
    print(k)
    

"""5. Print values in sorted order."""
alphabets = {"b": 2, "a": 1, "c": 3, "d": 4}
for v in sorted(alphabets.values()):
    print(v)

"""6. Count the number of items while iterating. """
for count, (k, v) in enumerate(user.items(), start=1):
    print(f"count of items: {count} | key={k}, val={v}")
    
for c, k in enumerate(user.keys(), start=1):
    print(f"count of keys: {c} | key={k}")
        
for c, v in enumerate(user.values(), start=1):
    print(f"count of values: {c} | value={v}")

"""7. Print only keys whose values are even. """
for k, v in alphabets.items():
    if v%2==0:
        print(k)

"""8. Print only values greater than 50. """
stocks = {"pen": 50, "pencil": 100, "Eraser": 20, "Sharpner": 55}
for k, v in stocks.items():
    if v>50:
        print(k)

"""9. Iterate through a nested dictionary. """
nested_user = {
    "user1": {"name": "Alice", "age": 25, "role": "admin"},
    "user2": {"name": "Bob", "age": 30, "role": "editor"}
}

for user_id, profile in nested_user.items():
    print(f"user_id:{user_id}, profile: {profile}")
    for key, val in profile.items():
        print(f"key: {key}, val:{val}")


"""10. Create a new dictionary while iterating. """
new_alphabets = {k: v for k, v in sorted(alphabets.items())}

print(new_alphabets)