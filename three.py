print("#////////////////////////////////////////////////////////////// 22. Return State, ..........")
# return statement = Function send python values / objects back to the caller.
#                these values/objects are known as the function's return value

def multiply(number1, number2):
    return number1 * number2

x = multiply(2,3)
print(x)
print("#////////////////////////////////////////////////////////////// 23. Keyword Argument, ..........")

# keyword arguments = arguments preceded by an identifier when we pass them to a function
#        The order of the arguments does not matter, unlike positional arguments
#       Python knows the name of the arguments that our function receives

def hello(first, middle, last):
    print("first, middle, last : ", first, middle, last)

hello(last="Code", middle="Dude", first="Bro")
print("#////////////////////////////////////////////////////////////// 24. Nested Function Calls, ..........")

# nested function calls = function calls inside other function calls
#                   innermost function calls are resolved first
#                   return value is used as argument for the next outer function

num = 3.4
num = float(num)
num = abs(num)
num = round(num)
print("result by multiple line : ", num)

print("result by one line : ", round(abs(float(3.6))))

print("#////////////////////////////////////////////////////////////// 25. Scope, ..........")

# scope = The region that a variable is recognized
#            A variable is only available from inside the region it is created.
#            A global and locally scoped versions of a variable can be created .
# L => Local
# E => Enclosing
# G => Global
# B => Built-in

name = "Bro" # global scope (available inside And outside function)

def display_name():
    name = "Code" # local scope (available only inside this function)
    print("inside local scope name : ", name)

display_name()
print("outside global scope name : ", name)


print("#////////////////////////////////////////////////////////////// 26. Args, ..........")
# *args = parameter that will pack all arguments into a tuple
#            useful so that a function can accept a varying amount of arguments
# by the way tuples are iterable...
# but tuples are ordered and unChangable.. lets attemp to change one of those values
# args will accept a varying amount of positional arguments and pack them into a tuple
def add(*stuff):
    sum = 0
    stuff = list(stuff) # tuple ke ekta list er moddhe rakhlam
    stuff[0] = 0 # list bananor por .. amra change korte parbo
    for i in stuff:
        sum += i
    return sum

print(add(1,2, 3))

print("#////////////////////////////////////////////////////////////// 27. **kwargs, ..........")

# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments
# we know that dictionary means -> key value pairs
def hello(**kwargs): # keyword arguments
    print(kwargs['first'], kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end= " ")
hello(title="Mr.", first="Bro", middle="Dude", last="Code")

print("#////////////////////////////////////////////////////////////// 28. string format, ..........")

# str.format() = optional method that gives users more control when displaying output
number = 1000
print("The number pi is {:.3f} ".format(number))
print("The number is {:,} ".format(number))
print("The number is {:b} ".format(number))
print("The number is {:o} ".format(number))
print("The number is {:x} ".format(number))
print("The number is {:E} ".format(number))

animal = "Cow"
item = "moon"
print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format("Cow", "moon")) # {} are format fields
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item)) # positional argument
print("The {1} jumped over the {0}".format(animal, item)) # positional argument
print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # keyword argument
print()
text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Bro"
print("Hello, my name is {} ".format(name))
print("Hello, my name is {:10} Nice to meet you".format(name)) # right side e kichu padding add korlam ..
# jei amount of space right side e chai .. sheta bole dite hoy

















