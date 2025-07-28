
#print welcome message
# print("Welcome to Connect Four!")
# print("Players will take turns dropping tokens into columns.")
# print("The first player to connect four tokens in a row (horizontally, vertically, or diagonally) wins!")

#establish tokens
# player1Token = input(f'{player1Name}, choose your token (X or O): ').upper()
# player2Token = 'O' if player1Token == 'X' else 'X'
#establish who is going first/current player - 
# currentPlayer = input(f'Who goes first? ({player1Name} or {player2Name}): ').strip()
# currentToken = player1Token if currentPlayer == player1Name else player2Token
# print('Wonderful! Let\'s start the game!')

#initialize the board and create a 2D list to represent the board
tokens = ['O', 'X']
rows = 6
columns = 7
board = [[' ' for _ in range(columns)] for _ in range(rows)] 

player1 = 'Player 1'
player2 = 'Player 2'
player1Token = 'X'
player2Token = 'O'

currentPlayer = player1
currentToken = 'X' if currentPlayer == player1 else '0'

gameStatus = True

#print formatted board
def print_board():
  #Column numbers
  print('  1 2 3 4 5 6 7')

  #Each row with a border
  for row in board:
    print('| ' + ' '.join(row) + " |")

  #Bottom border
  print('+' + '-' * (columns * 2 - 1) + '+')  

#add token to the board
def drop_token(col):
    #find the lowest empty row in the selected column / start from the 'bottom'
    for row_index in range(len(board) -1, -1, -1):
       if(board[row_index][col] == ' '):
          board[row_index][col] = currentToken
          return row_index
    return False  

#get input
def get_player_input():
  while True:
    colStr = input(f'{currentPlayer}, where would you like to place your token? (Col #)')
    if colStr.isdigit():
      colNum = int(colStr)
      if colNum >= 1 and colNum <= 7:
          return colNum - 1
      else:
          print('Please enter a number between 1-7')
    else:
       print('Please enter a valid number between 1-7')

#win detection
def detect_win(col, row):
   #horizontal
   #convert row into a searchable string
   row = ''.join(board[row])
   #check if 'XXXX' or 'OOOO' is in row_string
   if currentToken * 4 in row:
    return True
   #verticle 
   #create column and then make it into a searchable string
   column = ''.join([board[rowIndex][col] for rowIndex in range(rows)])
   if currentToken * 4 in column:
        return True
   #diagonal (ascending)
   #[5, 0] [4, 1] [3, 2] [2, 3] [1, 4] [0, 5]
   asc_diag = ''.join()





   #diagonal (descending)

# while gameStatus:
#    #prompt player for input and get number
   columnIndex = get_player_input()
#    #drop the token once column is assigned an int
   rowIndex = drop_token(columnIndex)
#    #alternate players
#    nextPlayer = player2 if currentPlayer == player1 else player1
#    currentPlayer = nextPlayer
#    #print the board
   print_board()




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