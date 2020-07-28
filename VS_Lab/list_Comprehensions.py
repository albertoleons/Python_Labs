words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
    if word[0] == '@':
        usernames.append(word)

print(usernames)

usernames = []
usernames = [word + "damn" for word in words if word[0] == '@']
print(usernames)

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [measurement * 9/5 + 32 for measurement in celsius]

print(fahrenheit)

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

single_digits = list(range(0,10))
#single_digits = range(0,10)

squares = []

for digits in single_digits:
  print(digits)
  squares.append(digits**2)

print(squares)

cubes = [digits**3 for digits in single_digits ]

print(cubes)

sabri = [30, "white", "woman", 167]
age, race, gender, height = sabri
print(age)
print(race)
print(gender)
print(height)

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price
print(total_price)

average_price = total_price/len(prices)
print('Average Haircut Price:',average_price)

new_prices = [price-5 for price in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print('Total Revenue:', total_revenue)

average_daily_revenue = total_revenue/7
print('Average Daily Revenue:',average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]

#cuts_under_30 = []
#for i in range(len(new_prices)-1):
 # if new_prices[i] < 30:
  #  cuts_under_30.append(hairstyles[i])

print(cuts_under_30)