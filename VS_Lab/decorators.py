

def test(message):
    def print_message():
        print(message)
    return print_message


a = test("Sabrina")
b = test("Alberto")

a()
b()
