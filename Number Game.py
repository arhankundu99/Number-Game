import tkinter
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'Purple', 'Brown']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
signs = ['+', '-', '*', '%']
# initial score
score = 0
# the game time left, initially 30 seconds.
timeleft = 30


# function that will start the game.This function is called every time the enter key is pressed
def startGame(event):
    if timeleft == 30:
        # starting the countdown timer.
        countdown()
    # running this function to get next expression
    getNextExpression()


# Function to choose and display the next expression.
def getNextExpression():

    global score
    if timeleft > 0:
        userInputBox.focus_set()

        # if the colour typed is equal to the colour of the text
        string = ''
        if signs[0] == '+':
            string = str(numbers[0]+numbers[1])
        if signs[0] == '-':
            string = str(numbers[0]-numbers[1])
        if signs[0] == '*':
            string = str(numbers[0]*numbers[1])
        if signs[0] == '%':
            string = str(numbers[0]%numbers[1])

        if userInputBox.get().lower() == string:
            score += 1

        # clearing the text entry box.
        userInputBox.delete(0, tkinter.END)

        random.shuffle(colours)
        random.shuffle(numbers)
        random.shuffle(signs)

        # changing the colour to type, by changing the text and the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(numbers[0])+signs[0]+str(numbers[1]))

        # updating the score.
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeleft

    # if the game is in play
    if timeleft > 0:
        # decrementing the timer.
        timeleft -= 1

        # updating the time left label
        timeLabel.config(text="Time left: "
                              + str(timeleft))

        # running the function again after 1 second.
        timeLabel.after(1000, countdown)
    # Driver Code

# creating a GUI Window
root = tkinter.Tk()

# setting the title
root.title("NUMBER GAME")

# setting the size
root.geometry("500x300")

# adding an instructions label
instructions = tkinter.Label(root, text="Type in the results of the arithmetic expression", font=('Helvetica', 12))

# the pack method packs widgets in rows or columns.
instructions.pack()

# adding a score label
scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Bold', 12))
scoreLabel.pack()

# adding a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

# adding a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# adding a text entry box for typing in colours
userInputBox = tkinter.Entry(root)
# running the 'startGame' function when the enter key is pressed
root.bind('<Return>', startGame)
userInputBox.pack()

# setting focus on the entry box
userInputBox.focus_set()

# starting the GUI
root.mainloop()
