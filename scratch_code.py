# List are Python equalivalent of Arrays. Like Arrays they start with a index of `0.

#grocery_list = ["Milk", "Eggs", "Cheese", "Bread"]

#print("The first item on the list is " + grocery_list[0])
#print("The second item on the list is " + grocery_list[1])

# Tuples are immutable list (can't be changed). You still use brakets to set index.

#planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
#print(planets[3])

# Sets are list that can't have duplicates only unique values. They also won't come out in the 
# same order.

#random_numbers = {5, 3, 6, 5, 9, 3, 1, 6}
#print(random_numbers)

# Dictionaries are the Objects of Python they have a key:value pair and are mutable

#customer_1 = {
#    "name":"John",
#    "age":34,
#    "birthday":"March 4th"
#}
#customer_2 = {
#    "name":"Rob",
#    "age":54,
#    "birthday":"April 3rd"
#}
#print(customer_1)

#       Python Data Structure
# Structure     Format              Example
# List          ["Item1", "Item2"]  planets = ["Venus", "Earth", "Mars"]
# Tuple         ("Item1", "Item2")  flavors = ("Venus", "Earth", "Mars")
# Set           {"Item1", "Item2"}  Set = {"Venus", "Earth", "Mars"}
# Dictionay     {"key":"value"}     Names = {"name":"Robert","age":"54"}

# Multidimensional List are Arrays with other data structures inside I.E. Tuple, Set, Dictonary
# or even other list.

# weekly high and low temps.

# temps = [
#     [
#         [66,55],
#         [100,20],
#         [35,90]
#     ],
#     [
#         [45,78],
#         [80,30],
#         [95,23]
#     ]
# ]
# print(temps[0][2])
# print(temps[1][1][0])
# print(temps[1])

# If statments.

# a = 10
# b = 3
# c = 3

# if a > b:
#     print("a is greater that b")
#     if b != c:
#         print("b is not equal to c")
#     else: 
#         print("b is equal to c")
# else:
#     print("a is less than b")

# For loop

# Display the planets

# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]

# for planet in planets:
#     print(planet)

# else is ran after the loop is finished.

# singular_words = ["student", "teacher", "room"]
# for word in singular_words:
#     print(word + "s")
# else:
#     print("Done!")

# for loop with range

# for i in range(10):
#     print(i)

# enumerate is good if you need the index and the value of a list.

# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]

# for index, value in enumerate(planets):
#     print("Planet " + str(index + 1) + ": " + value)

# while loop.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# bottles = 99
# while bottles > 0:
#     print(str(bottles) + " bottles of beer on the wall.")
#     print(str(bottles) + " bottles of beer.")
#     bottles -= 1
#     print("Take one down pass it around,")
#     print(str(bottles) + " bottles of beer on the wall.")

# bot = 99 
# for i in range(99):
#     print(str(bot) + " bottles of beer on the wall.")
#     print(str(bot) + " bottles of beer.")
#     print("Take one down pass it around,")
#     bot -= 1
#     i -= 1
#     print(str(bot) + " bottles of beer on the wall.")

# Exceptions in python 

# try: Try to run this code
# except: Run this code when something goes wrong
# else: Everything went fine, so run this.
# finally: No matter what happens, run this code.

# Divide a number by Zero
# a = 7 
# b = 0
# try:    
#     print(str(a) + " divided by " + str(b) + " is " + str(a/b))
# except Exception as e:
#     print("Sorry, a problem occurred dividing the numbers.")
#     print("Error details: " + str(e))
# finally: 
#     print("But still we tried!")
# print("All done!")

# Difine the  ask funtion
# Set a default prompt value
# def ask(prompt = "Please enter a value: "):
#     if prompt.endswith(" ")
#         return input(prompt)
#     else:
#         return input(prompt + " ")
    
# Use the ask funtion to find out how many cups we want
#question = ask("How many cups do you want?")
# ask()
# print(question)

# Define the function full_name
# def full_name(first = "First",middle = "Middle",last = " Last",display = False):
#     name = first + " " + middle + " " + last
#     if display:
#         print(name)
#     return name

# print(full_name)
# # Use our newly created funcion
# full_name("Robert", "W", "Oliver", True)
# complete_name = full_name("Robert", "W", "Oliver", False)
# print(complete_name)
    
# Define the average function 
# def average(*numbers):
#     sum = 0
#     for n in numbers:
#         # Add n to sum
#         # (+= means add n to sum and store in sum)
#         sum += n
#     return sum / len(numbers)
# # Use our newly minted function
# print(average(10, 40, 80 ,74, 16, 42, 12, 6))

# Define the generator function
# With the start argument defaulting to 99
# def bottles_song(start = 1):
#     # Set the initial number of bottles are gone
#     bottles = start
#     # Loop through until bottles are gon
#     while bottles < 99:
#         # Display the song
#         this_verse = []
#         this_verse.append(str(bottles) + " bottles on the wall. ")
#         this_verse.append(str(bottles) + " bottles of beer. ")
#         this_verse.append("Take one down, pass it around, ")
#         # Subtract a bottle
#         bottles += 1
#         this_verse.append(str(bottles) + " bottles of beer on the wall")
#         # Yield to the calling function
#         yield "".join(this_verse)
#         # Pick back up here when we return
#     return True

# # Loop through the generator
# for v in bottles_song():
#     print(v)


# Define the World class
# class World:
#     # Define our greeting
#     greeting = "Hello, World!"

#     # Run this whenever the object is created
#     def __init__(self):
#     # Print greeting
#         print(self.greeting)

# # Use the class World to create a world object named w
# w = World()

# Define a new class
# class Customer:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def greet(self):
#         print("Hello, " + self.name + "!")
# # Create three objects based on the Customer class
# c1 = Customer("Sarah", "Atlanta")
# c2 = Customer("Robert", "Florence")
# c3 = Customer("Thomas", "Denver")

# # Add customer objects to a list
# customers = [c1, c2, c3]

# # Iterate through list, greet, then display information
# for c in customers:
#     c.greet()
#     print(c.name + " lives in " + c.city + ".")



# class Customer:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def __enter__(self):
#         print("Entering scope.")
#         # Run code upon entering scope of with statement
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Leaving scope")
#         # Run code upon leaving scope of width statement

#     def greet(self):
#         print("Hello, " + self.name + "!")

#     # Use with to create a scope
# with Customer("Robert", "Florence") as robert:
#         robert.greet()


# class World:
#     def __init__(self):
#         print("I'm alive!")

#     def __del__(self):
#         print("I'm gone!")
 
# earth = World()
# del(earth)
 
# # Convert kilometers to miles
# class Converter:
#     def __init__(self, km):
#         self.km = km
#     def to_miles(self):
#         return self.km / 1.609
    
# # Convert 3 kilometers to miles
# distance1 = Converter(3)
# print(distance1.to_miles())


# class Distance:
#     def __init__(self, km):
#         self._km = km

#     @property
#     def km(self):
#         return self._km
    
#     @km.setter
#     def km(self, value):
#         self._km = value

#     @property
#     def miles(self):
#         return self._km / 1.609
    
#     @miles.setter
#     def miles(self, value):
#         self._km = value * 1.609

# distance2 = Distance(3)
# print("3 killometers is " + str(distance2.miles) + " miles.")
# distance2.miles = 3
# print(str(distance2.miles) + " miles is " + str(distance2.km) + " kilometers.")

class Length:
    def __init__(self, cm):
        self._cm = cm

    @property
    def cm(self):
        return self._cm
    @cm.setter
    def cm(self, value):
        self._cm = value

    @property
    def inch(self):
        return self._inch
    
    @inch.setter
    def inch(self, value):
        self.inch = value * 2.54





