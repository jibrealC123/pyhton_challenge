# Author: Jibreal Id-deen
# Date: June 23, 2026

# Activity: Try to practice using Lists exericse based on selling lemonade over two weeks.
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sales_w2.append(int(input("Please put the number of the day: ")))
sales = sales_w1 + sales_w2
best_day = (max(sales))
worst_day = (min(sales))

earning_best_day = best_day * 1.50
earning_worse_day = worst_day * 1.50
total = (sum(sales)) * 1.50
print(f"The total of the money you earned so far: {total}! ")
print(f"based on the best days, you earned: {earning_best_day}! ")
print(f"Based on the worst days, you earned: {earning_worse_day}! ")

 

