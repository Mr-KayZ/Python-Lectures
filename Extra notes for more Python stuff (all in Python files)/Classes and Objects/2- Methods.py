###################################################################################################
# Methods
###################################################################################################

# Now last one, we looked at how to make classes and objects and see what they can be used for...
# Let's look at something more interesting, object methods...

#--------------------------------------------------------------------------------------------------
# - Object Methods
#--------------------------------------------------------------------------------------------------

# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Methods are basically functions that belong to a class. Functions, on the other hand...
# Functions belong to an entire program. 
# So methods can only be called through the object of the class...

# Let's get an example, a rectangle area and parameter calculator...
# Of course we can use normal methods to get the answer directly...
# Or we can predefine the answer inside the class and get the area!

class Rectangle:    # Initialize the class

    # Now lets get the constructors for the class...
    def __init__(self, length, width):

        self.length = length
        self.width = width

    # Now this is all nice. Now we can continue on and define another function!
    # This is called a method, since it is in the class.
    # It works the exact same way (with minor differences) as a normal function.
    # This function/method will calculate the area:

    def calc_area(self):    # Note that only self are the parameters. This is intentional.

        # So we have self. That is it? What about the length and width?
        # They already exist, as indicated above!
        # So we simply take the variables from above and return a value:

        return self.length * self.width # Area = Length * Width

        # The minor difference seen here is the fact that we add a self before the variables.
        # If we don't, errors and bugs occur.

    # Now we have an area... Why not the perimeter as well?

    def calc_perimeter(self):   # Just like last time...

        # Again, similar methods to get the answer:

        return 2 * (self.length + self.width)

# And we created the class as well as the method. 
# Remember that until we create the object, nothing is loaded in memory. Yet...

# Now let's continue on and get a rectangle object:

Rectangle_1 = Rectangle(10,20)

# And the object is created! And now we can get the area!
# While we can get area using length * width, we can directly use the method defined in the class.
# We simply write it as a normal object variable:

Area_1 = Rectangle_1.calc_area()

print(Area_1)   # Output is [200] as expected.

# And we can use the other method as described in the class, the perimeter:

Perimeter_1 = Rectangle_1.calc_perimeter()

print(Perimeter_1)  # Output is [60] as expected.

# If we were to have another rectangle, we can use the same method applied above for it.
# Simply assign another object to it:

Rectangle_2 = Rectangle(5,4)

Area_2 = Rectangle_2.calc_area()

Perimeter_2 = Rectangle_2.calc_perimeter()

print (Perimeter_2, Area_2)

# And we can use it multiple times, as many times as needed!

#--------------------------------------------------------------------------------------------------
# - Object Methods - Example with copying
#--------------------------------------------------------------------------------------------------

# Remember the name and things we wanted to create a deep copy of last time?
# Let's make a better thing than that, as in, let's create a deep copy, using methods!
# This will save us the time of doing multiple codes and such if we have multiple points...
# And we need to copy all such points to another, and not as a shallow copy, but a deep one.
# Well, let's bring that name thing again, and this time, we add a method...
# This method will allow us to create a copy when needed!

# First we write the name thing class here:

class Person:   # Creating Class

    def __init__(self, name, age):

        self.name = name
        self.age = age

    # Now we make the method. Just treat the method like as if you are writing a function:

    def create_copy (self, anotherPoint):   # Now we need another parameter inside.

        # Now we have another parameter, called anotherpoint.
        # This is basically a variable that could be used as a temporary value.
        # Remember how we did deep copies last time? We used the same thing...
        # Only this time, we use anotherPoint instead of Person2 or something...

        self.name = anotherPoint.name
        self.age = anotherPoint.age

        # And now we have all that we need.

# Now let's create a Person_1:

Person1 = Person("Kazi Mushfik", 20)

# And now, let's use the anotherPoint method to create Person2, which is a deep copy of Person1.

Person2 = Person("Lel, this will be changed!", 10)  # Initialize Person2 first...

# Now we turn Person2 into Person1 using the method. Call it like a function, almost...

Person2.create_copy(Person1)

print("Person 1:", Person1.name, Person1.age)   # Output is [Person 1: Kazi Mushfik 20]
print("Person 2:", Person2.name, Person2.age)   # Output is [Person 2: Kazi Mushfik 20]

# And Person2 is a deep copy, because if we were to change it in any way, Person1 will not change.

Person2.name = "Change the Name!"

print("Person 1:", Person1.name, Person1.age)   # Output is [Person 1: Kazi Mushfik 20]
print("Person 2:", Person2.name, Person2.age)   # Output is [Person 2: Change the Name! 20]

# As shown, Person1 remains unchanged.