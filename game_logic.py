import random
from constants import CHOICES, WINNING_COMBINATIONS


def computer_choice():
    return random.choice(CHOICES)


def get_result(player, computer):
    if player == computer:
        return "Draw"

    if (player, computer) in WINNING_COMBINATIONS:
        return "You Win!"

    return "Computer Wins!"


def play_game(player):
    computer = computer_choice()
    result = get_result(player, computer)
    return computer, result