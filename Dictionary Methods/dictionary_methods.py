"""
1. Use copy() to create a copy.
2. Compare shallow copy and original dictionary.
3. Create a dictionary using fromkeys().
4. Use setdefault().
5. Use update() method.
6. Find the maximum key.
7. Find the minimum key.
8. Find the maximum value.
9. Find the minimum value.
10. Check if two dictionaries are equal.
"""
"""1. Use copy() to create a copy. """
stocks={"orange": 10, "grapes": 20, "cherry": 30, "lichy": 25}
copied = stocks.copy()

print(copied)

"""2. Compare shallow copy and original dictionary. """
stocks["dates"]=40

print(stocks)
print(copied)

"""3. Create a dictionary using fromkeys(). """
keys = ["a", "b", "c"]
values = 0

alphabets = dict.fromkeys(keys, values)
print(alphabets)


"""4. Use setdefault(). """
print("understanding get", stocks.get("plum", 20))
print("get", stocks)
print("understanding setdefault", stocks.setdefault("plum", 20))
print(stocks)

"""5. Use update() method. """
stocks.update({"guava": 15})
print(stocks)

"""6. Find the maximum key. """
numbers = {1:1, 2:2, 3:3, 40:4}
max_key = 0
for k, v in numbers.items():
    if k > max_key:
        max_key = k
print(max_key)

"""7. Find the minimum key. """
numbers = {1:1, 2:2, 3:3, 40:4}
keys = []
for k, v in numbers.items():
    keys.append(k)
    
print(min(keys))

"""8. Find the maximum value. """
numbers = {1:1, 2:2, 3:3, 40:4}
values = []
for k, v in numbers.items():
    values.append(v)
print(values)
print(type(values))
print(max(values))
"""9. Find the minimum value. """
print(min(values))

"""10. Check if two dictionaries are equal. """
dict_a = {"apple": 1, "banana": 2}
dict_b = {"banana": 2, "apple": 1}

print(dict_a == dict_b)