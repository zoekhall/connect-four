# ------------------------------- Constants ------------------------------- #
VALID_YES = ['YES', 'Y', 'TRUE', '1']
VALID_NO = ['NO', 'N', 'FALSE', '0']
DEFAULT_TOKENS = ['X', 'O', '@', '#', '*']
ROWS = {
  'name': 'rows',
  'default': 6, 
  'min': 4,
  'max': 10
}
COLS = {
  'name': 'columns',
  'default': 7, 
  'min': 4,
  'max': 12
}

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
def setup_row_or_col(type):
  response = get_yes_no(f"Would you like to change the # of {type['name']}? (default = {type['default']})")
  if response in VALID_YES:
    return get_number(f"How many {type['name']} would you like? (min = {type['min']}, max = {type['max']})", type['min'], type['max'])  
  else:
    print(f"Okay! We'll set the # of {type['name']} to {type['default']}.")
    return type['default']  
  
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

def setup_player(name, default_token, other_name=None, other_token=None):
  name, token = setup_player_name(name, other_name), setup_player_token(default_token, other_token)
  return Player(name, token)

# ---------------------------------- Classes --------------------------------- #
class Player: 
  def __init__(self, name, token):
    self.name = name
    self.token = token 
class ConnectFour:
  def __init__(self, player_1, player_2, rows, cols):
    self.rows = rows
    self.cols = cols 
    self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)] 
    self.player_1 = player_1 
    self.player_2 = player_2
    self.current_player = self.player_1 
    self.game_active = True
  
  #print board
  def __repr__(self):
    header = f"   {' '.join(str(i+1) for i in range(self.cols))}"
    rows = '\n'.join(f"{i+1}| {' '.join(row)} |" for i, row in enumerate(self.board))
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
      print(f"Please enter a number between 1-{self.cols}")

  #add token to the board
  def drop_token(self, col):
      for row_index in range(len(self.board) -1, -1, -1): #find the lowest empty row in the selected column / start from the 'bottom'
        if(self.board[row_index][col] == ' '):
            self.board[row_index][col] = self.current_player.token
            return row_index
      return False  
  
  #switch players
  def switch_players(self):
    self.current_player = self.player_2 if self.current_player == self.player_1 else self.player_1

  #win detection
  def detect_win(self, row, col):
    win_combo = self.current_player.token * 4
    horizontal_row = ''.join(self.board[row])
    vertical_col = ''.join([self.board[rowIndex][col] for rowIndex in range(self.rows)])
    asc_diag = ''.join(self.board[rowIndex][(row + col) - rowIndex] for rowIndex in range(self.rows) if 0 <= (row + col) - rowIndex < self.cols)
    desc_diag = ''.join(self.board[rowIndex][rowIndex - (row - col)] for rowIndex in range(self.rows) if 0 <= rowIndex - (row - col) < self.cols)
    
    if any(win_combo in line for line in [horizontal_row, vertical_col, asc_diag, desc_diag]):
      print(f"{self.current_player.name} wins! 🎉")
      self.game_active = False

  #draw detection
  def detect_draw(self):
    if all(self.board[0][col] != ' ' for col in range(self.cols)):
      print("There are no losers here. It's a draw! 🤝")
      self.game_active = False
  
  #game play
  def play(self):
    while self.game_active:
      print(self)
      col = self.get_player_input() #pick column #
      row = self.drop_token(col) #drop token into column 
      if row == False:
        print("Whoops! That column is full. Please pick another column.")
        continue 
      
      self.detect_win(row, col)
      self.detect_draw()

      if self.game_active:
        self.switch_players()
    # print("Game over. Thanks for playing! Would you like to play again?")

# ------------------------------- Player Set-Up ------------------------------ #
print("Welcome to Connect Four! Players will take turns dropping tokens into columns. The first player to connect four tokens in a row (horizontally, vertically, or diagonally) wins!")

print("Let's set up the first player.")
player_1 = setup_player('Player 1', 'X')

print("Now - let's set up the second player.")
player_2 = setup_player('Player 2', 'O', other_name = player_1.name, other_token= player_1.token)

# ------------------------------- Board Set-Up ------------------------------- #
print("Alright! Let's set up your board.")
response = get_yes_no("Would you like to customize your board?") #ask if want to customize board
if response in VALID_YES:
  rows, cols = setup_row_or_col(ROWS), setup_row_or_col(COLS)  
else:
  rows, cols = ROWS['default'], COLS['default']

print(f"Okay, we'll now create your gameboard with {rows} rows and {cols} columns.")
game = ConnectFour(player_1, player_2, rows, cols)
print(game)

# --------------------------------- Game Play -------------------------------- #






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