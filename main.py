# ----- board basics ----- #
rows = 6
columns = 7
board = [['_' for _ in range(columns)] for _ in range(rows)] 
#determines the status of the game (True = ongoing)
game_status = True

# ---------------------------- player information ---------------------------- #
player_1 = 'Player 1'
player_2 = 'Player 2'
player_1_token = 'X'
player_2_token = 'O'
current_player = player_1
current_token = 'X' if current_player == player_1 else '0'

# ------------------------------ game functions ------------------------------ #
#print formatted board
def print_board():
  print('   1 2 3 4 5 6 7') #column #s
  for rowIndex, row in enumerate(board): #formatted rows
    print(f'{rowIndex}| {' '.join(row)} |') 
  print(f'+{'-' * (columns * 2 + 2)}+') #formatted bottom border 

#get and validate player input
def get_player_input():
  while True:
    colStr = input(f'{current_player}, where would you like to place your token? (choose a column #)')
    if colStr.isdigit():
      colNum = int(colStr)
      return colNum - 1 if colNum >= 1 and colNum <= 7 else print('Please enter a number between 1-7')
    else:
      print('Please enter a valid number between 1-7')

#add token to the board
def drop_token(col):
    #find the lowest empty row in the selected column / start from the 'bottom'
    for row_index in range(len(board) -1, -1, -1):
      if(board[row_index][col] == ' '):
          board[row_index][col] = current_token
          return row_index
    return False  

#win detection
def detect_win(row, col):
  win_combo = current_token * 4

  horizontal_row = ''.join(board[row])
  vertical_col = ''.join([board[rowIndex][col] for rowIndex in range(rows)])
  asc_diag = ''.join(board[rowIndex][(row + col) - rowIndex] for rowIndex in range(rows) if 0 <= (row + col) - rowIndex < columns)
  desc_diag = ''.join(board[rowIndex][rowIndex - (row - col)] for rowIndex in range(rows) if 0 <= rowIndex - (row - col) < columns)
  
  return win_combo in vertical_col or win_combo in horizontal_row or win_combo in asc_diag or win_combo in desc_diag

#draw detection
def detect_draw():
  return any(' ' in row for row in board)  

def set_game_status(row, col):
   if detect_win(row, col):
      print('Way to go!')
      game_status = False
   elif detect_draw():
      print('So sad. No-one wins')  
      game_status = False

#print welcome message
print('Welcome to Connect Four! Players will take turns dropping tokens into columns.')
print('The first player to connect four tokens in a row (horizontally, vertically, or diagonally) wins!')


#establish tokens
# player_1_token = input(f'{player_1Name}, choose your token (X or O): ').upper()
# player_2_token = 'O' if player_1_token == 'X' else 'X'
#establish who is going first/current player - 
# current_player = input(f'Who goes first? ({player_1Name} or {player_2Name}): ').strip()
# current_token = player_1_token if current_player == player_1Name else player_2_token
# print('Wonderful! Let\'s start the game!')
#game play
while game_status:
   #prompt player for input and get number
   columnIndex = get_player_input()
   #drop the token once column is assigned a valid int
   rowIndex = drop_token(columnIndex)

   print_board()

   set_game_status(rowIndex, columnIndex)

   if not game_status: current_player = player_2 if current_player == player_1 else player_1




#Edge cases to look out for:
  #Response if player inputs a column that is full
  #Response if player inputs an invalid column (not an integer between 1-7)

#Current laginappe:
  #Add ability for players to choose the board size (default 7x6)
  #Add ability for player to exit and restart the game at any time
  #Add ability for players to choose their tokens (X or O)
  #Add ability for players to choose who goes first
  #Add ability for players to choose their name