import random
print("***************TIC TAC TOE***************\n")

class TicTacToe:
    def __init__(self, player:str = None, computer:str = None):
        self.player = player
        self.computer = computer
        self.playerWin = None
        self.computerWin = None
        self.isDraw = None
        self.grid = [["","",""],
                     ["","",""],
                     ["","",""]]
    
    def printGrid(self):
        print(f"\t{self.grid[0][0]}\t|\t{self.grid[0][1]}\t|\t{self.grid[0][2]}\t")
        print(f"----------------|---------------|---------------")
        print(f"\t{self.grid[1][0]}\t|\t{self.grid[1][1]}\t|\t{self.grid[1][2]}\t")
        print(f"----------------|---------------|---------------")
        print(f"\t{self.grid[2][0]}\t|\t{self.grid[2][1]}\t|\t{self.grid[2][2]}\t")
    
    def checkWinner(self, character):
        if character == self.player:
            self.playerWin = True
        elif character == self.computer:
            self.computerWin = True

    def status(self, count, length):
        diagonal_left = 0
        diagonal_right = 2
        d_l = []
        d_r = []

        for i in range(len(self.grid)):
            ROW = []
            COL = []
            
            d_l.append(self.grid[i][diagonal_left])
            d_r.append(self.grid[i][diagonal_right])
            
            diagonal_left+=1
            diagonal_right-=1
            
            for j in range(len(self.grid[i])):
                ROW.append(self.grid[i][j])
                COL.append(self.grid[j][i])
            if(ROW[0]!="" and [ROW[0]]*len(ROW) == ROW):
                self.checkWinner(ROW[0])
            if(COL[0]!="" and [COL[0]]*len(COL) == COL):
                self.checkWinner(COL[0])
            
        if(d_l[0]!="" and [d_l[0]]*len(d_l) == d_l):
                self.checkWinner(d_l[0])
        if(d_r[0]!="" and [d_r[0]]*len(d_r) == d_r):
                self.checkWinner(d_r[0])
        if count >= length ** 2:
            self.isDraw = True
        
    def playerTurn(self):
        print("Player turn!")
        while True:
            pPos = input("Enter player position \"row col\": ")
        
            try:
                row, col = map(int, pPos.split())
            except ValueError:
                print("Please enter a number between 0 and 2 in this format: row column\n(for e.g., if you want to insert at top left corner, use: 0 0)")
                continue

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Please enter a number between 0 and 2")
                continue
            elif self.grid[row][col] in ["x", "o"]:
                print("A character already exists!")
                print(f"Character: {self.grid[row][col]}")
                continue
            else:

                self.grid[row][col] = self.player
                
                self.printGrid()
                break

    def computerTurn(self):
        print("computer's turn!")
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if self.grid[row][col] in ["x", "o"]:
                continue
            else:
                self.grid[row][col] = self.computer
                
                self.printGrid()
                break

    def game(self, playerTurn):
        count = 0
        if playerTurn == True:
            while count < len(self.grid) ** 2:
                print(f"count: {count}")
                self.playerTurn()
                count += 1
                self.status(count, len(self.grid))
                if self.playerWin:
                    print("You win!")
                    break
                elif self.computerWin:
                    print("You lose!")
                    break
                if self.isDraw:
                    print("DRAW!")
                    break
                self.computerTurn()
                self.status(count, len(self.grid))
                count += 1
                if self.playerWin:
                    print("You win!")
                    break
                elif self.computerWin:
                    print("You lose!")
                    break
                if self.isDraw:
                    print("DRAW!")
                    break
        else:
            while count < len(self.grid) ** 2:
                print(f"count: {count}")
                self.computerTurn()
                count += 1
                self.status(count, len(self.grid))
                if self.playerWin:
                    print("You win!")
                    break
                elif self.computerWin:
                    print("You lose!")
                    break
                if self.isDraw:
                    print("DRAW!")
                    break
                self.playerTurn()
                self.status(count, len(self.grid))
                count += 1
                if self.playerWin:
                    print("You win!")
                    break
                elif self.computerWin:
                    print("You lose!")
                    break
                if self.isDraw:
                    print("DRAW!")
                    break

    def start(self):
        while True:
            playerStart = input("Player start?: ").lower()
            if playerStart in ["yes", "y"]:
                print("Player starts first!")
                self.game(True)
                break
                
            elif playerStart in ["no", "n"]:
                print("Computer goes first!")
                self.game(False)
                break
            else:
                print("Please say yes or no")
                continue


def main():
    game = TicTacToe()
    while True:
        char = input("Input player character: ").lower()
        if char == "x":
            print(f"You are {char}")
            print(f"Opponent is o")

            game.player = char
            game.computer = "o"
            game.start()
            break

        elif char == "o":
            print(f"You are {char}")
            print(f"Opponent is x")

            game.player = char
            game.computer = "x"
            game.start()
            break

        elif char == "q":
            print(f"QUIT!")
            break
        else:
            print("That's not a valid character")
            continue

if __name__ == '__main__':
    main()