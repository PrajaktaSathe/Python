board=['0','1','2','3','4','5','6','7','8']
empty = [0,1,2,3,4,5,6,7,8]

def display_board():
  print('  |   |   ')
  print(board[0]+' | '+board[1]+' | '+board[2])
  print('  |   |   ')
  print('---------')
  print('  |   |   ')
  print(board[3]+' | '+board[4]+' | '+board[5])
  print('  |   |   ')
  print('---------') 
  print('  |   |   ')
  print(board[6]+' | '+board[7]+' | '+board[8])
  print('  |   |   ')

def player_input(player):
  player_symbol = ['X','O']
  correct_input = True

  position = int(input('player {playerNo} chance! Choose field to fill {symbol} '.format(playerNo = player +1, symbol = player_symbol[player])))

  if board[position] == 'X' or board[position] == 'O':
    correct_input = False
  
  if not correct_input:
    print("Position already equipped")
    player_input(player)
  else:
    empty.remove(position)
    board[position] = player_symbol[player] 
    return 1

def check_win():
  player_symbol = ['X','O']
  winning_positions =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

  for check in winning_positions:
    first_symbol = board[check[0]]
    if first_symbol != ' ':
      won = True
      for point in check:
        if board[point] !=  first_symbol:
          won = False
          break
      if won:
        if first_symbol == player_symbol[0]:
          print('player 1 won')
        else:
          print('player 2 won')
        break
    else:
      won = False

  if won:
    return 0
  else:
    return 1
def play():
  player = 0
  while empty and check_win():    
    display_board()
    player_input(player)
    player = int(not player)
  if not empty:
    print("NO WINNER!")

if __name__ == '__main__':
  play()
