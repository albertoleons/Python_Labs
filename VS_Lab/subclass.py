# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

# Define your exception up here:


class OutOfStock(Exception):
    print("It's out of stock")

# Update the class below to raise OutOfStock


class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if (self.stock[color] <= 0):
            raise OutOfStock
        else:
            self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
# candle_shop.buy('green')

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text


class User:
    def __init__(self, username):
        self.username = username

    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text


class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text


# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40


# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * 0.001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * 0.00005


# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


class Chess:
    def __init__(self):
        #self.board = setup_board()
        #self.pieces = add_chess_pieces()
        print("Chess")

    def play(self):
        print("Playing chess!")


class Checkers:
    def __init__(self):
        #self.board = setup_board()
        #self.pieces = add_checkers_pieces()
        print("Checkers")

    def play(self):
        print("Playing checkers!")


def play_game(chess_or_checkers):
    chess_or_checkers.play()


chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()

for game in [chess_game, checkers_game, chess_game_2]:
    play_game(game)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))
print(len(a_dict))
print(len(a_string))

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms


sodium = Atom("Na")
chlorine = Atom("Cl")
#salt = Molecule([sodium, chlorine])
salt = sodium + chlorine
print(salt)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


class UserGroup:
    def __init__(self, users, permissions):
        self.user_list = users
        self.permissions = permissions

    def __iter__(self):
        return iter(self.user_list)

    def __len__(self):
        return len(self.user_list)

    def __contains__(self, user):
        return user in self.user_list


diana = User('diana')
frank = User('frank')
jenn = User('jenn')

can_edit = UserGroup([diana, frank], {'can_edit_page': True})
can_delete = UserGroup([diana, jenn, frank], {'can_delete_posts': True})

print(len(can_edit))
# Prints 2

for user in can_edit:
    print(user.username)
# Prints "diana" and "frank"

if frank in can_delete:
    print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers

    def __len__(self):
        return len(self.lawyers)

    def __contains__(self, lawyer):
        return lawyer in self.lawyers


d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
print("Donelli" in d_and_p)
print(len(d_and_p))

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


class SortedList(list):
    def __init__(self, value):
        super().__init__(value)
        super().sort()

    def append(self, value):
        super().append(value)
        return super().sort()


a = SortedList([2, 1, 6])
print(a)

a.append(-2)
print(a)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")
