import tkinter as tk
from tkinter import messagebox


def check_winner():
    for row in board:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            highlight_winner(row)
            return True

    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != "":
            highlight_winner([board[i][col] for i in range(3)])
            return True

    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        highlight_winner([board[i][i] for i in range(3)])
        return True

    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        highlight_winner([board[i][2 - i] for i in range(3)])
        return True

    return False


def highlight_winner(winning_cells):
    for cell in winning_cells:
        cell.config(bg="lightgreen")
    messagebox.showinfo("Game Over", f"Player {player} wins!")
    reset_board()


def pressed(r, c):
    global player
    if board[r][c]["text"] == "" and not check_winner():
        board[r][c]["text"] = player
        if check_winner():
            return
        player = "O" if player == "X" else "X"
        label.config(text=f"Player {player}'s turn")


def reset_board():
    global player
    for row in board:
        for cell in row:
            cell.config(text="", bg="white")
    player = "X"
    label.config(text="Player X's turn")


root = tk.Tk()
root.title("Tic-Tac-Toe")

player = "X"
board = [[None] * 3 for _ in range(3)]
label = tk.Label(root, text="Player X's turn", font=("Arial", 14))
label.pack()

frame = tk.Frame(root)
frame.pack()

for r in range(3):
    for c in range(3):
        board[r][c] = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                                command=lambda r=r, c=c: pressed(r, c))
        board[r][c].grid(row=r, column=c)

reset_button = tk.Button(root, text="Reset", command=reset_board, font=("Arial", 12))
reset_button.pack()

root.mainloop()
