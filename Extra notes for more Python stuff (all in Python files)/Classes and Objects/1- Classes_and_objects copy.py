###################################################################################################
# Classes and Objects
###################################################################################################

# Python is a very object oriented programming language. 
# Almost everything in Python is an object, with its properties and methods.
# A class is like an object constructor, or a "blueprint" for creating objects.

#--------------------------------------------------------------------------------------------------
# - Class and Object creation
#--------------------------------------------------------------------------------------------------

# What is a class? A class can be considered a composite variable, containing different things.
# It is the definition of a new entity, or data type. 
# (For example, a desk is an entity with a table top and legs. A class is similar...)
# Let's say we want a point on the cartesian plane (x and y coordinate...)
# This would require a variable that is more complex, hence we create:

class Point:
    x = 1
    y = 2

# And we have created a class.
# Now we need to construct an object relating to that class, so we write:

Point_1 = Point()    # This is an object

# But what is an object? An object is an instance of a class.
# (Remember the table entity? The desk I am working on is an instance of the table.)

# In other words, a class is the definition of an object, and an object is the real thing.

# Let's say we want to print an object, say p1. We write the following:

print(Point_1.x, Point_1.y)   # Output is [1 2].

# And if we want to change the variable in a class, we can do so like this:

Point_1.x = -7

print(Point_1.x, Point_1.y)   # Output is [-7 2].

# Note that if we were to simply write [x = -11], [Point_1.x] would still be -7.
# This is because [x] is considered a separate entity to [Point_1.x].

#--------------------------------------------------------------------------------------------------
# - Constructors and the __init__() function
#--------------------------------------------------------------------------------------------------

# Let's take the same class Point and assign it to 2 more objects, p1 and p2:

p1 = Point()    # Constructing p1 which is an object of type point
p2 = Point()    # Constructing p2 which is another object of type point

# Both now have the same values inside them. (x = 1, y = 2)

# Notice how we kept on using the word [Point()]. Now, [Point()] is not a function.
# It is called a constructor (as it was defined as class instead of a function, which is def)
# In other words, [Point()] is a constructor of class point . 
# This constructor can be used to construct objects of type point.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# So far, the examples above are classes and objects in their simplest form.
# In real life applications, they really are not that useful. Therefore...
# To understand the meaning of classes, we have to understand the built-in [__init__()] function.

# All classes have a function called [__init__()].
# This is always executed before the class is being initiated.
# We use the [__init__()] function to assign values to object properties.
# Either that, or we do other operations that are necessary to do when the object is being created.

# Let's create a s=class named person, and lets use the [__init__()] function to assign values...
# Values for name and age:

class Person:   # Creating Class

    # Now we will define the function [__init__()]. It is just like any normal function:
    def __init__(self, name, age):  # We write the usual 2 after self...

        self.name = name    # Now we define name...
        self.age = age      # Now we define age...

# Now you may have noticed a new parameter inside [__init__()], called [self].
# What is the self parameter? It is a reference to the current instance of a class...
# In other words, when defining an object, whatever value is passed onto the object...
# It's type will be created alongside the variable of that object.

# Now we can use the class properly:

Person1 = Person ("Kazi Mushfik", 20) # Note that now we put arguments into the constructor...

# Now we can put values into the class instead of changing it individually before!
# And we can use them the same way we use normal objects:

print(Person1.name, Person1.age)  # Output is [Kazi Mushfik 20]

# Note that the [__init__()] function is called automatically every time a class is used...
# To create a new object.

#--------------------------------------------------------------------------------------------------
# - Copying Objects
#--------------------------------------------------------------------------------------------------

# Now objects share a lot of similarities with arrays, in the sense they both can contain data.
# However, with the [__init__()] function, it can hold variable sets of data.
# But what happens if we copy objects? For example, let's have another Person:

Person2 = Person ("Leeroy Jenkins", 21)

# This Person2 is nothing like Person1, as they have different values.
# Now let's make Person1 = Person2:

Person1 = Person2

# Now like arrays, Person will change with Person2 if we change Person2 in any way.
# This is known as a shallow copy. It is because both objects are looking at the same memory spot.

Person2.name = "Lol No name!"

print(Person1.name, Person1.age)  # Output is [Lol No name! 21]

# But if we want a deep copy (a copy independent of each other)...
# We have to manually type each and every item equal to the other, like so:

Person1 = Person ("Kazi Mushfik", 20)   # Reinitialize Person1...

Person1.name = Person2.name
Person1.age = Person2.age

Person2.name = "Changed again!"

print(Person1.name, Person1.age)  # Output is [Lol No name! 21]