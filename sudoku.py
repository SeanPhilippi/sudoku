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

def solve(board):


# the board (array of arrays), num being inserted, and coordinates for insertion
def valid(board, num, coords):
  # check row
  # for each position in range of 9
  for i in range(len(board[0])):
    # looping 0-8, checking the number at each coordinate for coords[0] row, if it is equal to
    # the insertion # and the coords[1] col number is not equal to the column number, return False
    # so ignore the number if it's the number that was just inserted
    if board[coords[0]][i] == num and coords[1] != i:
      return False

  # check column
  for i in range(len(board)):
    if board[i][coords[1]] == num and coords[0] != i:
      return False

  # check box (9 boxes)
  box_x = coords[1] // 3 # divide by 3 to determine column index of box, or x position (0-2)
  box_y = coords[0] // 3 # divide by 3 to determine row index of box, or y position (0-2)

  # loop through the found box and make sure the same number doesn't appear twice
  for i in range(box_y * 3, box_y * 3 + 3):
    for j in range(box_x * 3, box_x * 3 + 3):
      if board[i][j] == num and (i, j) != coords:
        return False
  return True

valid(board, 1, (1, 2))

def print_board(board):
  # range returns a sequence of #s from 0 to n
  for i in range(len(board)): # for item in [0-8]
    # print('i', i)
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

# print_board(board)

# returns coordinates of empties
def find_empty(board):
  for i in range(len(board)): # for each row
    for j in range(len(board[0])): # for each column
      if board[i][j] == 0:
        return (i, j) # return tuple of row (y), column (x)

print(find_empty(board))