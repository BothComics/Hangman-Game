import random, time
from os import system

def main():
	system('mode con: cols=40 lines=17')
	cont = True
	gameCount = 1
	backgrounds = ['0', '1', '2', '3', '4', '5', '6', '7']
	foregrounds = ['9', 'A', 'B', 'C', 'D', 'E', 'F']
	gameStatesList = createGameStates()
	while cont == True:
		win = False
		lose = False
		incorrectGuesses = []
		word = randomWordSelect('allNouns.txt').upper()
		word = list(word)
		currentState = 0
		blankSpace = createBlankSpace(word)
		scoreCard = list(blankSpace)
		color = str(random.choice(backgrounds) + random.choice(foregrounds))
		system('color ' + color)
		system("TITLE Hangman Game: #" + str(gameCount))
		while win is False and lose is False:
			system('cls')
			print(gameStatesList[currentState])
			print(' '.join(scoreCard))
			print("Incorrect Letters: ", ', '.join(incorrectGuesses))
			currentGuess = letterGuess(incorrectGuesses, word)
			currentState = len(incorrectGuesses)
			if currentGuess[0] == None:
				print("currentGuess is None")
				pass
			if currentGuess == "QUIT":
				break
			elif currentGuess[0] == True:
				scoreCard = scorecardUpdate(scoreCard, word, currentGuess)
			if currentState >= 6:
				system('cls')
				print(gameStatesList[currentState])
				print(' '.join(scoreCard))
				print("Incorrect Letters: ", ', '.join(incorrectGuesses))
				print("Sorry, you lose :(")
				print("The word was: ", ''.join(word), '\n')
				lose = True
				playAgain = input("Would you like to play again? (Y / N) ").upper()
				gameCount += 1
				if playAgain != 'Y':
					cont = False
			elif '_' not in scoreCard:
				system('cls')
				print(gameStatesList[currentState])
				print(' '.join(scoreCard))
				print("Incorrect Letters: ", ', '.join(incorrectGuesses))
				print("Congratulations, you won!")
				for i in range(15):
					color = str(random.choice(backgrounds) + random.choice(foregrounds))
					system('color ' + color)
					time.sleep(0.2)
				win = True
				playAgain = input("Would you like to play again? (Y / N) ").upper()
				gameCount += 1
				if playAgain != 'Y':
					cont = False
		
def createGameStates():	
	gameState1 = """
		 ,---
		     |
		     |
		    _|_
		   /___\\
	"""
	gameState2 = """
		 ,---
		 O   |
		     |
		    _|_
		   /___\\
	"""
	gameState3 = """
		 ,---
		 O   |
		 |   |
		    _|_
		   /___\\
	"""
	gameState4 = """
		 ,---
		 O   |
	\t/|   |
		    _|_
		   /___\\
	"""
	gameState5 = """
		 ,---
		 O   |
	\t/|\  |
		    _|_
		   /___\\
	"""
	gameState6 = """
		 ,---
		 O   |
	\t/|\  |
	\t/   _|_
		   /___\\
	"""
	gameState7 = """
		 ,---
		 O   |
	\t/|\  |
	\t/\  _|_
		   /___\\
	"""
	return [gameState1, gameState2, gameState3,
		gameState4, gameState5, gameState6, gameState7]

def randomWordSelect(wordFile):
	wordsList = []
	selectedWord = ''
	infile = open(wordFile, 'r')
	for line in infile:
		line = line.strip('\n')
		if '-' in line:
			pass
		elif line[0].isupper():
			pass
		else:
			wordsList.append(line)
	infile.close()
	selectedWord = wordsList[random.randint(0, len(wordsList))]
	return selectedWord
	
def createBlankSpace(word):
	wordLen = len(word)
	blankSpace = ('_' * wordLen)
	return blankSpace

def letterGuess(incorrectGuesses, word):
	guess = input("Guess a letter:   ").upper()
	if guess == "QUIT":
		return guess
	elif len(guess) != 1 or guess.isalpha() == False or guess in incorrectGuesses:
		print("That is not a possible letter:   ")
		return None, guess, incorrectGuesses
	elif guess not in word:
		incorrectGuesses.append(guess)
		return False, guess, incorrectGuesses
	elif guess in word:
		return True, guess, incorrectGuesses

def scorecardUpdate(scoreCard, word, currentGuess):
	for i, item in enumerate(word):
		if str(item) == str(currentGuess[1]):
			scoreCard[i] = currentGuess[1]
	return scoreCard


main()