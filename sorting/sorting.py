"""
1. Sort dictionary by keys.
2. Sort dictionary by values.
3. Sort dictionary by key in descending order.
4. Sort dictionary by value in descending order.
5. Get top 3 highest values.
6. Get top 3 lowest values.
7. Sort nested dictionaries.
8. Sort dictionary items alphabetically.
9. Sort by length of values.
10. Sort a dictionary containing string values.
"""

# 1. Sort dictionary by keys.
contact_book = {"name": "Then", "mobile": 8500085000, "email": "then@example.com"}
sort_by_key = {k: v for k, v in sorted(contact_book.items())}

print(sort_by_key)

# 2. Sort dictionary by values.

fruits = {'a': 'apple', 'b':'banana', 'd':'dragon fruit', 'c': 'cherry'}
sort_by_values = dict(sorted(fruits.items(), key=lambda item: item[1]))
print(sort_by_values)

#3. Sort dictionary by key in descending order.
reverse_sort = dict(sorted(fruits.items(), reverse=True))
print(reverse_sort)

#4. Sort dictionary by value in descending order.
reverse_sort_values = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))
print(reverse_sort_values)

#5. Get top 3 highest values.
my_dict = {'a': 10, 'b': 50, 'c': 20, 'd': 70, 'e': 15}
top_3_highest_value = dict((sorted(my_dict.items(), key=lambda x: x[1], reverse=True))[:3])
print(top_3_highest_value)

#6. Get top 3 lowest values.
top_3_lowest_value = dict((sorted(my_dict.items(), key=lambda x: x[1]))[:3])
print(top_3_lowest_value)

#7. Sort nested dictionaries.
nested_dict = {
    'A': {'score': 85, 'age': 25},
    'B': {'score': 92, 'age': 30},
    'C': {'score': 78, 'age': 27}
}
sort_by_score = dict((sorted(nested_dict.items(), key=lambda x: x[1]['score'])))
sort_by_age = dict((sorted(nested_dict.items(), key=lambda item: item[1]['age'])))
print(sort_by_score)
print(sort_by_age)

#8. Sort dictionary items alphabetically.
#9. Sort by length of values.
#10. Sort a dictionary containing string values.    