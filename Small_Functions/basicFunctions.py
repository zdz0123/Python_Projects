"""
some basic functions in python
"""

// is_even function
"""
If x is even, then return True. Otherwise, return False.
"""

def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False


// is_int function
"""
Have it return True if the number is an integer (as defined above) and False otherwise.
"""

def is_int(x):
  if x - round(x) == 0:
    return True
  else:
    return False
    
    
// digit_sum function
"""
Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.
"""

def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
    return total
    
 
// factorial function
"""
Return the factorial of number x
"""

def factorial(x):
  result = 1
  for i in range(1, x+1):
    result = result * i
  return result
  
  
// is_prime function
"""
Check a number is a prime or not
"""

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True
        
        
// reverse function
"""
Define a function called reverse that takes a string textand returns that string in reverse. 
"""

def reverse(text):
  reverse = ""
  for x in range(len(text) - 1, -1, -1):
    reverse += text[x]
  return reverse
  
  
// anti_vowel function
"""
Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
"""

def anti_vowel(text):
  vowel = "aeiouAEIOU"
  for char in vowel:
    text = text.replace(char, "")
  return text
  
  
// scrabble_score function
"""
Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.
"""

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  result = 0
  for char in word:
    char = char.lower()
    result += score[char]
  return result
  
  
// censor function
"""
It should return the text with the word you chose replaced with asterisks. 
"""

def censor(text, word):
    words = text.split()
    result = ""
    stars = "*" * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result = " ".join(words)

    return result
    
    
// count function
"""
Return the number of times the item occurs in the list.
"""

def count(sequence, item):
  count = 0
  for num in sequence:
    if num == item:
      count += 1
  return count


// purify function
"""
Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
"""

def purify(numbers):
  for i in range(len(numbers)-1, -1, -1):
    if numbers[i] % 2 != 0:
      del(numbers[i])
  return numbers
  
  
// product function
"""
Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.
"""

def product(numbers):
  product = 1
  for num in numbers:
    product = product * num
  return product


// remove_duplicates function
"""
Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.
"""

def remove_duplicates(origin):
  result = []
  for i in origin:
    if i not in result:
      result.append(i)
  return result
  
  
// median function
"""
Write a function called median that takes a list as an input and returns the median value of the list. 
"""

def median(numbers):
  numbers = sorted(numbers)
  if len(numbers) % 2 != 0:
    return numbers[len(numbers) / 2]
  else:
    return (numbers[len(numbers) / 2] + numbers[len(numbers) / 2 - 1]) / 2.0
