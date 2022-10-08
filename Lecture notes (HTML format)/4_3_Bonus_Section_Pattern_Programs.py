###################################################################################################
# 4.3 - Bonus section: Repetition Structures (Pattern programs)
###################################################################################################

# One of the things that loops can be used for is producing patterns.
# Some of them can be used to produce squares, triangles...
# This will go over the basics of such patterns.

#--------------------------------------------------------------------------------------------------
# - Pattern Example 1 - Square
#--------------------------------------------------------------------------------------------------

# One of the easiest patterns to draw is a square. Let's say we want to draw a 10x10 square of 0s.
# The easiest way could be to print '0' ten times on each line using [print("0 0 0 0...")]
# But that is boring... Why not use a loop?

# Using a loop, we can even alter the shape of the square, which is not possible above.
# So we can ask the user an input:

n = int(input("Please enter the length of the side: "))

print()

# And make a loop to print n * n many 0s. And thus we use the following loop:

i = 0   # Initialize i...

while ( i < n ):    # The outer loop...

    j = 0   # Initialize j inside the loop...

    while ( j < n ):    # The inner loop...

        print("0", end = " ")   # Print one 0...

        j += 1  # Print another 0 while j < n...
    
    i += 1  # Update statement, go to new line...

    print() # Print a new line once inner loop finishes...

print()

#--------------------------------------------------------------------------------------------------
# - Pattern Example 2 - Square with diagonal from left to right
#--------------------------------------------------------------------------------------------------

# Let's say we want a square that looks nice now, say with a diagonal stripe.
# If you notice, a diagonal stripe can occur from the top left to the bottom right.
# As in, when the number i = j, that position is on the diagonal...
# So all we have to do is change it to something else from a 0 to indicate, say a *.

# We can use the same values as above, no problems... Now we take the same while statement...
# And we add an if function inside the inner loop.

i = 0   # Reinitialize i back to 0...

while ( i < n ):

    j = 0

    while ( j < n ):

        if ( i == j ):  # This is the new if statement we use...

            print("+", end = " ")   # If the position is on the diagonal, we print a 1.

        else:

            print("0", end = " ")   # Otherwise it is the usual...

        j += 1
    
    i += 1

    print()

print()

#--------------------------------------------------------------------------------------------------
# - Pattern Example 3 - Square with diagonal from right to left
#--------------------------------------------------------------------------------------------------

# Now that pattern is nice and all, but what if we want a diagonal from left to right?
# Now notice here, the position of the 1 would be different now...
# Now here, we notice that values of the pattern are kind of the opposite...
# Using math and algebra, we get another condition: i + j = n - 1...
# And we can use that for our condition instead for the if statement...

i = 0   # Reinitialize i back to 0...

while ( i < n ):

    j = 0

    while ( j < n ):

        if ( i + j == n - 1 ):  # Change the condition...

            print("+", end = " ")

        else:

            print("0", end = " ")

        j += 1
    
    i += 1

    print()

print()

#--------------------------------------------------------------------------------------------------
# - Pattern Example 4 - Square with diagonal cross
#--------------------------------------------------------------------------------------------------

# Now this is a real what-if scenario... What if we want both diagonals in the square?
# Both from left to right and right to left?
# Then we incorporate the use of both statements as elif...

# Simple copy paste work really and slight editing:

i = 0   # Reinitialize i back to 0...

while ( i < n ):

    j = 0

    while ( j < n ):

        if ( i + j == n - 1 ):  # Change the condition...

            print("+", end = " ")

        elif ( i == j ):        # The second condition...

            print("+", end = " ")

        else:

            print("0", end = " ")

        j += 1
    
    i += 1

    print()

print()

#--------------------------------------------------------------------------------------------------
# - Pattern Example 5 - Printing an alternate pattern
#--------------------------------------------------------------------------------------------------

# Let's say we want to print a code that prints 1s and 0s in an alternating sequence...
# As in the first number is 1 and the next is 0. How will we print them?
# Well, let's start with the logic... For every row, the column i changes...
# The addition of all column and row position will give that row/column an even/odd combination.
# And hence we can use that logic in the square pattern to print out alternate patterns.

i = 0   # Reinitialize the counter...

while ( i < n ):

    j = 0

    while ( j < n ):

        if ( ( i + j) % 2 == 0 ):  # This is where the logic comes in...

            print("+", end = " ")   # If the position number is odd, write a +.

        else:

            print("0", end = " ")   # Otherwise it even and can be written as otherwise.

        j += 1
    
    i += 1

    print()

print()

#--------------------------------------------------------------------------------------------------
# - Pattern Example 6 - Right angled triangle with side on left
#--------------------------------------------------------------------------------------------------

# Let's say we want a program to print a right angled triangle with equal sides...
# So an isosceles right-angled triangle laying on it's side... We can use the same n value...
# But how do we draw it?

# Again a while function. This time, each line is increasing by 1 as it goes down...

i = 0   # Reinitialize i back to 0...

while ( i < n ):

    j = 0

    while ( j <= i ):

        print("0", end = " ")   # Prints the line increasingly...

        j += 1  # Updates the inner loop expression.

    print() # Goes to the next line.

    i += 1  # Updates outer loop.

print() 

#--------------------------------------------------------------------------------------------------
# - Pattern Example 7 - Inverted right angled triangle with side on left
#--------------------------------------------------------------------------------------------------

# Basically the same triangle as above, but this time it is upside down.
# So what is the idea here? Now the condition will be j < n - i (opposite)
# And we print the answer... Basically the same loop as above with updated condition.

i = 0   # Reinitialize i back to 0...

while ( i < n ):

    j = 0

    while ( j < n - i ):    # Change the condition of the inner loop

        print("0", end = " ")

        j += 1

    print()

    i += 1

print()

#--------------------------------------------------------------------------------------------------
# - Pattern Example 8 - Right angled triangle with side on right
#--------------------------------------------------------------------------------------------------

# This is the triangle but now with the side on the right instead of the left.
# now here, we need something to the opposite side...
# Since python codes from the left, we can fill it with empty spaces...
# And fill the other side with actual numbers like that in a square, but half square, a triangle.

i = 0   # Reinitialize i back to 0...

while ( i < n ):

    j = 0

    while ( j < n ):

        if ( i > n - j ):  # This is the new if statement we use...

            print("0", end = " ")   # This will print everything on the right.

        else:

            print(" ", end = " ")   # Otherwise it will be a space

        j += 1
    
    i += 1

    print()

print()

#--------------------------------------------------------------------------------------------------
# - Pattern Example 9 - Inverted right angled triangle with side on right
#--------------------------------------------------------------------------------------------------

# Above triangle but this time upside down. Now we simply change the if condition:

i = 0   # Reinitialize i back to 0...

while ( i < n ):

    j = 0

    while ( j < n ):

        if ( i < j ):  # This is the new if statement we use...

            print("0", end = " ")   # This will print everything on the right.

        else:

            print(" ", end = " ")   # Otherwise it will be a space

        j += 1
    
    i += 1

    print()

print()