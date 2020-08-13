class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "This is the {name} Menu and is available from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time=self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for item in purchased_items:
            if (item in self.items):
                bill += self.items[item]
        return bill


brunch_menu_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_menu_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_menu_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_menu_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

brunch_menu = Menu("Brunch", brunch_menu_items, 11, 14)

early_bird_menu = Menu("Early Bird", early_bird_menu_items, 15, 18)

dinner_menu = Menu("Dinner", dinner_menu_items, 17, 23)

kids_menu = Menu("Kids", kids_menu_items, 11, 21)

print(brunch_menu)

brunch_menu_order = ["pancakes", "home fries", "coffee"]
print(brunch_menu.calculate_bill(brunch_menu_order))

early_bird_order = ["salumeria plate", "mushroom ravioli (vegan)"]
print(early_bird_menu.calculate_bill(early_bird_order))


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "This store is located at {address}".format(address=self.address)

    def available_menus(self, time):
        available = []
        for menu in self.menus:
            if (menu.start_time <= time) and (menu.end_time > time):
                available.append(menu)
        return available


flagship_store_address = "1232 West End Road"
new_installment_address = "12 East Mulberry Street"

flagship_store_menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
new_installment_menu = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]


flagship_store = Franchise(flagship_store_address, flagship_store_menus)
new_installment = Franchise(new_installment_address, new_installment_menu)

print(flagship_store)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


fazoolin_name = "Basta Fazoolin' with my Heart"
fazoolin_franchises = [flagship_store, new_installment]

fazoolin_business = Business(fazoolin_name, fazoolin_franchises)

arepas_menu_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Arepas", arepas_menu_items, 10, 20)

arepas_place_address = "189 Fitzgerald Avenue"
arepas_place = Franchise(arepas_place_address, [arepas_menu])

arepas_place_name = "Take a' Arepa"
arepas_business = Business(arepas_place_name, [arepas_place])
