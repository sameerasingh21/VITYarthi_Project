import tkinter as tk
from game_logic import play_game
from utils import update_score, reset_score
from constants import SNAKE, WATER, GUN


def create_gui(root):
    score = {
        "player": 0,
        "computer": 0
    }

    title = tk.Label(
        root,
        text="Snake Water Gun",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    result_label = tk.Label(
        root,
        text="Choose your move!",
        font=("Arial", 16)
    )
    result_label.pack(pady=10)

    computer_label = tk.Label(
        root,
        text="Computer: -",
        font=("Arial", 14)
    )
    computer_label.pack(pady=5)

    score_label = tk.Label(
        root,
        text="You: 0   Computer: 0",
        font=("Arial", 14)
    )
    score_label.pack(pady=10)

    def choose(choice):
        computer, result = play_game(choice)

        update_score(result, score)

        result_label.config(
            text=f"You chose: {choice}\n{result}"
        )

        computer_label.config(
            text=f"Computer chose: {computer}"
        )

        score_label.config(
            text=f"You: {score['player']}   Computer: {score['computer']}"
        )

    def reset():
        reset_score(score)

        result_label.config(
            text="Choose your move!"
        )

        computer_label.config(
            text="Computer: -"
        )

        score_label.config(
            text="You: 0   Computer: 0"
        )

    tk.Button(
        root,
        text="Snake",
        width=15,
        command=lambda: choose(SNAKE)
    ).pack(pady=5)

    tk.Button(
        root,
        text="Water",
        width=15,
        command=lambda: choose(WATER)
    ).pack(pady=5)

    tk.Button(
        root,
        text="Gun",
        width=15,
        command=lambda: choose(GUN)
    ).pack(pady=5)

    tk.Button(
        root,
        text="Reset",
        width=15,
        command=reset
    ).pack(pady=15)