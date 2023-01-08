'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michaela Hronová
email: hronova.michaela09@gmail.com; hronova@ceps.cz
discord: 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# username = input('Jake je Vase prihlasovaci jmeno? ')
# password = input('Jake je Vase heslo? ')
username = "bob"
password = "123"

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123" 
}

if username in uzivatele.keys():
    if password == uzivatele[username]:
        print(f"Welcome to the app, {username}")
    else:
        print("Incorrect password, terminating the program.")
        quit()
else:
    print("Unregistered user, terminating the program.")
    quit()

while True:
    # text_number_input = input("Enter a number btw. 1 and 3 to select: ")
    text_number_input = "1"
    try:
        text_number_int = int(text_number_input)
    except ValueError:
        print("Invalid value. The value has to be a number.")
        continue

    if text_number_int in [1,2,3]:
        text = TEXTS[text_number_int - 1]
        break
    else:
        print("This number of text is not available.")
        continue

print(text)

# analyza textu
word_list = text.split()
total_word_count = 0
titlecase_word_count = 0
uppercase_word_count = 0
lowercase_word_count = 0
numeric_strings_count = 0
numeric_strings_sum = 0

for word in word_list:
    total_word_count = total_word_count + 1
    if word.istitle():
        titlecase_word_count = titlecase_word_count + 1
    if word.isupper():  # 30N se vyhodnocuje taky jako uppercase
        uppercase_word_count = uppercase_word_count + 1
        # print(word)
    if word.islower():
        lowercase_word_count = lowercase_word_count + 1
    if word.isnumeric():
        numeric_strings_count = numeric_strings_count + 1
        numeric_strings_sum = numeric_strings_sum + int(word)


print(f"There are {total_word_count} words in the selected text.")
print(f"There are {titlecase_word_count} titlecase words.")
print(f"There are {uppercase_word_count} uppercase words.")
print(f"There are {lowercase_word_count} lowercase words.")
print(f"There are {numeric_strings_count} numeric strings.")
print(f"The sum of all the numbers {numeric_strings_sum}.")

    
