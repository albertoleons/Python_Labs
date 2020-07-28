authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

author_last_names = []

for author in author_names:
  n = author.split()
  author_last_names.append(n[-1])

print(author_last_names)

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)

print(reapers_line_one)

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

love_maybe_full = "\n".join(love_maybe_lines_stripped)

print(love_maybe_full)

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

print(toomer_bio_fixed)

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")

print(disown_placement)

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc


author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description, '\n', '\n')

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems, "\n")

highlighted_poems_list = highlighted_poems.split(",")

#print(highlighted_poems_list)

highlighted_poems_stripped = []

for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())
#print(highlighted_poems_stripped)

highlighted_poems_details = []

for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(":"))

#print(highlighted_poems_details)

titles = []
poets = []
dates = []

for n in highlighted_poems_details:
  titles.append(n[0])
  poets.append(n[1])
  dates.append(n[2])

#print(titles)
#print(poets)
#print(dates)

for n in range(0, len(titles)):
  line = "The poem {title} was published by {poet} in {date}".format(title=titles[n], poet=poets[n], date=dates[n])
  print(line, "\n")





















