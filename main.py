# ------------------------------- Constants ------------------------------- #
VALID_YES = ['YES', 'Y', 'TRUE', '1']
VALID_NO = ['NO', 'N', 'FALSE', '0']
DEFAULT_TOKENS = ['X', 'O', '@', '#', '*']
DEFAULT_ROWS = 6
DEFAULT_COLS = 7

# ----------------------------- Utility Functions ---------------------------- #
def get_yes_no(prompt):
  while True: 
    response = input(prompt).strip().upper()
    if response in (*VALID_YES, *VALID_NO):
      return response
    print("Please enter Yes or No.")

def get_name(taken_name=None):
  while True:
    name = input("What would you like your name to be?").strip() 
    if name != taken_name:    
      return name
    print(f"That name has already been chosen. Please pick a unique name.")
      
def get_token(taken_token=None):
  while True:
    token = input("What would you like your token to be? Please pick one character that is not a number.").strip()
    if len(token) != 1:
      print("Please enter a single character.")
    elif token.isdigit(): 
      print("Please don't use a number.")
    elif token == taken_token:
      print("That token is already taken. Try another one.")     
    else:
      return token 

def get_number(prompt, min_val, max_val):
  while True:
    val = input(prompt).strip()
    if val.isdigit() and min_val <=int(val) <= max_val: 
      return int(val)      
    print(f"Please pick a valid number between {min_val} and {max_val}.")

# --------------------------- Game Setup Functions --------------------------- #
def setup_player_name(player_num, other_name=None):
  if get_yes_no("Would you like to choose your name?") in VALID_YES:
    player_name = get_name(other_name) 
  else: 
    player_name = player_num #if yes, get_name(and compare other_name) - else assigned the player #
  print(f"Great! You've chosen the name: {player_name}.")
  return player_name

def setup_player_token(default_token, other_token=None):
  response = get_yes_no("Would you like to choose your token?") #ask if want to choose token
  if response in VALID_YES:
    token = get_token(other_token)
  else:
    if default_token == other_token: 
      token = 'O' if default_token == 'X' else 'X'
    else:
      token = default_token   
  print(f"Great! You've chosen the token: {token}.")
  return token

# ---------------------------------- Classes --------------------------------- #
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
    self.game_active = True
  
  def __repr__(self):
    header = f"   {' '.join(str(i + 1) for i in range(self.cols))}"
    rows = '\n'.join(f"{i}| {' '.join(row)} |" for i, row in enumerate(self.board))
    bottom_border = f"+{'-' * (self.cols * 2 + 2)}+"
    return f"{header}\n{rows}\n{bottom_border}"

  #ask for/handle player's input
  def get_player_input(self): 
    while True:
      colStr = input(f"{self.current_player.name}, where would you like to place your token? (choose a column #)")
      if colStr.isdigit():
        colNum = int(colStr)
        if 1 <= colNum <= self.cols:
          return colNum - 1
      print(f"{prompts.NUMBER_ERROR} 1-{self.cols}")

  #add token to the board
  def drop_token(self, col):
      #find the lowest empty row in the selected column / start from the 'bottom'
      for row_index in range(len(self.board) -1, -1, -1):
        if(self.board[row_index][col] == ' '):
            self.board[row_index][col] = self.current_player.token
            return row_index
      return False  

  #win detection
  def detect_win(self, row, col):
    win_combo = self.current_player.token * 4
    horizontal_row = ''.join(self.board[row])
    vertical_col = ''.join([self.board[rowIndex][col] for rowIndex in range(self.rows)])
    asc_diag = ''.join(self.board[rowIndex][(row + col) - rowIndex] for rowIndex in range(self.rows) if 0 <= (row + col) - rowIndex < self.cols)
    desc_diag = ''.join(self.board[rowIndex][rowIndex - (row - col)] for rowIndex in range(self.rows) if 0 <= rowIndex - (row - col) < self.cols)
    
    return any(win_combo in line for line in [horizontal_row, vertical_col, asc_diag, desc_diag])

  #draw detection
  def detect_draw(self):
    return all(self.board[0][col] != ' ' for col in range(self.cols))

# ------------------------------- Player Set-Up ------------------------------ #
print("Welcome to Connect Four! Players will take turns dropping tokens into columns. The first player to connect four tokens in a row (horizontally, vertically, or diagonally) wins!")

print("Let's set up the first player")
player_1_name = setup_player_name("Player 1")

print("Now - let's set up the second player")
player_2_name = setup_player_name("Player 2", player_1_name)

print(f"Let's choose {player_1_name}'s token")
player_1_token = setup_player_token('X')

print(f"Let's choose {player_2_name}'s token")
player_2_token = setup_player_token('O', player_1_token)

player_1 = Player(name=player_1_name, token=player_1_token)
player_2 = Player(name=player_2_name, token=player_2_token)

# ------------------------------- Board Set-Up ------------------------------- #
# print("Alright! Let's set up your board")
# while True: 
#   customize_board = input(f"Would you like to customize your board? The default is 6 rows/7 columns. {YES_NO_PROMPT}")
#   if customize_board in VALID_YES:
#     #row customization 
#     while True:
#       customize_rows = input(f"Would you like to customize the number of rows? {YES_NO_PROMPT}")
#       if customize_rows in VALID_YES:
#         while True:
#           row_count = input("How many rows would you like your board to have? You can have between 4-12")
#           if row_count.isdigit() and 4 <= int(row_count) <=12: 
#               print(f"Wonderful! Your board will have {int(row_count)} rows")
#               break
#           print(f"{NUMBER_ERROR} 4-12")  
#         break 
#       elif customize_rows in VALID_NO:
#         print("Sounds good! Your board will have 6 rows")
#         break
#   elif customize_board in VALID_NO:
#     print("Using default board size: 6 rows x 7 columns")
#     break 
#   print(YES_NO_PROMPT)   



# game = ConnectFour(player_1, player_2)

# #game play
# while game_status:
#    #prompt player for input and get valid col #
#    columnIndex = get_player_input()
#    #drop the token once column is assigned a valid int and get row #
#    rowIndex = drop_token(columnIndex)

#    print_board()

#    set_game_status(rowIndex, columnIndex)

#    if not game_status: current_player = player_2 if current_player == player_1 else player_1


# # def set_game_status(row, col):
#   #   if detect_win(row, col):
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