# ------------------------------- Constants / Repeated Messages ------------------------------- #
YES_NO_PROMPT = "Please enter Yes/No"
PLAYER_PROMPT = "Would you like to choose your name? Yes/No"
NAME_PROMPT = "What would you like your name to be?"
TOKEN_PROMPT = "Would you like to choose your token? Yes/No"
TYPE_OF_TOKEN_PROMPT = "What would you like your token to be? You may choose X/O"

VALID_YES = ['YES', 'Y', 'TRUE', '1']
VALID_NO = ['NO', 'N', 'FALSE', '0']

class Player: 
  def __init__(self, name, token):
    self.name = name
    self.token = token 
class ConnectFour:
  def __init__(self, player_1, player_2, rows=6, cols=7):
    self.rows = rows
    self.cols = cols 
    self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)] 
    self.player_1 = player_1 
    self.player_2 = player_2
    self.current_player = self.player_1 
    self.current_token = self.player_1.token if self.current_player == self.player_1 else self.player_2.token
    self.game_active = True
    self.win_combo = self.current_token * 4
  
  def __repr__(self):
    print('   1 2 3 4 5 6 7') #column #s
    for rowIndex, row in enumerate(self.board): #formatted rows
      print(f'{rowIndex}| {' '.join(row)} |') 
    print(f'+{'-' * (self.columns * 2 + 2)}+') #formatted bottom border 

  #ask for/handle player's input
  def get_player_input(self): 
    while True:
      colStr = input(f"{self.current_player}, where would you like to place your token? (choose a column #)")
      if colStr.isdigit():
        colNum = int(colStr)
        return colNum - 1 if colNum >= 1 and colNum <= self.cols else print(f"Please enter a number between 1-{self.cols}")
      else:
        print(f"Please enter a valid number between 1-{self.cols}")

  #add token to the board
  def drop_token(self, col):
      #find the lowest empty row in the selected column / start from the 'bottom'
      for row_index in range(len(self.board) -1, -1, -1):
        if(self.board[row_index][col] == ' '):
            self.board[row_index][col] = self.current_token
            return row_index
      return False  

  #win detection
  def detect_win(self, row, col):
    horizontal_row = ''.join(self.board[row])
    vertical_col = ''.join([self.board[rowIndex][col] for rowIndex in range(self.rows)])
    asc_diag = ''.join(self.board[rowIndex][(row + col) - rowIndex] for rowIndex in range(self.rows) if 0 <= (row + col) - rowIndex < self.cols)
    desc_diag = ''.join(self.board[rowIndex][rowIndex - (row - col)] for rowIndex in range(self.current_playerrows) if 0 <= rowIndex - (row - col) < self.cols)
    
    return any(self.win_combo in line for line in [horizontal_row, vertical_col, asc_diag, desc_diag])

  #draw detection
  def detect_draw(self):
    return all(self.board[0][col] != ' ' for col in range(self.col))

#print welcome message
print("Welcome to Connect Four! Players will take turns dropping tokens into columns. The first player to connect four tokens in a row (horizontally, vertically, or diagonally) wins!")

# ------------------------------- Player Set-Up ------------------------------ #
#set up player 1 name
print("Let's set up the first player")
while True: 
  ask_player_name_1 = input(PLAYER_PROMPT).upper()
  if ask_player_name_1 in VALID_NO + VALID_YES:
    player_1_name = input(NAME_PROMPT) if ask_player_name_1 in VALID_YES else 'Player 1'
    print(f"Great! The player going first is {player_1_name}")
    break
  else:   
    print(YES_NO_PROMPT)

#set up player 1 token
while True: 
  ask_player_token_1 = input(f"{player_1_name}, {TOKEN_PROMPT}")
  if ask_player_token_1 in VALID_NO + VALID_YES:
    player_1_token = input(f"{player_1_name}, {TOKEN_PROMPT}") if ask_player_token_1 in VALID_YES else None
    print("Okay, we'll give player 2 the opportunity to choose or one will be assigned to you") if player_1_token == None else print(f"Great! {player_1_name} has chosen {player_1_token}")
    break 
  else:
    print(YES_NO_PROMPT)


  

#set up player 2
print("Now - let's set up the second player")
while True: 
  ask_player_name_2 = input(PLAYER_PROMPT).upper()
  if ask_player_name_2 in VALID_NO + VALID_YES:
    player_2_name = input(NAME_PROMPT) if ask_player_name_2 in VALID_YES else 'Player 2'
    if player_2_name == player_1_name: 
      print("Please enter a unique name")
    else:  
      print(f"Great! The player going second is {player_2_name}")
      break
  else:   
    print(YES_NO_PROMPT)




if player_1_token == None: 
  while True: 
    customize_player_2_token = input(f"{player_2_name}, would you like to choose your token? If not, one will be assigned to you. {YES_NO_PROMPT}")
    if customize_player_2_name == 'Yes':
      player_2_token = input("What would you like your token to be? You may choose X or O").capitalize()
      player_1_token = 'X' if player_2_token == 'O' else 'O'
      print(f"Great! {player_2_name} has chosen {player_2_token}")
      break
    elif customize_player_2_name == 'No':
      print('No worries! We will choose for you')
      break
    else:
      print(YES_NO_PROMPT)
else: 
  player_2_token = 'O' if player_1_token == 'X' else 'X'

player_1 = Player(player_1_name, player_1_token)
player_2 = Player(player_2_name, player_2_token)

# ------------------------------- Board Set-Up ------------------------------- #
print("Alright! Let's set up your board")

while True: 
  customize_board = input(f"Would you like to customize your board? The default is 6 rows/7 columns. {YES_NO_PROMPT}")
  if customize_board == 'Yes':
    #row customization 
    customize_rows = input("Would you like to customize the number of rows? (Y/N)")
    while True:
      if customize_rows == 'Yes':
        row_count = input("How many rows would you like your board to have? You can have between 4-12")
        if customize_rows < 4 or customize_rows > 12 or customize_rows.digit() == False:
          print("Please enter a valid number of rows. Any number between 4 - 12")
        else:
          print(f"Wonderful! Your board will have {customize_rows} rows")
          break
      elif customize_rows == 'No':
        print("Sounds good! Your board will have 6 rows")
        break
      else: 
        print(YES_NO_PROMPT)
    # customize_columns = input("Would you like to customize the number of rows? (Y/N)")    




game = ConnectFour(player_1, player_2)

#game play
while game_status:
   #prompt player for input and get valid col #
   columnIndex = get_player_input()
   #drop the token once column is assigned a valid int and get row #
   rowIndex = drop_token(columnIndex)

   print_board()

   set_game_status(rowIndex, columnIndex)

   if not game_status: current_player = player_2 if current_player == player_1 else player_1


# def set_game_status(row, col):
  #   if detect_win(row, col):
  #       print('Way to go!')
  #       game_status = False
  #   elif detect_draw():
  #       print('So sad. No-one wins')  
  #       game_status = False

#Edge cases to look out for:
  #Response if player inputs a column that is full
  #Response if player inputs an invalid column (not an integer between 1-7)

#Current laginappe:
  #Add ability for players to choose the board size (default 7x6)
  #Add ability for player to exit and restart the game at any time
  #Add ability for players to choose their tokens (X or O)
  #Add ability for players to choose who goes first
  #Add ability for players to choose their name


  # player_1_token = input(f'{player_1Name}, choose your token (X or O): ').upper()
# player_2_token = 'O' if player_1_token == 'X' else 'X'
#establish who is going first/current player - 
# current_player = input(f'Who goes first? ({player_1Name} or {player_2Name}): ').strip()

# print('Wonderful! Let\'s start the game!')
#establish tokens