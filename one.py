print("boom")

print("# variable ================================================================================")

name = "Bro"
print("Hello" + name) # string add korte hoile + use korte hoy .. print korte hoile comma

print("data type of name variable : " , type(name))

age = 21
age += 1
print("age (by using comma ) = ", age) # amra jodi + diye likhte chai .. taile amader ke type casting kore nite hobe ..
# print("age = " + age) # this gives us error
print("age (after type cast and use + )= " + str(age)) # this sould works fine

height = 30.4
print("height = ", str(height), type(height))

human = True
print("human = ", human, type(human))

print("#/////////////////////////////////////////////////////////////////////////////////////////////////")
name = "Bro Code"
age = 21
attractive = True
print("name age attractive : ", name, " ", age, " ", attractive)


name , age, attractive = "big", 44, False  # using one line of code .........

print("name age attractive : ", name, " ", age, " ", attractive)

# all of the variable with same value
aa = bb = cc = dd = 3

print("aa bb cc dd : ", aa, " ", bb, " ", cc , " ", dd)


print("#========================================================== Available methods for String")

name = "bro"
print("length of String = ", len(name))
print("position of B index = ", name.find("B"))
print(name,"lets make capitalized = ", name.capitalize())
print(name,"lets make uppercase = ", name.upper(),  name.isupper(), name.upper().isupper())
print(name,"lets make lowercase = ", name.lower())
print(name,"isdigit .. return True or False = ", name.isdigit())
print(name,"isalpha ..  space thakle false = ", name.isalpha()) # space ase kina check korte isalpha use kora jabe
print(name,"name.count(\"o\") = ", name.count("o")) # o koto gula ase
print(name,"replace(\"o\", \" \") ..  o ke space diye replace korlam = ", name.replace("o", " "))
print("display string multiple time by into : ", name*3 )

print("#////////////////////////////////////////////////////////////// Type Casting in python ..........")

x = 1 # int
y = 2.0 # float
z = "3" # str
print("type cast y , float to int",y, type(int(y)), int(y))
print()
print("z*3 = 333  ::::::", z*3)
print("int(z)*3 = 9 ::::::", int(z)*3)

# name = input("what is your name ? : ") ###################### take input from user
# age = int(input("how old are you ? : "))
age += 1
print("name , age : ", name, age)

print("#////////////////////////////////////////////////////////////// Math ..........")

pi = 3.14
import math
print("round of pi : ", round(pi))
print("ceil of pi : ",math.ceil(pi))
print("floor of pi : ",math.floor(pi))
print("absolute of pi : ",abs(pi)) # return positive value
print("power of pi : ",pow(pi, 2)) # base, exponent
print("square root of pi : ",math.sqrt(pi))
x = 1
y = 2
z = 3
print("max number of x y z : ",max(x, y, z))
print("min number of x y z : ",min(x, y, z))


print("#////////////////////////////////////////////////////////////// 8. String Slicing ..........")

# indexing[] or slice() -> [start : stop : step] for indexing // step er moddhe koto kore barate chai index, sheta bole
# dite pari .. [start, stop, step]  for slice() ... just ekta te colon arekta te comma

name = "Bro Code"

first_Name = name[1] # nth index er letter print korte chaile ..

print("slicing -> ", first_Name)

first_Name = name[0 : 3] # to slice first 3 character // [inclusive (shoho) : exclusive (chara) ]

print("slicing -> ", first_Name)

first_Name = name[1 : 8  :2] # to slice first 3 character // [inclusive (shoho) : exclusive (chara) ]

print("slicing -> ", first_Name)

reversed_name = name[::-1]
print(reversed_name) # funky way to do this

website = "http://google.com" # amra may be http:// and .com alada korte chai ..
slice = slice(7, -4) # jehetu ekta link koto boro hobe amra sheta jani na .. shejonno negetive index niye
# amader kaj korte hoy ... -1 mane holo .. shob cheye right letter  er index

print("website[slice] => ", website[slice]) # it should give us .. just website name

print("#////////////////////////////////////////////////////////////// 9. If Statement ..........")

age = 12
# order matters
if age == 12:
    print("you are above 12")
elif age >= 24:
    print("you are above 24")
else:
    print("you are a child ")

print("#////////////////////////////////////////////////////////////// 10. logical operator ..........")

temp = 22
if not (temp >= 0 and temp <= 20) : # condition duita true hoile .. overall result not er karone false hobe
    # not True ke false kore ... false ke true kore
    print("temp between o-20")
elif temp >= 20 or temp <= 40 :
    print("temp between 2o-40")
else:
    print("temp between else")










