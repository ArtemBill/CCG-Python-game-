# Импортируем необходимый модуль для рандомного подбора слов
import random

# Импортируем предложенный набор слов
from hangman_guessing import guess_list

# Импортируем и печатаем название игры
from hangman_life import game_name
print(game_name)
print()

tries = 6
guessing_word = list(random.choice(guess_list).lower())
print(guessing_word)
print()

guessing_letter = str(input())
word_underscore = ["_", "_", "_", "_", "_", "_"]
print(*word_underscore)



if guessing_letter in guessing_word:
    print(guessing_word[0])

# def the_game():
#     tries = 6
#     failed = 0
#     word_underscore = "______"
#     guessing_word = random.choice(guess_list).lower()
#     print(guessing_word, "2", "3")
#     # guessing_letter = str(input("Guess a letter: "))
#
#     for guessing_letter in guessing_word:
#         # guessing_letter = str(input("Guess a letter: "))
#         if guessing_letter not in guessing_word:
#             print("_")
#         print(guessing_letter)
#     else:
#         print("something")
#
#
#
#
#
# the_game()



listOrigin = ["c", "a", "r", "r", "o", "t"]
listMask = ["_", "_", "_", "_", "_", "_"]
gs_letter = str(input())

for item in listOrigin:
    if gs_letter in listOrigin:
        item = gs_letter
        print(listOrigin.index(item))
        break
    elif gs_letter not in listOrigin:
        print("fuck")



print(listOrigin)
print(listMask)
