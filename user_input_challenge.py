# Author: Jibreal Id-deen
# Date: June 22, 2026
# Activity: Try to create a distance coverter coverting Km to miles

#  Distance coverter converting Km to Miles — Challenge Steps

# - Take two inputs from user: Their first name and the distance in km.
name = input("What's your name? ")
print(f"Hello, {name}! ")
distance_km = float(input("Enter the km: "))

# - Create a distance converter converting Km to miles in a round.
distance_miles = distance_km / 1.609 
distance_miles = round(distance_miles, 2)

# - Print the outscreen to show the user that is converting to miles  so the user can understand.
print("------------DISTANCE COVERTER-------------")
print(f"{name.capitalize()}, {distance_km} km is equal to {distance_miles} miles! ")
