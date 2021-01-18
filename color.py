#Type the colour and not the word
#from usingpython.com

#import the modules we need, for creating a GUI...
from tkinter import *
from tkinter import messagebox
import tkinter
import random

#a function that will start the game.
def startGame():
	if timeleft == 60:
		#start the countdown timer.
		countdown()
		random.shuffle(colours)
		#change the colour to type, by changing the text _and_ the colour to a random colour value
		label.config(fg=str(colours[1]), text=str(colours[0]))
		#run the function to choose the next colour.
		e.bind('<Return>', nextColour)

#function to choose and display the next colour.
def nextColour(event):
	#use the variables as globally declared.
	global score
	global timeleft
	global colors
	global mistake
	colors +=1
	#if a game is currently in play.
	if timeleft > 0:
		#...make the text entry box active.
		e.focus_set()
		#if the colour typed is equal to the colour of the text...
		if e.get().lower() == colours[1].lower():
			print (e.get().lower())
			#...add one to the score.
			score += 1
		else:	
			mistake +=1
		if e.get().lower() == '':
			mistake =0
			colors =0
		#clear the text entry box.
		e.delete(0, tkinter.END)
		#shuffle the list of colours.
		random.shuffle(colours)
		#change the colour to type, by changing the text _and_ the colour to a random colour value
		label.config(fg=str(colours[1]), text=str(colours[0]))

		#update the values or score.
		colorLabel.config(text="Colors Count: " + str(colors))
		errorLabel.config(text="Mistake: " + str(mistake))
		scoreLabel.config(text="Score: " + str(score))

#a countdown timer function. 
def countdown():
	global timeleft	#if a game is in play...
	if timeleft > 0:
		#decrement the timer.
		timeleft -= 1
		#update the time left label.
		timeLabel.config(text="Time left: " + str(timeleft))
		#run the function again after 1 second.
		timeLabel.after(1000, countdown)

#This function is to reset the game
def resetGame():
	global timeleft, score
	timeleft = 60
	score=0
	colors=0
	mistake=0
	colorLabel.config(text="Colors Count: " + str(colors))
	errorLabel.config(text="Mistake: " + str(mistake))
	scoreLabel.config(text="Score: " + str(score))
	label.config(text='')
	timeLabel.config(text="Time left : " + str(timeleft))
	e.delete(0, tkinter.END)

def main():
	global timeLabel, root
	global e, label, colorLabel, scoreLabel, errorLabel	
	#create a GUI window.
	root = tkinter.Tk()
	#set the title.
	root.title("SPEED COUNT")
	#set the size.
	root.geometry("400x300")

	#add an instructions label.
	instructions = tkinter.Label(root, text="Type the colour of the words in the box, and not the word text!", font=('Times New Roman', 12))
	instructions.pack()

	#add a score label.
	scoreLabel = tkinter.Label(root, text="Score", font=('Helvetica', 12), fg='Green')
	scoreLabel.pack()

	#add a color label.
	colorLabel = tkinter.Label(root, text="Color count", font=('Helvetica', 12), fg='blue')
	colorLabel.pack()

	#add a color label.
	errorLabel = tkinter.Label(root, text="Error count", font=('Helvetica', 12), fg='red')
	errorLabel.pack()

	#add a time left label.
	timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
	timeLabel.pack()

	#add a label for displaying the colours.
	label = tkinter.Label(root, font=('Helvetica', 60))
	label.pack()

	#add buttons for game start and reset
	btn_frame = Frame(root, width= 80, height = 40, bg= 'red')
	btn_frame.pack(side = BOTTOM)
	start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "Green", bd = 0,padx = 20, pady = 10 , command = startGame)
	start_button.grid(row=0, column= 0)
	reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "orange", bd = 0,padx = 20, pady = 10 , command = resetGame)
	reset_button.grid(row=0, column= 1)

	#add a text entry box for typing in colours.
	e = tkinter.Entry(root)
	e.pack()
	#set focus on the entry box.
	e.focus_set()

	#start the GUI
	root.mainloop()

# Main function
if __name__ == "__main__":
	#the list of possible colour.
	colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
	#the player's score, initially 0.
	score=0
	colors=0
	mistake=0
	#the game time left, initially 60 seconds.
	timeleft=60
	main()
