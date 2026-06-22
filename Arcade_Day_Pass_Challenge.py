# Author: Jibreal Id-deen
# Date: June 21, 2026
# Activity: Try to create the Arcade Day Pass Challenge that is provided by Scrimba website

# 🕹️ Arcade Day Pass Tracker — Challenge Steps

# 1) Create variables to store:
customer_name = "Emma"
number_of_passes = 5
token_per_pass = 50
price_per_pass = 10.00
tokens_required_per_game = 5

# 2) Calculate:
total_tokens = number_of_passes * token_per_pass
total_cost = price_per_pass * number_of_passes
game_available = total_tokens // tokens_required_per_game

# 3) Print a summary with:
print(f"Hello, {customer_name}! Welcome to the Arcade Day Pass Tracker! " )
print(f"I see, you brought {number_of_passes} passes! Which is that you will get {total_tokens} tokens! That is really a lot... ")
print(f"With that, it will cost {total_cost} based on that! ")
print(f"Okay, you have the {game_available} number of games you can play with! Good luck.")