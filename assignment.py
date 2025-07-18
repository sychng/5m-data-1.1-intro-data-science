# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):

    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """

    # number is divisible by both 3 and 5 condition -> return "FizzBuzz"
    if number % 3 == 0 and number % 5 == 0 :
        return "FizzBuzz"
    
    # number is divisible by 3 condition -> return "Fizz"
    elif number % 3 == 0 :
        return "Fizz"
    
    # number is divisible by 5 condition -> return "Buzz"
    elif number % 5 == 0 :
        return "Buzz"
    
    # number is not divisible by either 3 or 5, the function should return the number itself
    else :
        return number
    
# Using the function
print(fizz_buzz(3))     # Output: 'Fizz'
print(fizz_buzz(5))     # Output: 'Buzz'
print(fizz_buzz(15))    # Output: 'FizzBuzz'

# End of Question 1


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):

    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """

    x = 0 # initialise 
    for index_numbers in numbers :
        x +=  (index_numbers**2)
        

    return x

# Using the function
print(sum_of_squares([1, 2, 3]))    # Output: 14
print(sum_of_squares([2, 4, 6]))    # Output: 56


# End of Question 2


# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):

    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """

    vowels = "aeiou"
    y = 0
    for index_count in string:
        if index_count in vowels:
            y +=  1

    return y

# Using the function
print(count_vowels("hello"))    # Output: 14
print(count_vowels("aeiou"))    # Output: 56

# End of Question 3


# Question 4

# Write a function that counts the number of repeated characters in a string.



def count_repeats(string):

    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """

    #Dictionaries
    char_count = {}    # Initialise 

    for index_char in string:
        if index_char in char_count: 
            char_count[index_char] += 1
        else:
            char_count[index_char] = 1

    z = 0
    for index_char in char_count:
        if char_count[index_char] > 1:
            z += char_count[index_char]
            
    return z


# Using the function
print(count_repeats("hello"))    # Output: 2
print(count_repeats("aeiou"))    # Output: 0

# End of Question 4




if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)