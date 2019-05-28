"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('Since %s I fed them to %s sharks for %.2f seconds' % (z, x, y))
# Use the 'format' string method to print the same thing
print('Since {} I fed them to {} sharks for {} seconds'.format(z,x,round(y, 2)))
# Finally, print the same thing using an f-string
print(f'Since {z} I fed them to {x} sharks for {round(y, 2)} seconds')