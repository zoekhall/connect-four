#print welcome message
#print board

#For each turn:
  #print instruction specific to player  
  #get input from player
  #check if input is valid (1-7)
  #find the lowest empty row in the selected column
  #place the player's specific token in that row

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