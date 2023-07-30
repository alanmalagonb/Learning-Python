#1) Create a list of names and use a for loop to output the length of each name (len() ).
names = ['Alan','Adrian','Jorge','Rodrigo','Alejandro']

for name in names:
    print(name)
    print(len(name))

#2) Add an if  check inside the loop to only output names longer than 5 characters.
print('-'*30)
for name in names:
    if len(name) > 5:
        print(name)
        print(len(name))

#3) Add another if  check to see whether a name includes a “n”  or “N”  character.
print('-'*30)
for name in names:
    if len(name) > 5 and ('N' in name or 'n' in name):
        print(name)
        print(len(name))

#4) Use a while  loop to empty the list of names (via pop() )
print('-'*30)
while len(names) > 0:
    print(names.pop())

print(names)

"""
Loops
    for: Loop through List (Iterable) Elements
    while: Loop as long as Condition is True

Boolean Operators
    ==: Are two Values Equal?
    !=: Are two Values NOT Equal?
    >: Is Value 1 greater than Value 2?
    <: Is Value 1 lower than Value 2?
    >=: Is Value 1 greater or equal than Value 2?
    <=: Is Value 1 lower or equal than Value 2?
    is: Is Value True?
    not: Is Value NOT True?

if-elif-else
    if: Check whether a certain
        Condition is Fulfilled
    else: Execute Code in Case
        Condition is NOT Fulfilled
    elif: Perform an additional check in
        case Condition is NOT Fulfilled
"""