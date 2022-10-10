###################################################################################################
# Functions (general)
###################################################################################################

# Lets say we we want to make a program that takes in 3 inputs for the lengths of a cuboid.
# The program then outputs the volume of the cuboid, which is height * length * width.

# We can ask the user to enter 3 separate values 3 times like so:

#--------------------------------------------------

# width = input("Please enter a real number: ")
# width = float(width)

# height = input("Please enter a real number: ")
# height = float(height)

# length = input("Please enter a real number: ")
# length = float(length)

# volume = width * height * length

# print(f"The volume is: {volume}")

#--------------------------------------------------

# This is an awful amount of writing...

# Instead of all that, we can write the inputs and calculations as a function.
# And we call such functions instead.

# To define a function, we start with def FunctionName([Parameters, if any]).
# For the input, we don't need any parameters (for now).
# And we write the instructions for that function in indents inside the function.

def input_function():

    input_value = input("Please enter a real number: ")
    input_value = float(input_value)

    return input_value

    # The above code does exactly as it is supposed to. Now we can write even less things.

def calculate_function(width_value, height_value, length_value):

    volume = width_value * length_value * height_value

    return volume

    # The above function gets 3 parameters from the arguments.
    # The volume is calculated and returned to the main function.

def print_function(volume_value):

    print("The volume is:", volume_value)


# And we have defined the functions above. Now we need a main function. Hence we write:

def main(): # This is the main function. It isn't required, but it is useful...

    print("Program to calculate the volume of a cuboid")

    # Now this is the main function things. We want the user input.
    # But we already have a function for that, so we simply need to redirect the program there.

    width = input_function()
    height = input_function()
    length = input_function()

    # And we got three values for our sides of the cuboid.
    # Now we want to get the volume of the cuboid. We can also simply redirect all values there.
    # Just pass such values on as arguments in the function and we are done:

    volume = calculate_function(width,height,length)

    # And we got the volume. Now simply print the value, using another function!

    print_function(volume)

# Why did we write a main function? It is not required in Python.
# But most other programming languages need it for it to work. So we write it.

# But now we need to redirect to the main function. Hence we use an entry point.
# Therefore we write:

if __name__ == '__main__':

    main()  # Redirects to the main function.

# For each and every function:
# 1- Determine what data we send to the function (function arguments)
# 2- Determine the function returns (sends back) to the calling functions
