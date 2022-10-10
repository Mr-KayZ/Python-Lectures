###################################################################################################
# Other things of Classes and Objects
###################################################################################################

# In the last few notes, we have seen what Classes and Objects are, as well as used methods.
# This is to cover the extra things that may be useful in Classes and Objects...

#--------------------------------------------------------------------------------------------------
# - The self Parameter in __init__()
#--------------------------------------------------------------------------------------------------

# The [self] parameter is a reference to the current instance of the class. 
# It is used to access variables that belong to that class.

# Now, the [self] parameter does not need to be named self.
# It can be called whatever you want, but it needs to be the first parameter of any method.

class Person:

    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def My_Function(self):
        print("Hello, my name is:", self.Name)

Person1 = Person("Kazi Mushfik", 20)
Person1.My_Function()

# Note that Pylint shows it up as an error if we were to change it from self. But it still works...

#--------------------------------------------------------------------------------------------------
# - Deleting Object Properties and Objects
#--------------------------------------------------------------------------------------------------

# If we want to remove an object property (for example, the [Name] from Person1)...
# We can use the [del] keyword before the object property:

del Person1.Name

# print(Person1.Name)   # This gives an error when run.

# Now the name attribute is deleted for Person1. But that does not mean it cannot be reinitialized:

Person1.Name = "I am back"

print(Person1.Name) # Output is [I am back].

# Alternatively, we can delete the whole object itself if wanted. The del keyword is used again.
# Only this time, instead of pointing it at an attribute, we point it to the object itself.

del Person1

# print(Person1.Name, Person1.Age)  # This gives an error when run.

# Again, we have to reinitialize Person1 if we want to use it again. Maybe with different values...

Person1 = Person("I am back 2", 123)

print(Person1.Name, Person1.Age) # Output is [I am back 2 123].

#--------------------------------------------------------------------------------------------------
# - The Pass statement
#--------------------------------------------------------------------------------------------------

# Class definitions cannot be empty under any circumstances.
# However if we want to initialize it for use later (as in we are just debugging the code now)...
# We can use the [pass] statement to ignore this class when called upon by a code.
# Simply put pass in class:

class Person_2:
    pass


# This way, even if we use it, we won't get an error:

Person2 = Person_2

# However, if we were trying to access any attribute of Person2, it would fail to compile.
# This is because no attribute of Person2 exists yet.

# However, if we have constructors inside, even after the [pass] statement...
# The [pass] statement is ignored and it becomes obsolete as the rest of the class is still called.
# So [pass] really works when there is nothing else in the class.

class Person_3:
    pass
    
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def My_Function(self):
        print("Hello, my name is:", self.Name)

Person3 = Person_3("Kazi Mushfik", 20)

print(Person3.Name) # Still works. Output is [Kazi Mushfik].