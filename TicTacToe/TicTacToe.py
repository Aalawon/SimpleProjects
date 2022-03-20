import random


class TicTacToe:
    def __init__(self):
        self.isRunning = True

    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '], ]

    isRunning = True

    def displayBoard(self):
        for a in range(0, 3):
            print("-------------")
            print("| " + self.board[a][0] + " | " + self.board[a][1] + " | " + self.board[a][2] + " |")
        print("--------------")

    def playTurn(self, cordX, cordY, symbol):
        if cordX > len(self.board) or cordY > len(self.board[0]):
            print("Incorrect coordinates!")
        else:
            if self.board[cordX][cordY] == ' ':
                self.board[cordX][cordY] = symbol

            else:
                print("This space is already taken!")
        self.displayBoard()
        self.checkForWinner()

    def checkForWinner(self):
        # check horizontally
        for a in range(0, 3):
            if self.board[a][0] == self.board[a][1] == self.board[a][2] and self.board[a][0] != ' ':
                print(self.board[a][0] + " Won!")
                self.isRunning = False
        # check vertically
        for b in range(0, 3):
            if self.board[0][b] == self.board[1][b] == self.board[2][b] and self.board[0][b] != ' ':
                print(self.board[0][b] + " Won!")
                self.isRunning = False
        # check diagonally
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            print(self.board[0][0] + " Won!")
            self.isRunning = False

        if self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
            print(self.board[0][0] + " Won!")
            self.isRunning = False

    def aiChoosePosition(self):
        X = random.randint(0, 2)
        Y = random.randint(0, 2)
        while self.board[X][Y] != ' ':
            X = random.randint(0, 2)
            Y = random.randint(0, 2)
        self.playTurn(X, Y, 'O')

    def game(self):
        while self.isRunning is True:
            posX = int(input("Input your position X"))
            posY = int(input("Input your position Y"))
            self.playTurn(posX, posY, "X")
            self.aiChoosePosition()

currentGame = TicTacToe()
currentGame.game()
