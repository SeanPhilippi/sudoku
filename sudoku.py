board = [
  [7,8,0,4,3,5,6,3,5],
  [5,4,3,5,7,8,4,5,6],
  [5,4,6,1,7,7,6,9,0],
  [7,8,0,4,3,5,6,3,5],
  [5,4,3,5,7,8,4,5,6],
  [5,4,6,1,7,7,6,9,0],
  [7,8,0,4,3,5,6,3,5],
  [5,4,3,5,7,8,4,5,6],
  [5,4,6,1,7,7,6,9,0]
]

def print_board(board):
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print('\n- - - - - - - - - - - - - ')
    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print(' | ', end='')

      if j == 0:
        print(board[i][j])
      else:
        print(str(board[i][j]) + ' ', end='')

print_board(board)