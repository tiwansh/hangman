from random_words import RandomWords

rw = RandomWords()
word = rw.random_word()

#random word is generated and stored in word

#define states of hangman

maxStates = 6
#keep on taking inputs while the either wins or hangman reaches state 7
def printState(guesses):
	if guesses == 0:
		print "________      "
		print "|      |      "
		print "|             "
		print "|             "
		print "|             "
		print "|             "
	elif guesses == 1:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|             "
		print "|             "
		print "|             "
	elif guesses == 2:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /       "
		print "|             "
		print "|             "
	elif guesses == 3:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|      "
		print "|             "
		print "|             "
	elif guesses == 4:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|             "
		print "|             "
	elif guesses == 5:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|     /       "
		print "|             "
	else:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|     / \     "
		print "|             "
		print "The noose tightens around your neck, and you feel the"
		print "sudden urge to urinate."

#character guessed are stored in charGuesses list
charGuessed = []
charRight = []
state = 0

print word

while(True):
	print "Word length : ", len(word)
	if(len(charGuessed) != 0):
		print "Character guessed : ", charGuessed
	if(len(charRight) != 0):
		print "Right Characters guessed : ", charRight
 	ch = raw_input("Guess a character : ")
 	charGuessed.append(ch)
 	if(ch not in word):
 		state = state + 1
 		printState(state)
 	else:
 		charRight.append(ch)
 	if(len(charRight) == len(word)):
 		print "You Won !"
 		break
 	if(state == 6):
 		print "You Lost !"
 		break


