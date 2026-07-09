"""
1. Count frequency of characters in a string.
2. Count frequency of words in a sentence.
3. Count occurrences of numbers in a list.
4. Find the most frequent element.
5. Find the least frequent element.
6. Count vowels in a string using a dictionary.
7. Count uppercase and lowercase letters.
8. Count positive and negative numbers.
9. Create a histogram using a dictionary.
10. Count duplicate values in a dictionary.
"""

"""1. Count frequency of characters in a string. """
string = "hello world"
frequency = {}
for char in string:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char] = 1
print(frequency)

"""2. Count frequency of words in a sentence."""
sent = "Python is a programming language. Python is fun and easy to learn"
word_freq = {}
for word in sent.split():
    if word in word_freq:
        word_freq[word]+=1
    else:
        word_freq[word] = 1
print(word_freq)

""" 3. Count occurrences of numbers in a list."""
list_of_numbers = [1, 1, 1, 2, 2, 3]
frequency_of_numbers = {}
for number in list_of_numbers:
    if number in frequency_of_numbers:
        frequency_of_numbers[number]+=1
    else: 
        frequency_of_numbers[number]=1
print(frequency_of_numbers)

# approach 2: 
count = {}
for num in list_of_numbers:
    count[num]= count.get(num, 0)+1
print(count)

"""4. Find the most frequent element."""


"""5. Find the least frequent element."""

"""6. Count vowels in a string using a dictionary."""

"""7. Count uppercase and lowercase letters."""

"""8. Count positive and negative numbers."""

"""9. Create a histogram using a dictionary."""

"""10. Count duplicate values in a dictionary."""