sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

translations = {"mountain": "orod", "bread": "bass",
                "friend": "mellon", "horse": "roch"}

print(translations["mountain"])

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

animals_in_zoo = {}

animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck",
                 "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key: value for key, value in zipped_drinks}

print(drinks_to_caffeine)

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key: value for key, value in zip(names, heights)}

print(students)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


songs = ["Like a Rolling Stone", "Satisfaction", "Imagine",
         "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key: value for key, value in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
            "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20,
                   "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
print(available_items)

health_points = 20
print(health_points)

health_points += available_items.pop("stamina grains", 0)
print(health_points)

health_points += available_items.pop("power stew", 0)
print(health_points)

health_points += available_items.pop("mystic bread", 0)
print(health_points)

print(available_items)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
            "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

print(list(user_ids))

for u in user_ids.keys():
    print(u)

for u in list(user_ids):
    print(u)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

print(num_exercises.values())
print(list(num_exercises.values()))

total_exercises = 0

for values in num_exercises.values():
    total_exercises += values

print(total_exercises)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

pct_women_in_occupation = {"CEO": 28, "Engineering Managers": 9,
                           "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for position, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) + " percent of " + position)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

tarot = {1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune",
         11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

print(spread)

for time, card in spread.items():
    print("Your " + time + " is the " + card + " card.")

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")
