from Tkinter import *
from random_words import RandomWords

rw = RandomWords()
word = rw.random_word()

#random word is generated and stored in word
charGuessed = []
charRight = []
state = 0

print word
wordList = list(word)
#define states of hangman
wordAnswer = []
for i in range(len(word)):
	wordAnswer.append('_')

maxStates = 6
#keep on taking inputs while the either wins or hangman reaches state 7
def printState(guesses):
	mySting = ""
	if guesses == 1:
		myString = "________      "
		myString  = myString + '\n' + "|      |      "
		myString  = myString + '\n' + "|             "
		myString  = myString + '\n' + "|             "
		myString  = myString + '\n' + "|             "
		myString  = myString + '\n' + "|             "
	elif guesses == 2:
		myString  = "________      "
		myString  = myString + '\n' + "|      |      "
		myString  = myString + '\n' + "|      0      "
		myString  = myString + '\n' + "|             "
		myString  = myString + '\n' + "|             "
		myString  = myString + '\n' + "|             "
	elif guesses == 3:
		myString  = "________      "
		myString  = myString + '\n' + "|      |      "
		myString  = myString + '\n' + "|      0      "
		myString  = myString + '\n' + "|     /       "
		myString  = myString + '\n' + "|             "
		myString  = myString + '\n' + "|             "
	elif guesses == 4:
		myString  = "________      "
		myString  = myString + "\n" + "|      |      "
		myString  = myString + '\n' + "|      0      "
		myString  = myString + '\n' + "|     /|      "
		myString  = myString + '\n' + "|             "
		myString  = myString + '\n' + "|             "
	elif guesses == 5:
		myString = "________      "
		myString  = myString + '\n' + "|      |      "
		myString  = myString + '\n' + "|      0      "
		myString  = myString + '\n' + "|     /|\     "
		myString  = myString + '\n' + "|             "
		myString  = myString + '\n' + "|             "
	elif guesses == 6:
		myString = "________      "
		myString  = myString + '\n' + "|      |      "
		myString  = myString + '\n' + "|      0      "
		myString  = myString + '\n' + "|     /|\     "
		myString  = myString + '\n' + "|     /       "
		myString  = myString + '\n' + "|             "
	else:
		myString= "________      "
		myString  = myString + '\n' + "|      |      "
		myString  = myString + '\n' + "|      0      "
		myString  = myString + '\n' + "|     /|\     "
		myString  = myString + '\n' + "|     / \     "
		myString  = myString + '\n' + "|             "
		myString  = myString + '\n' + "The noose tightens around your neck, and you feel the"
		myString  = myString + '\n' + "sudden urge to urinate."
	vHangman.set(myString)

#character guessed are stored in charGuesses list

def kaam():
	global state
	char_entered = enteredChar.get()
	# define characters
	charGuessed.append(char_entered)
	if(char_entered not in word):
 		state = state + 1
 		printState(state)
 	else:
 		charRight.append(char_entered)
 		#add it to word
 		for i in range(len(wordList)):
 			if(char_entered == wordList[i]):
 				wordAnswer[i] = char_entered
 	if(len(charGuessed) != 0):
		vAll.set("Character guessed : " + str(charGuessed))
	if(len(charRight) != 0):
		#create word
		vCorrect.set("Right Characters guessed : " + str(wordAnswer))
 	if(set(wordAnswer) == set(wordList)):
 		vResult.set("You Won !")
 	if(state == 6):
 		vResult.set("You Lost !") 			


root = Tk()
root.title("Hangman : The guessing game")
root.geometry('500x500')
root.configure(background = 'green')

topFrame = Frame(root, bg= "blue", bd = 5)
topFrame.pack(side= TOP)
#create a label in topframe toshow the status of hangman
vHangman = StringVar()
displayHangman = Label(topFrame, textvariable = vHangman)
displayHangman.pack()


charFrame = Frame(root,bg = "red")
charFrame.pack()

#crete a label for entry of the characters
labelFrame= Label(charFrame, text = "Enter a character : ")
labelFrame.pack(side= LEFT)

#create an char entry  
enteredChar = Entry(charFrame, bd= 5)
enteredChar.pack(side=RIGHT)

#create a button frame too
button = Button(root, text = "Check",fg = "Green", bd = 4, activebackground = "Blue", activeforeground = "White", command = kaam, relief = RAISED)
button.pack()


vAll = StringVar()
display1Frame = Label(root, textvariable = vAll)
display1Frame.pack()

vCorrect = StringVar()
display2Frame= Label(root, textvariable = vCorrect)
display2Frame.pack()

vResult = StringVar()
displayResultFrame = Label(root, textvariable = vResult)
displayResultFrame.pack()

root.mainloop()