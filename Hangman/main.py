import random

class Hangman:
    wordList = ["car", "school", ]

    def chooseRandomWord(self):
        return random.choice(self.wordList)

    def makeAGuess(self):
        guess = ''
        conditionsMet = False
        while conditionsMet is False:
            guess = (input("Choose a letter:")).lower()
            if len(guess) == 1 and guess.isalpha():
                conditionsMet = True
            else:
                print("Please input single letter")
        return guess

    def calculateLength(self, word):
        encryptedWord = '_' * len(word)
        return encryptedWord

    def checkAGuess(self, word, letter, encrypted):
        encryptedWord = list(encrypted)
        returnString = ''
        for a in range(0, len(word)):
            if word[a] == letter:
                encryptedWord[a] = letter
        for b in encryptedWord:
            returnString += b
        return returnString



    def playGame(self):
        triesRemaining = 10
        currentGuess = ''
        currentWord = self.chooseRandomWord()
        encryptedWord = self.calculateLength(currentWord)

        while triesRemaining > 0 and encryptedWord != currentWord:
            print(encryptedWord)
            currentGuess = self.makeAGuess()
            triesRemaining -= 1
            encryptedWord = self.checkAGuess(currentWord, currentGuess, encryptedWord)
            print(f"You have {triesRemaining} tries remaining" )
        if triesRemaining <= 0:
            print("Sorry, you lost, the word was: " + currentWord)
        else:
            print("Congratulations, you won! The word was: " + currentWord)


game1 = Hangman()
game1.playGame()
