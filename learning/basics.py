#1 Create two variable - one with your name and one with your age
#user_name = 'Alan'
#user_age = 29
user_name = input('Enter your name: ')
user_age = input('Enter your age, too: ')

#2 Create a function which prints your data as one string
def print_user_data():
    """Prints the user name (uses global variables!)"""
    print(user_name + ' - ' + user_age)

print_user_data()

#3 Create a function which prints ANY data (two arguments) as one string
def print_concatenated_data(el1, el2):
    """Print two concatenated strings.
    
    Arguments:
        :param el1: The first string to be concatenated.
        :param el2: The second string to be concatenated.
    """
    print(el1 + ' - ' + el2)

print_concatenated_data(user_name,user_age)

#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def calculate_decades(age):
    """Calculates the integer part of the age received.
    
    Arguments:
        :param age: The age for which the decades should be calculated.

    Returns the decades lived.
    """
    decades_lived = age // 10
    print(decades_lived)

decades = calculate_decades(int(user_age))
print(decades)

"""
Data Types
    Numbers (Integers & Floats)
    Strings
    Booleans

Operators
    Base Arithmetic +,-,*,/
    Modulus: %
    Floor division: //
    Power: **
    Strings can be added and
        multiplied (with Integers)

Lists
    Create Lists
    Add Items via append()
    Access Items via Index
        (which starts at 0!)
    Other List Operations
        (pop(),...)
    
Functions
    Use Indentation and : to define Code Block
    Can use Arguments
    Can return Values
    Can use Default Arguments
    Keyword Arguments allow you to re-order or skip arguments
"""