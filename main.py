#print welcome message

# print("Welcome to Connect Four!")
# print("Players will take turns dropping tokens into columns.")
# print("The first player to connect four tokens in a row (horizontally, vertically, or diagonally) wins!")

#establish player names and tokens
# player1Name = input("Enter name for Player 1: ")
# player2Name = input("Enter name for Player 2: ")
# player1Token = input(f"{player1Name}, choose your token (X or O): ").upper()
# player2Token = 'O' if player1Token == 'X' else 'X'

#establish who is going first/current player
# currentPlayer = input(f"Who goes first? ({player1Name} or {player2Name}): ").strip()

# print("Wonderful! Let's start the game!")

#initialize the board
rows = 6
columns = 7
# Create a 2D list to represent the board
board = [[' ' for _ in range(columns)] for _ in range(rows)] 

def print_board(board):
  #Column numbers
  print("  1 2 3 4 5 6 7")

  #Each row with a border
  for row in board:
    print('| ' + " ".join(row) + " |")

  #Bottom border
  print("+" + "-" * (columns * 2 + 1) + "+")  




#For each turn:
  #print instruction specific to player  
  #get input from player
  #check if input is valid (1-7)
  #find the lowest empty row in the selected column
  #place the player's specific token in that row

#print board

#After each turn:
  #check if the player has won - horizontal, vertical, or diagonal (both directions)
    #if player has won, print winning message and exit
    #else, reprint the board
  #check if the game is a draw - if all columns are full
    #if draw, print draw message and exit
    #check if the game is still ongoing
      #if ongoing, continue to next player's turn
  #else continue to next player's turn

#Edge cases to look out for:
  #Response if player inputs a column that is full
  #Response if player inputs an invalid column (not an integer between 1-7)

#Current laginappe:
  #Add ability for players to choose the board size (default 7x6)
  #Add ability for player to exit and restart the game at any time
  #Add ability for players to choose their tokens (X or O)
  #Add ability for players to choose who goes first
  #Add ability for players to choose their name