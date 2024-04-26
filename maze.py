from cell import Cell
import time

class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    self._cells = []
    self._create_cells()

  def _create_cells(self):
    for col in range(self._num_cols):
      column = []
      for row in range(self._num_rows):
        cell = Cell(self._win)
        x1 = self._x1 + col * self._cell_size_x
        y1 = self._y1 + row * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)
        column.append(cell)
      self._cells.append(column)
    

  def _draw_cell(self, col, row):
    if self._win is None:
      return
    cell = self._cells[col][row]
    cell.draw(cell._x1, cell._y1, cell._x2, cell._y2)
    self._animate()

  def _animate(self):
    if self._win is None:
      return
    self._win.redraw()
    time.sleep(0.05)