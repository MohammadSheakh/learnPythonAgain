print("#////////////////////////////////////////////////////////////// 10. While Statement ..........")


# while 1==1 :
#     print("help me please")
"""
name = ""
while len(name) == 0 :
    name = input("Enter your name : ")
print(name)

name = None # same thing different way
while not name:
    name = input("Enter your name : ")
print(name)

"""

print("#////////////////////////////////////////////////////////////// 11. For Loop ..........")

for i in range(10):
    print(i+1)

print("------------------------")
for i in range(50, 72+1): # inclusive, exclusive # third argument for step ..........
    print(i)

print("------------------------")
for i in range(50, 60, 3):# third argument for step ..........
    print(i)
for i in "Bro Code":
    print(i) # each letter will be printed # prottek ta letter niye amra kaj o korte parbo

# amra time niye kaj korbo
import time
for seconds in range(10, 0, -1) : # which means 10 theke 0 te back korbe .. count down hobe
    print("seconds : ", seconds)
    time.sleep(0.000001) # 3 second er jonno sleep korte chai

print("New Year Baby ! ")

rows = 3
columns = 3
symbol = "#"
for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # , end="" # new line print na korar jonno eta likhte hobe
    print() # printing new line

print("#////////////////////////////////////////////////////////////// 12. Loop Control Statement..........")

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as placeholder

# while True:
#     name = input("Enter Name : ")
#     if name != "":
#         break
# print("your name : ", name)
# print("----------------------------------------")
# phone_Number = "32323-323"
# print("phone number : ", end="")
# for i in phone_Number:
#     if i == "-":
#         continue # mane hocche i jokhon "-" .. tokhon amra kichu korbo na .. mane print korbo na
#     print(i, end="") # otherwise amra index gula print korte chai .. mane ultimately "-" chara baki gula
print("-----------------------------------------")
for i in range(1, 12):
    if i == 2 :
        pass
    else:
        print(i, " ", end="")

print("#////////////////////////////////////////////////////////////// 13. list..........")

# list = used to store multiple items in a single variable

food = "pizza"
food = ["food", "boom", "hotcat", "chill"]
print (food)
# to access a certain element of this list , we have to use index
food[2] = "hei man"
print("food of 2nd index : ", food[2])
print("all of the element in list  : ",end=" ")
for x in food:
    print( x, end=" ")
print()
print("#////////////////////////////////////////////////////////////// 14. few useful function of list..........")

food.append("appeded food") # last e add hoy
food.remove("hei man") # for remove a value
food.pop() # pop remove the last element
food.insert(0, "cake") # jekono index e list e value add kora jabe ..
food.sort()

print(food)
food.clear()
print(food)

print("#////////////////////////////////////////////////////////////// 15. 2D list in python..........")

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hot cat", "hot dog"]
dessert = ["cake", "ice cream"]
# add all of these list into one list
food = [drinks, dinner, dessert]
print("print all merged food together : ", food)
print("print first list by index : ", food[0])
print("print first list first element by index : ", food[0][0])


print("#////////////////////////////////////////////////////////////// 16. tuples..........")

# tuple = collection which is ordered and unchangeable can have duplicate value
#                   used to group together related data

student = ("Bro", 21, "male")
print("how many times bro appear in that tuple : ", student.count("Bro"))

print("find index of a value : ", student.index("male"))

# you can display all of the contents within a tuple using a for loop
print("all content in tuple : ", end="")
for x in student:
    print(x, end=" ")

print("")
# also we can check to see if a certain value exist within our tuple
if "Bro" in student:
    print("Bro is here !!!!")


print("#////////////////////////////////////////////////////////////// 18. set..........")

# set = collection which is unordered, unindexed . No duplicate value, unique

utensils = {"fork", "spoon", "knife"} # print korle order same thakbe na
for x in utensils:
    print(x)
# set is actually faster than list .. if you need to check to see if something
print("-------------------same order e kintu print hoy nai -----------------------------")
dishes = {"bowl", "plate", "cup", "knife"}

print("utensils : ", utensils)
print("dishes : ", dishes)
utensils.add("napkin")
print("utensils after adding napkin : ", utensils)
utensils.remove("fork")
print("utensils after removing fork : ", utensils)
# utensils.clear()
# print("utensils after clear everything : ", utensils)
print("dishes before updating with utensils : ", dishes)
dishes.update(utensils) # ek ta set er moddhe arekta set ke insert kora ..
print("dishes after updating with utensils : ", dishes) # shob value unique , no duplicate value

dinner_table = utensils.union(dishes) # all unique ... duita set join kore , new set create kora


print("dishes    : ", dishes)
print("utensils : ", utensils)
print("dishes.difference(utensils)   : ", dishes.difference(utensils)) # dishes er moddhe emon ki ki ase .. jegula utensils e nai
print("utensils.intersection(dishes) : ", utensils.intersection(dishes)) # duitar moddhe common kon gula

print("utensils.union(dishes) -> dinner table : ", dinner_table)


print("#////////////////////////////////////////////////////////////// 19. Dictionary..........")

# Dictionary = A changeable, unordered collection of unique key : value pairs
#            very fast , because they use hashing, allow us to access a value quickly

# onek ta set er motoi
capitals = {
    "USA" : "Washington",
    "BD" : "Dhaka",
    "China" : "Beijing",
}
print("capital of china : ",capitals["China"])
# dictionary te kono element ase kina , sheta check korar jonno get method ase
print("is germeny is the dictionary ? :", capitals.get("Germany")) # if it returns none, then it is not into that dictionary

print("print only the keys of dictionary : ", capitals.keys())
print("print only the values of dictionary : ", capitals.values())
print("print both keys and values of dictionary : ", capitals.items())

# for loop use koreo print kora jay ...

for key, value in capitals.items():
    print(key, value) # prottek bar ekta kore key value ashbe ..

# update method er maddhome amra dictionary change korte pari ..
capitals.update({"Germeny" : "Berlin"})
print()
for key, value in capitals.items():
    print(key, value)

# now change a value of existing one
capitals.update({"USA" : "New Value"})

print()
for key, value in capitals.items():
    print(key, value)

# use POP method to remove a key value pair ...
capitals.pop('China') # taile china er key value pair remove hoye jabe ..

print()
for key, value in capitals.items():
    print(key, value)

capitals.clear() # this will clear my dictionary

print("#////////////////////////////////////////////////////////////// 20. Index Operator..........")

# index operator [] = gives access to a sequence's element(str, list, tuples)
# String, List , Tuples e index operator use kora jay

name = "bro Code!"
if (name[0].islower()):
    name = name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]
print("first name, last name, last character : ",first_name, last_name, last_character)

print("#////////////////////////////////////////////////////////////// 21. Function ..........")

# function = a block of code which is executed only when it is called

def hello(first_name, last_name, age):
    # pass
    print("calling hello function : ", first_name, last_name, age)
hello("Bro", "Code", 32)




















