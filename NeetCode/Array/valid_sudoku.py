from typing import List, Optional, Any, Tuple
from collections import defaultdict
import json

class Solution:
  '''
    data-structure would be:
    hash: {
      row: {
          1:
          ...
          9:
        },
      col: {
          1:
          ...
          9:
        },
      box: {
          1:
          ...
          9:
        },
    }

    in total of 27 lists

    while appending the new element only if integer, then search in 
    corresponding saved list O(1) -> O(n)
  '''
  def valid_sudoku(self, board: List[List[str]]) -> bool:

    board_hash = {
       'row': { i: set() for i in range(ROW) },
       'col': { i: set() for i in range(ROW) },
       'box': { i: set() for i in range(ROW) },
    }

    for i in range(ROW):
      for j in range(COL):
        elem = board[i][j]

        if elem == '.':
          continue

        if elem in board_hash['row'][i] \
          or elem in board_hash['col'][i]:
          return False

        board_hash['row'][i].add(elem)
        board_hash['col'][i].add(elem)
    
    for box_row in range(3):
      for box_col in range(3):
        box_index = (box_row * 3) + box_col

        for i in range(3):
          for j in range(3):
            row = box_row * 3 + i
            col = box_col * 3 + j

            elem = board[row][col]

            if elem == '.':
              continue

            if elem in board_hash['box'][box_index]:
              return False

            board_hash['box'][box_index].add(elem)

    return True

  def optimal_solution(self, board: List[List[int]]) -> bool:
    
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for i in range(ROW):
      for j in range(COL):

        elem = board[i][j]

        if elem == ".":
          continue

        if elem in rows[i] \
          or elem in cols[i] \
          or elem in squares[(i // 3, j // 3)]:
          return False
        
        rows[i].add(elem)
        cols[i].add(elem)
        squares[(i // 3, j // 3)].add(elem)

    return True

if __name__ == "__main__":
  sol = Solution()

  ROW = 9
  COL = 9

  # board = [[str(elem) for elem in row.split()] for row in iter(input, "")]

  # input_string = """
  #   [["1","2",".",".","3",".",".",".","."],
  #   ["4",".",".","5",".",".",".",".","."],
  #   [".","9","8",".",".",".",".",".","3"],
  #   ["5",".",".",".","6",".",".",".","4"],
  #   [".",".",".","8",".","3",".",".","5"],
  #   ["7",".",".",".","2",".",".",".","6"],
  #   [".",".",".",".",".",".","2",".","."],
  #   [".",".",".","4","1","9",".",".","8"],
  #   [".",".",".",".","8",".",".","7","9"]]
  #   """

  input_string = """
  [["1","2",".",".","3",".",".",".","."],
  ["4",".",".","5",".",".",".",".","."],
  [".","9","1",".",".",".",".",".","3"],
  ["5",".",".",".","6",".",".",".","4"],
  [".",".",".","8",".","3",".",".","5"],
  ["7",".",".",".","2",".",".",".","6"],
  [".",".",".",".",".",".","2",".","."],
  [".",".",".","4","1","9",".",".","8"],
  [".",".",".",".","8",".",".","7","9"]]
  """
  
  board = json.loads(input_string)

  converted_board = [
     [int(elem) if elem.isdigit() else -1 for elem in row]
     for row in board
  ]

  # print(converted_board)

  print(sol.valid_sudoku(board))
  print(sol.optimal_solution(board))