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
def player_game():
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
    return player_choice

player = player_game()

print()

# Объясняем что следующим, цвет выбирает компъютер. Импортируем рандом
print("Now its computer turn to choose a color.......")
import random

# Добавляем функцию для рандомного выбора цифр от 1 до 5
def computer_game():
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
    return computer_choice

computer = computer_game()


# Сравниваем ответы игрока и компъютера. Если совпадают - игрок победил, нет - проиграл.
# За каждую партию засчитывается очко игроку или компъютеру
player_score = 0
computer_score = 0
def compare_results():
    print(player, computer)
    global player_score
    global computer_score
    if player == computer:
        player_score += 1
        print("player_score: ", player_score, '\n'
        "computer_score: ", computer_score)
    elif player != computer:
        computer_score += 1
        print("player_score: ", player_score, '\n'
        "computer_score: ", computer_score )


compare_results()

# Спрашиваем игрока хочет ли он сыграть ещё раз
# print("Do you want to play again?: (Y/N) ")
# play_again_or_not = str(input())
def restart_or_exit():
    global player
    global computer
    print("Do you want to play again?: (Y/N) ")
    play_again_or_not = str(input())
    while play_again_or_not == "Y" or play_again_or_not == "y":
        print()
        # player_choice = int(input("Enter valid input: "))

        player = player_game()
        print("Now its computer turn to choose a color.......")

        computer = computer_game()
        compare_results()
        print("Do you want to play again?: (Y/N) ")
        play_again_or_not = str(input())
    if play_again_or_not == "N" and player_score < computer_score:
        print()
        print("<== Computer wins ==>", "\n",
              "Player is Defeated", "\n",
              "Thanks for playing")
    elif play_again_or_not == "N" and player_score > computer_score:
        print()
        print("<== Player wins ==>", "\n",
              "Computer is Defeated", "\n",
              "Thanks for playing")



restart_or_exit()



