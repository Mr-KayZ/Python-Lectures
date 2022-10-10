###################################################################################################
# Nested Classes
###################################################################################################

# We have seen the notion that classes can contain strings, numbers and other things...
# But then we need to ask ourselves the diabolical question: 
# What if we contain a class within a class?

# To whoever thought that up, I admire you for your bravery...
# But I hate you because I now have to study this!

# Such things are called nested classes.

#--------------------------------------------------------------------------------------------------
# - Objects within classes
#--------------------------------------------------------------------------------------------------

# This is basically a class within a class. Using classes to create an object within a class...

# Let's begin with an example, say the class Point:

class Point:    # Define the class point

    # Define the point using [__init__()]:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Now let's create another class using the object of Point. Say we want to make a Circle...
# For that, we need a constant Pi. So...

Pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534

class Circle:

    def __init__(self, x, y, radius):
        
        # Now we want to create a variable called center...
        # We will use the class point to create this object:

        self.center = Point(x, y)   # Simply create it like an object!
        
        # And the radius can be the radius:

        self.radius = radius
    
    # Now let's create a method, say the area function.
    # We use the value of Pi to get that answer. Pi is a constant.

    def calculate_area(self):
        return Pi * self.radius * self.radius

Circle_1 = Circle(30, 40, 100)

print(Circle_1.calculate_area())

#--------------------------------------------------------------------------------------------------
# - Using Arrays to store Objects
#--------------------------------------------------------------------------------------------------

# Like how we used arrays to store arrays, we can also use arrays to store objects.
# Let's say we have 2 circles:
# - Circle 1 - Center (20,30), Radius 10
# - Circle 2 - Center (1, 2), Radius 5
# - Circle 3 - Center (250,305), Radius 102

# And we can put the objects into an array as is:

CircleArray = [Circle(20,30,10), Circle(1,2,5), Circle(250,305,102)]

# And if we want to access the value of the object from the array, simply refer to it's index:

print(CircleArray[0].calculate_area())  # Output is [314.1592653589793].
print(CircleArray[1].calculate_area())  # Output is [78.53981633974483].
print(CircleArray[2].calculate_area())  # Output is [32685.129967948207].