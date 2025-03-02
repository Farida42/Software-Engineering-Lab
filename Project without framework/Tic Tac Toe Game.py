from tkinter import *
import random


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))

        elif check_winner() is True:
            label.config(text=(player + " wins"))

        elif check_winner() == "Tie":
            label.config(text="Tie!")


def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="lightgreen")
            buttons[row][1].config(bg="lightgreen")
            buttons[row][2].config(bg="lightgreen")
            return True

    # Check columns
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="lightgreen")
            buttons[1][column].config(bg="lightgreen")
            buttons[2][column].config(bg="lightgreen")
            return True

    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[2][2].config(bg="lightgreen")
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[2][0].config(bg="lightgreen")
        return True

    # Check for tie
    if empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="lightyellow")
        return "Tie"

    return False


def empty_spaces():
    return any(buttons[row][column]['text'] == "" for row in range(3) for column in range(3))


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="white")


# Tkinter window setup
window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="lightblue")

players = ["X", "O"]
player = random.choice(players)

# Title Label
title_label = Label(window, text="Welcome to Tic-Tac-Toe", font=("Arial", 20), bg="lightblue")
title_label.pack(side="top", pady=10)

# Turn Label
label = Label(window, text=player + " turn", font=('Consolas', 20), bg="lightblue")
label.pack(side="top")

# Restart Button
reset_button = Button(window, text="Restart Game", font=('Consolas', 15), command=new_game, bg="lightcoral")
reset_button.pack(side="top", pady=5)

# Game Board Frame
frame = Frame(window)
frame.pack()

buttons = [[None] * 3 for _ in range(3)]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Consolas', 30), width=5, height=2, bg="white",
                                      command=lambda r=row, c=column: next_turn(r, c))
        buttons[row][column].grid(row=row, column=column, padx=5, pady=5)

window.mainloop()
