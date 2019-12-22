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
  # range returns a sequence of #s from 0 to n
  for i in range(len(board)): # for item in [0-8]
    #print('i', i)
    # determine if a line should be printed based on row #
    if i % 3 == 0 and i != 0:
      print('- - - - - - - - - - - -')
    # logic for what characters to print on each row
    for j in range(len(board)):
      if j % 3 == 0 and j != 0:
        print(' | ', end='') # setting print end argument to empty string instead of deafult \n

      if j == 8:
        # print last character with the default end argument \n
        print(board[i][j])
      else:
        # print the character at board[i][j] with end argument of '' so more characters concatenate
        print(str(board[i][j]) + ' ', end='')

print_board(board)