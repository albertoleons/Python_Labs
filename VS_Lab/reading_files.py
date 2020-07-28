import json
import csv

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


with open("test_file.txt") as text_file:
    text_data = text_file.read()

print(text_data)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

with open("test_file2.txt") as lines_doc:
    for lines in lines_doc.readlines():
        print(lines)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

with open("test_file.txt") as first_line_doc:
    first_line = first_line_doc.readline()
print(first_line)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

with open("bad_bands.txt", "w") as bad_bands_doc:
    bad_bands_doc.write("Whatever")

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

with open("cool_dogs.txt", "a") as cool_dogs_file:
    cool_dogs_file.write("Air Buddy")

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

#close_this_file = open('fun_file.txt')
with open("fun_file.txt") as close_this_file:
    setup = close_this_file.readline()
    punchline = close_this_file.readline()

print(setup)
print(punchline)

fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")

# But we need to remember to close the file
fun_cities_file.close()

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

with open("logger2.csv") as log_csv_file:
    print(log_csv_file.read())

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


with open("cool_csv.csv") as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        print(row["Cool Fact"])

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

isbn_list = []
with open("books.csv") as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter="@")
    for book in books_reader:
        isbn_list.append(book["ISBN"])
print(isbn_list)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {
    'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}]

with open('output.csv', 'w') as output_csv:
    fields = ['name', 'userid', 'is_admin']
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)

    output_writer.writeheader()
    for item in big_list:
        output_writer.writerow(item)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {
    'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

with open("logger.csv", "w") as logger_csv:
    log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
    log_writer.writeheader()
    for log in access_log:
        log_writer.writerow(log)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

with open('purchase_14781239.json') as purchase_json:
    purchase_data = json.load(purchase_json)

print(purchase_data['user'])
# Prints 'ellen_greg'

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

with open("message.json") as message_json:
    message = json.load(message_json)
    print(message["text"])

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

turn_to_json = {
    'eventId': 674189,
    'dateTime': '2015-02-12T09:23:17.511Z',
    'chocolate': 'Semi-sweet Dark',
    'isTomatoAFruit': True
}

with open('output.json', 'w') as json_file:
    json.dump(turn_to_json, json_file)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

data_payload = [
    {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
     'follow up': 'But enough talk!'}
]

with open("data.json", "w") as data_json:
    json.dump(data_payload, data_json)

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")
