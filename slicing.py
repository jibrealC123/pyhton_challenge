# Author: Jibreal Id-deen
# Date: June 22, 2026
# Activity: Use Slicing/Strings - basic

# The original string we are working with
msg = 'welcome to Python 101: Strings'

# Print the built string using slicing
print(msg[18], msg[0:7].title(), msg[25:29].title(), msg[8:10].title(), msg[8].title() + msg[12] + msg[2] + msg[1] + msg[25])

# Save the built string into a variable
result = str(msg[18]) + " " + msg[0:7].title() + " " + msg[25:29].title() + " " + msg[8:10].title() + " " + msg[8].title() + msg[12] + msg[2] + msg[1] + msg[25]

# Print the result backwards
print(result[::-1])