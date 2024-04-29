from cell import Cell
import time
import random

class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    if seed is not None:
      self._seed = random.seed(seed)
    else: 
      self._seed = seed
    self._cells = []
    self._create_cells()
    self._generate_maze()

  def _create_cells(self):
    for i in range(self._num_cols):
      column = []
      for j in range(self._num_rows):
        cell = Cell(self._win)
        column.append(cell)
      self._cells.append(column)
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_cells_visited()

  def _generate_maze(self):   
    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self._draw_cell(i, j)

  def _draw_cell(self, i, j):
    if self._win is None:
      return
    x1 = self._x1 + i * self._cell_size_x
    y1 = self._y1 + j * self._cell_size_y
    x2 = x1 + self._cell_size_x
    y2 = y1 + self._cell_size_y
    self._cells[i][j].draw(x1, y1, x2, y2)
    self._animate()

  def _animate(self):
    if self._win is None:
      return
    self._win.redraw()
    time.sleep(0.05)

  def _break_entrance_and_exit(self):
    cell = self._cells[0][0]
    cell.has_top_wall = False

    cell = self._cells[-1][-1]
    cell.has_bottom_wall = False

  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True
    while True:
      next_index_list = []

      # determine which cell(s) to visit next
      # left
      if i > 0 and not self._cells[i - 1][j].visited:
        next_index_list.append((i - 1, j))
      # right
      if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
        next_index_list.append((i + 1, j))
      # up
      if j > 0 and not self._cells[i][j - 1].visited:
        next_index_list.append((i, j - 1))
      # down
      if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
        next_index_list.append((i, j + 1))

      # if there is nowhere to go from here
      # just break out
      if len(next_index_list) == 0:
        self._draw_cell(i, j)
        return

      # randomly choose the next direction to go
      direction_index = random.randrange(len(next_index_list))
      next_index = next_index_list[direction_index]

      # knock out walls between this cell and the next cell(s)
      # right
      if next_index[0] == i + 1:
        self._cells[i][j].has_right_wall = False
        self._cells[i + 1][j].has_left_wall = False
      # left
      if next_index[0] == i - 1:
        self._cells[i][j].has_left_wall = False
        self._cells[i - 1][j].has_right_wall = False
      # down
      if next_index[1] == j + 1:
        self._cells[i][j].has_bottom_wall = False
        self._cells[i][j + 1].has_top_wall = False
      # up
      if next_index[1] == j - 1:
        self._cells[i][j].has_top_wall = False
        self._cells[i][j - 1].has_bottom_wall = False

      # recursively visit the next cell
      self._break_walls_r(next_index[0], next_index[1])

  def _reset_cells_visited(self):
    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self._cells[i][j].visited = False