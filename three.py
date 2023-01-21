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
print("Hello, my name is {:<10} Nice to meet you".format(name)) # right side padding # left align
print("Hello, my name is {:>10} Nice to meet you".format(name)) # left side padding # right align
print("Hello, my name is {:^10} Nice to meet you".format(name)) # overall padding # center align

# positional argument ar keyword argument er bepar thakle , colon er age sheta boshate hobe

# how to format numbers
number = 3.14159
# first 2 digit
print("The number of the PI => {:.2f}".format(number)) # eta number ke round kore fele
print("The number of the PI => {:.3f}".format(number))
number = 1000

print("The number is => {:,}".format(number)) # joto 1000 place ase .. shegula te comma boshbe

print("#////////////////////////////////////////////////////////////// 29. Random ..........")

import random

x = random.randint(1, 6) # duita value e inclusive
print("x : ",x)
y = random.random() # may be 0-1 er moddhe value dey
print("y : ",y)
myList = ["rock", "paper", "scissors"]
print("myList -> ",myList)

x = random.choice(myList) # jekono ekta return kore
print("random choice from myList -> ", x)

cards = [1,2,3,4,5, "A", "d", "a"]
print("befor shuffle, cards => ",cards)
random.shuffle(cards) # shob gulai shuffle kore return kore
print("after shuffle, cards => ",cards)

print("#////////////////////////////////////////////////////////////// 30. Exception Handling..........")

# exception -> events detected during execution that interrupt the flow of a program
try :
    numerator = 5
    denominator = 0
    result = numerator / denominator
    print("result : ", result)

except ZeroDivisionError as e :
    print(e)
    print("You cant divide by zero")
except ValueError as e :
    print(e)
    print("Enter only Number Please")

except Exception :
    print("Something went wrong : -> ",Exception)
else:
    print("else block : number -> ", result)

finally:
    # kono file open thakle , sheita ei block er moddhe close kore dibo
    print("This will always execute")

print("#////////////////////////////////////////////////////////////// 31. File Detection..........")
import os
path = "G:\\ok.jpg"
if os.path.exists(path):
    print("That location is exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("That location doesn't exist ! ")
print("#////////////////////////////////////////////////////////////// 32. Reading a File..........")

try:
    print("File Reading Start : ")
    with open("text.txt") as file: # this will close the file automatically
        print(file.read())
    print("File Reading End ! ")
    print("File Close Status : ", file.closed)
except FileNotFoundError:
    print("That file was not found !")

print("#////////////////////////////////////////////////////////////// 33. Writing a File..........")

text = "We are trying to write in text file .... \n boom, we are in new line "
with open('text.txt', 'w') as file:# 2nd argument e mode bole deowa jabe .. #r for read #w for write
    # overwrite your current file
    file.write(text) # we have to create text variable
print("Writing Done !")

with open('text.txt', 'a') as file: # a -> append mode
    file.write(text)
print("Writing Done !")

print("#////////////////////////////////////////////////////////////// 34. Copying a File..........")
# copyfile() => copies contents of a file
# copy() => copyfile + permission mode + destination can be a directory
# copy2() => copy() + copies metadata(file's creation and modification times)
import shutil

shutil.copyfile('text.txt', 'copy.txt') # src.dst

print("#////////////////////////////////////////////////////////////// 35. Moving a File..........")
# same way te folder o move kora jabe ...
source = "text.txt"
destination = "E:\\Python Project\\learnPythonAgain\\test\\text.txt"
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+ " was moded")
except FileNotFoundError:
    print(source+" was not found")

print("#////////////////////////////////////////////////////////////// 36. Delete a File..........")

path = 'text.txt'
try:
    os.remove(path) # delete a file # empty folder eta diye delete kora jay na Permission error dey
    # os.rmdir(path) # delete a file or empty folder/directory
    # shutil.rmtree(path) # delete files and or folders #🟥this is very dangerous code..
        # because it will delete a directory and all files contained it ...
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("That folder contains files")
else:
    print(path+ " was deleted")



















