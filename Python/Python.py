import math #have to import this, so we can use the math functions

#String variable type (str); check it with print(type(variable_name_here)); chars or even complete sentences

print("Strings (str)")
first_name = "J"
last_name = "Development"
full_name = first_name + " " + last_name #combines the first and the last name
adress = "Germany"

print("Your name is " + first_name + " and you live in " + adress + ".")
print(type(first_name)) #prints the type of the variable called 'first_name'

print("Hello " + full_name) # prints the Full name
print()

#Integer variable type (int); check it with print(type(variable_name_here)); a whole number
print("Integers (int)")

age = 15
age += 1 #adds '1' to the age variable
print("You are " + str(age) + " years old") #str(age) converts the int variable to a str variable
print(type(age)) #prints the type of the 'age' variable
print()

print("Floating point number (float; decimal number)")

height = 1.70
print(height)
print(type(height)) #checks the variable type of the 'height' variable
print("You are " + str(height) + "m tall") #converts the float variable type to a string so that we can use it along with text
print()
print("boolean (true or false)")

human = True
print("Are you a human? " + str(human)) #converts the boolean variable to a str variable
print(type(human)) #prints the type of the 'human' variable

print()
print("Multiple assignment = allows us to assign multiple variables at the same time in one line of code")

#name = "John"  #normal way to assign variables
#age = 15    #normal way to assign variables
#attractive = True  #normal way to assign variables

name, age, attractive = "John", 15, True #assign multiple variables in one line of code; you have to assign them in the right order!

print(name)
print(age)
print(attractive)

print()
print("String methods")

name = "John"

print(len(name)) #prints the amount of chars in your 'name' variable
print(name.find("J")) #Finds the letter 'J' and gives us the index of it; it starts counting at 0!
print(name.capitalize()) #capitalizes the first letter of the string
print(name.upper()) #prints the string in UPPERCASE
print(name.lower()) #prints the string in lowercase
print(name.isdigit()) #prints true/false depending on if its a digit or not
print(name.isalpha()) #checks if the chars are in the alphabet, note that if you add a space its gonna be false!
print(name.count("J")) #counts how many 'J' there are
print(name.replace("o", "u")) #replaces all 'o' with 'u'
print(name*3) #prints the 'name' variable '3' times

print()
print("Type casting; convert the data type to another data type")

x = 1 #int
y = 2.0 #float
z = "3" #str

x = float(x) #converts it to a float
y = float(y) #converts it to a float
z = float(z) #converts it to a float; if we dont convert it, it will print '333' instead of '9'

print("X equals: " + str(x)) #if we dont put 'str(x)' here, it wont print it
print("Y equals: " + str(y)) #if we dont put 'str(y)' here, it wont print it
print("Z * 3 quals: "+ str(z*3)) #if we dont put 'str(z*3)' here, it wont print it 

print()
print("How to accept user input")

name = input("what is your name?: ") #accepting user input and assigning it to the variable 'name'
print("Hello, " + name) #printing the name that the user just entered
age = float(input("How old are you?: ")) #accepting user input and assigning it to the variable 'age'
print("You are " + str(age) + " years old") #printing the age of the user
age = age + 1 #adds 1 to the age the user entered
print("In one year you are going to be " + str(age) + " years old.") #prints the age + 1
height = float(input("How tall are you? (in cm) ")) #asks for the height of the user
print("You are " + str(height)+ "cm tall") #prints the height of the user

print()
print("Math functions")

pi = 3.14 #float
x = 1
y = 2
z = 3

print(round(pi)) #rounds the 'pi' variable for us
print(math.ceil(pi)) #rounds a number up
print(math.floor(pi)) #rounds a number down
print(abs(pi)) #tells you how far away a number is from 0; abs = absolute value
print(pow(pi, 2)) #multiplies the number by itself '2' times; 3.14 * 3.14
print(math.sqrt(pi)) #gives us the square root of the variable 'pi'
print(max(pi, x, y, z)) #finds the highest number
print(min(pi, x, y, z)) #finds the lowest number

print()
print("String slicing")

name = "J Development" #string we want to slice apart

first_name = name[0] #location where we want to start slicing; 0 = 'J'
last_name = name[2:] #location where we want to start and stop slicing; 2 = 'D'; empty space afer the '2:' means that it goes all the way to the end
crazy_name = name[::2] #:2 means that it only counts every 2nd char, it´s built like this: [start:stop:step]
reversed_name = name[::-1] #reverses the name

print(first_name) #prints the sliced first_name
print(last_name) #prints the sliced last_name
print(crazy_name) #prints the name that only counts every 2nd char
print(reversed_name) #prints the reversed name

website = "https://github.com/JAYC404/"

slice = slice(8,-13)

print(website[slice]) #slicing the websites name out of the url

print()
print("If statements")
age = int(input("How old are you? ")) #accepting user input

if age == 100:
    print("You are a century old!")
elif age >= 18:   #if they are over or 18 years old, it will say 'You are an adult!' and if not, it will say 'You are a child!'
    print("You are an adult!")
elif age < 0:
    print("You havent been born yet!")
else:
    print("You are a child!")

    print()
    print("Logical operators") #checks if two or more conditional statements are true or not (and, or, not)

    temp = int(input("What is the temperature outside?: "))

    if not(temp >= 0 and temp <= 30): #if the temp is over 0 and below 30, it prints this: The temperature is good today! Go outside!
        print("the temperature is bad today!")
        print("Stay inside!")
    elif not(temp < 0 or temp >30): #if the temp is below 0 OR over 30, it prints this: the temperature is bad today! Stay inside!
        print("The temperature is good today!")
        print("Go outside!")

print()
print("While loops")

name = ""

while len(name) == 0: #while the name lenght is equal to 0, it will keep asking the user to enter a name
    name = input("Enter your name: ")

print("Hello " + name)  #if the user enters a name, it´ll send a welcome message



