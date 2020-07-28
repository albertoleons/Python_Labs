letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
  unique_letters = []
  for letter in word:
    if unique_letters.count(letter) == 0:
      unique_letters.append(letter)
  return len(unique_letters)

# Uncomment these function calls to test your function:
#print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))
# should print 4

# Write your count_char_x function here:

def count_char_x(word, x):
  return word.count(x)


# Uncomment these function calls to test your tip function:
#print(count_char_x("mississippi", "s"))
# should print 4
#print(count_char_x("mississippi", "m"))
# should print 1

# Write your substring_between_letters function here:

def substring_between_letters(word, start, end):
  first_index = word.find(start)
  new_word = word[first_index + 1:]
  second_index = new_word.find(end)
  if second_index > 0:
    return new_word[:second_index]
  else:
    return word

# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# Write your x_length_words function here:
def x_length_words(sentence, x):
  lst = sentence.split(" ")
  for word in lst:
    if len(word) < x:
      return False
  return True

# Uncomment these function calls to test your tip function:
#print(x_length_words("i like apples", 2))
# should print False
#print(x_length_words("he likes apples", 2))
# should print True

# Write your check_for_name function here:
def check_for_name(sentence, name):
  new_sentence = sentence.lower()
  if new_sentence.find(name.lower()) > -1:
    return True
  else:
    return False


# Uncomment these function calls to test your  function:
#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# Write your every_other_letter function here:
def every_other_letter(word):
  new_word = ""
  for n in range(0, len(word), 2):
    new_word += word[n]
  return new_word

# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 

# Write your reverse_string function here:
def reverse_string(word):
  new_word = ""
  for n in range(len(word)-1, -1, -1):
    new_word += word[n]
  return new_word

# Uncomment these function calls to test your  function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print

# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  return word2[0] + word1[1:] + " " + word1[0] + word2[1:]

# Uncomment these function calls to test your function:
#print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a

# Write your add_exclamation function here:
def add_exclamation(word):
  while len(word) < 20:
    word += "!"
  return word

# Uncomment these function calls to test your function:
#print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
#print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn