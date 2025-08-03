# ------------------------------- Constants ------------------------------- #
VALID_YES = ['YES', 'Y', 'TRUE', '1']
VALID_NO = ['NO', 'N', 'FALSE', '0']
VALID_YES_NO = VALID_YES + VALID_NO
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
    if response in VALID_YES_NO:
      return response
    print("Please enter Yes or No. ")

def yes(prompt):
  return get_yes_no(prompt) in VALID_YES

def get_name(taken_name=None):
  while True:
    name = input("Which name would you like? ").strip().capitalize() 
    if name != taken_name:    
      return name
    print(f"That name has already been chosen. Please pick a unique name. ")
      
def get_token(taken_token=None):
  while True:
    token = input("What token would you like? Please pick a character (not a number) as your unique token. ").upper().strip()
    if len(token) != 1 or token.isdigit() or token == taken_token:
      print("Please pick a single character that is not a number or already used by another player") 
    else:
      return token 

def get_number(prompt, min_val, max_val):
  while True:
    val = input(prompt).strip()
    if val.isdigit() and min_val <=int(val) <= max_val: 
      return int(val)      
    print(f"Please pick a valid number between {min_val} and {max_val}. ")

# --------------------------- Game Set_up Functions --------------------------- #  
def set_name(prompt, default_name, other_name=None):
  name = get_name(other_name) if yes(prompt) else default_name
  print(f"Great! Your name is: {name}. ")
  return name

def set_token(prompt, default_token, other_token=None):
  if yes(prompt):
    token = get_token(other_token)
  else:
    token = default_token if default_token != other_token else ('O' if default_token == 'X' else 'X') 
  print(f"Great! Your token is: {token}. ")      
  return token

def create_player(player, default_token, other_name=None, other_token=None):
  print(f"Let's set up {player}.")
  name = set_name(f"Would you like to choose your name? If not, a name will be assigned to you", player, other_name)
  token = set_token(f"Would you like to choose your token? If not, a token will be assigned to you", default_token, other_token)
  return Player(name, token)

def set_who_goes_first(player_1, player_2):
  while True: 
    response = input(f"Who'd like to go first? {player_1.name} or {player_2.name}?").strip()
    if response == player_1.name:
      return player_1
    elif response == player_2.name:
      return player_2
    print("Please enter a valid player name. ")

def set_up_row_or_col(type):
  if yes(f"Would you like to change the # of {type['name']}? (default = {type['default']}) "):
    return get_number(f"How many {type['name']} would you like? (min = {type['min']}, max = {type['max']}) ", type['min'], type['max'])  
  else:
    print(f"Okay! We'll set the # of {type['name']} to {type['default']}. ")
    return type['default']  
  
def set_up_board():
  if yes("Would you like to customize the board? "):
    rows, cols = set_up_row_or_col(ROWS), set_up_row_or_col(COLS)
  else: 
    rows, cols = ROWS['default'], COLS['default']
  print(f"Okay, we'll now create your gameboard with {rows} rows and {cols} columns.")
  return (rows, cols)

def customize_players(player_1, player_2):
  player_1.name = set_name(f"Would you like to change the name of {player_1.name}? ", player_1.name, player_2.name)
  player_1.token = set_token(f"Would you like to change {player_1.name}'s token? ", player_1.token, player_2.token)
  player_2.name = set_name(f"Would you like to change the name of {player_2.name}? ", player_2.name, player_1.name)
  player_2.token = set_token(f"Would you like to change {player_2.name}'s token? ", player_2.token, player_1.token)

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
      colStr = input(f"{self.current_player.name}, where would you like to place your token? (choose a column #) ")
      if colStr.isdigit():
        if 1 <= int(colStr) <= self.cols:
          return int(colStr) - 1
      print(f"Please enter a number between 1-{self.cols}. ")

  #add token to the board
  def drop_token(self, col):
      for row_index in range(len(self.board) -1, -1, -1): #find the lowest empty row in the selected column / start from the 'bottom'
        if(self.board[row_index][col] == ' '):
            self.board[row_index][col] = self.current_player.token
            return row_index
      return False  
  
  #switch players
  def switch_players(self):
    self.current_player = self.player_2 if self.current_player is self.player_1 else self.player_1

  #win detection
  def detect_win(self, col, row):
    horizontal_row = ''.join(self.board[row])
    vertical_col = ''.join([self.board[rowIndex][col] for rowIndex in range(self.rows)])
    asc_diag = ''.join(self.board[rowIndex][(row + col) - rowIndex] for rowIndex in range(self.rows) if 0 <= (row + col) - rowIndex < self.cols)
    desc_diag = ''.join(self.board[rowIndex][rowIndex - (row - col)] for rowIndex in range(self.rows) if 0 <= rowIndex - (row - col) < self.cols)
    
    if any((self.current_player.token * 4) in line for line in [horizontal_row, vertical_col, asc_diag, desc_diag]):
      print(f"{self}\n{'*' * (self.cols * 2 + 2)}\n{self.current_player.name} wins! 🎉")
      self.game_active = False

  #draw detection
  def detect_draw(self):
    if all(self.board[0][col] != ' ' for col in range(self.cols)):
      print(f"{self}\n{'*' * (self.cols * 2 + 2)}\nThere are no losers here. It's a draw! 🤝")
      self.game_active = False

  #game play
  def play(self):
    while self.game_active:
      print(self)
      col, row = self.get_player_input(), self.drop_token(col)
      if row is False:
        print("Whoops! That column is full. Please pick another column. ")
        continue 
      
      self.detect_win(col, row)
      self.detect_draw()

      if self.game_active:
        self.switch_players()

# ------------------------------- Initial Set-Up ------------------------------ #
print("Welcome to Connect Four! Players will take turns dropping tokens into columns. The first player to connect four tokens in a row (horizontally, vertically, or diagonally) wins!")

player_1 = create_player('Player 1', 'X')
player_2 = create_player('Player 2', 'O', other_name = player_1.name, other_token= player_1.token)

print("Alright! Let's set up the board.")
rows, cols = set_up_board()

# --------------------------------- Game Play -------------------------------- #
def game_play():
  global rows, cols
  while True:
    game = ConnectFour(player_1, player_2, rows, cols)
    game.current_player = set_who_goes_first(player_1, player_2)
    game.play() 
    if yes("Do you want to play again? "):
      if yes("Do you want to change player information/board size? "):
        if yes("Would you like to change player information? "):
          customize_players(player_1, player_2)
        if yes("Would you like to customize the board? "):
          rows, cols = set_up_board()
    else:
      print("Thanks for playing!")

if __name__ == "__main__":
  game_play()      