import copy
import sys

width = 40
height = 27

Alive = '🐋'
Dead = ' '

board = [[Dead for _ in range(width)] for _ in range(height)]
next_board = copy.deepcopy(board)

board[3][3:5] = [Alive, Alive]
board[4][2:4] = [Alive, Alive]
board[5][3] = Alive

def print_board(board):
  for row in board:
    print(' '.join(row))

def get_neighbors(board, row, col):
  next_col = col + 1 if col + 1 < width else 0
  next_row = row + 1 if row + 1 < height else 0
  return (board[row - 1][col - 1], board[row - 1][col], board[row - 1][next_col],
          board[row][col - 1],                          board[row][next_col],
          board[next_row][col - 1], board[next_row][col], board[next_row][next_col])

def step(old, new):
  for row in range(height):
    for col in range(width):
      cell = old[row][col]
      neighbors = get_neighbors(old, row, col)
      alive = [x for x in neighbors if x == Alive]
      if cell == Alive:
        if len(alive) < 2 or len(alive) > 3:
          new[row][col] = Dead
        else:
          new[row][col] = Alive
      else:
        if len(alive) == 3:
          new[row][col] = Alive
        else:
          new[row][col] = Dead

while True:
  print("Conways game of life")
  print_board(board)

  step(board, next_board)
  board, next_board = next_board, board

  sys.stdin.read(1)
