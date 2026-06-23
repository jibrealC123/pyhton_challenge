# Author: Jibreal Id-deen
# Date: June 22, 2026
# Activity: Try to create the Pit Stop Timing Optimzer
# 🏁 Pit Stop Timing Optimizer 🔧

# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds)
ask_total_race_time = (float(input("What is your total of the race time in seconds?: ")))
pit_stops = (int(input("How many pit stops were made?: ")))
average_pit_stop_duration = (float(input("What is the average pit stop duration in seconds?: ")))

# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
total_pit_stop_time = pit_stops * average_pit_stop_duration
percentage_of_the_spent = total_pit_stop_time / ask_total_race_time * 100
percentage_of_the_spent = round(percentage_of_the_spent, 2)


# - Total pit stop time in seconds
# - Percentage of race time spent in pits
print(f"The total of the pit stop time: {total_pit_stop_time} ")
print(f"The percentage of race time spent in pits: {percentage_of_the_spent} ")

# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"
if percentage_of_the_spent > 5:
    print("You need a bit crew. 🛠️ ")

