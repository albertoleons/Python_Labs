gamers = []


def add_gamer(gamer, gamer_list):
    if ("name" in gamer) and ("availability" in gamer):
        gamer_list.append(gamer)
    else:
        print("Bad Gamer")


kimberly = {"name": "Kimberly Warner",
            "availability": ["Monday", "Tuesday", "Friday"]}

add_gamer(kimberly, gamers)
add_gamer({'name': 'Thomas Nelson', 'availability': [
          "Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': [
          "Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': [
          "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': [
          "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': [
          "Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': [
          "Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': [
          "Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': [
          "Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': [
          "Monday", "Tuesday", "Wednesday"]}, gamers)

# print(gamers)


def build_daily_frequency_table():
    frequency_table = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }
    return frequency_table


count_availability = build_daily_frequency_table()
# print(count_availability)


def calculate_availability(gamer_list, available_frequency):
    for gamer in gamer_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1


calculate_availability(gamers, count_availability)
# print(count_availability)


def find_best_night(availability_table):
    biggest_value = 0
    best_game_night = ""
    for key, value in availability_table.items():
        if value > biggest_value:
            biggest_value = value
            best_game_night = key
    return best_game_night


game_night = find_best_night(count_availability)
# print(game_night)


def available_on_night(gamer_list, night):
    people_available = []
    for gamer in gamer_list:
        if night in gamer["availability"]:
            people_available.append(gamer["name"])
    return people_available


attending_game_night = available_on_night(gamers, game_night)
# print(attending_game_night)

#form_email = "{name}, {day_of_week}, {game}"
form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society
"""


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(
            name=gamer, day_of_week=day, game=game))


send_email(attending_game_night, game_night, "Abruptly Goblins!")

unable_to_attend_best_night = []

for gamer in gamers:
    if (gamer["name"] in attending_game_night) == False:
        add_gamer(gamer, unable_to_attend_best_night)

# print(unable_to_attend_best_night)

second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)
# print(second_night_availability)

second_night = find_best_night(second_night_availability)
# print(second_night)

available_second_game_night = available_on_night(
    unable_to_attend_best_night, second_night)
# print(available_second_game_night)

send_email(available_second_game_night, second_night, "Abruptly Goblins!")
