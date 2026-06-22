# Author: Jibreal Id-deen
# Date: June 22, 2026
# Activity: Use Slicing/Strings - basic

# The original string we are working with
msg = 'welcome to Python 101: Strings'

# Print the built string using slicing
print(msg[23:30].title(),msg[0:7].title(),msg[18:21],msg[11:17])

# # Save the built string into a variable
reseve_msg = msg[23:30].title() + " " + msg[0:7].title() + " " + msg[18:21] + " " + msg[11:17]

# Print the result backwards
print(reseve_msg[::-1])
 