# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

# Write your sum_values function here:


def sum_values(my_dictionary):
    sum_value = 0
    for value in my_dictionary.values():
        sum_value += value
    return sum_value


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
    total_value = 0
    for value in my_dictionary:
        if value % 2 == 0:
            total_value += my_dictionary[value]
    return total_value


# Uncomment these function calls to test your  function:
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


# Write your add_ten function here:
def add_ten(my_dictionary):
    for i in my_dictionary:
        my_dictionary[i] += 10
    return my_dictionary


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
    lst = []
    for key in my_dictionary:
        for value in my_dictionary.values():
            if key == value:
                lst.append(key)
                break
    return lst


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


# Write your max_key function here:
def max_key(my_dictionary):
    lgst_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > lgst_value:
            lgst_value = value
            return_key = key
    return return_key


# Uncomment these function calls to test your  function:
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

# Write your word_length_dictionary function here:


def word_length_dictionary(words):
    new_dictionary = {}
    for word in words:
        new_dictionary[word] = len(word)
    return new_dictionary


# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")


# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    new_dictionary = {}
    for word in words:
        if (word in new_dictionary) == False:
            new_dictionary[word] = words.count(word)
    return new_dictionary


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

# Write your unique_values function here:


def unique_values(my_dictionary):
    lst = []
    for key, value in my_dictionary.items():
        if (value in lst) == False:
            lst.append(value)
    return len(lst)


# Uncomment these function calls to test your  function:
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1

# -------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

# Write your count_first_letter function here:


def count_first_letter(names):
    new_names = {}
    for key, value in names.items():
        first_letter = key[0]
        number_people = len(value)
        if (first_letter in new_names) == False:
            new_names[first_letter] = number_people
        elif (first_letter in new_names) == True:
            new_names[first_letter] += number_people
    return new_names


# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
