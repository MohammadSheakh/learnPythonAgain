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

name = input("what is your name ? : ")
age = int(input("how old are you ? : "))
age += 1
print(name, age)


