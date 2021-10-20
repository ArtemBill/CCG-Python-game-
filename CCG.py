# Описание правил игры
print("Winning Rules of the Color choice Game as follows:\n"
      "Enter a number from one to five and match computer choice to win the computer"
      "\n")

# Допустимые значение
print("red = 1\n"
      "yellow = 2\n"
      "orange = 3\n"
      "green = 4\n"
      "blue = 5\n"
      "take a turn:"
      "\n")

# Игрок выбирает валидное число. Выводим на экран его цвет
player_choice = int(input("Enter valid input: "))
if player_choice == 1:
    print("player color choice is: red")
elif player_choice == 2:
    print("player color choice is: yellow")
elif player_choice == 3:
    print("player color choice is: orange")
elif player_choice == 4:
    print("player color choice is: green")
elif player_choice == 5:
    print("player color choice is: blue")

print()

# Объясняем что следующим, цвет выбирает компъютер
print("Now its computer turn to choose a color.......")
import random

# Добавляем функцию для рандомного выбора цифр от 1 до 5
computer_choice = random.randrange(1, 5)
if computer_choice == 1:
    print("Computer color choice is: red")
elif computer_choice == 2:
    print("Computer color choice is: yellow")
elif computer_choice == 3:
    print("Computer color choice is: orange")
elif computer_choice == 4:
    print("Computer color choice is: green")
elif computer_choice == 5:
    print("Computer color choice is: blue")

# Сравниваем ответы игрока и компъютера. Если совпадают - игрок победил, нет - проиграл.
# За каждую партию засчитывается очко игроку или компъютеру
player_score = 0
computer_score = 0
if player_choice == computer_choice:
    print("player_score: ", int(player_score + 1), '\n'
          "computer_score: ", int(computer_score + 0))
elif player_choice != computer_choice:
    print("player_score: ", int(player_score + 0), '\n'
          "computer_score: ", int(computer_score + 1))

print("Do you want to play again?: (Y/N) ")
play_again_or_not = str(input())

if play_again_or_not == "Y" or play_again_or_not == "y":



