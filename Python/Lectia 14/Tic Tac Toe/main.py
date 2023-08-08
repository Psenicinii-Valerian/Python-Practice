from tkinter import *
import random

                                            # GUI Elements Functions
def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + "'s turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+ " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + "'s turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")


def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)

    label.config(text=player + "'s turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#E6E6FA")


app = Tk()
app.configure(bg="#E6E6FA")

app.title("Tic Tac Toe")
# app.title() - metoda ce ne permite sa indicam titlul aplicatiei noastre

# Get the screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Set the app window's geometry to the maximum screen size
app.geometry(f"{screen_width}x{screen_height}")

players = ["x", "o"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + "'s turn", font=('consolas', 40), bg="#CBC3E3")
label.pack(pady=25, side="top")
# side="top" - prin acest keyword, vom seta automat pozitia label-ului nostru label
# ca fiind in partea de centru, sus a ferestrei noastre principale app

reset_button = Button(text="Restart game", font=('consolas', 20), bg="#CCCCFF", relief="groove", command=new_game)
reset_button.pack(side="top")

frame = Frame(app)
frame.pack(padx=5, pady=50)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), bg="#E6E6FA", width=5, height=2, relief="groove",
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

app.mainloop()