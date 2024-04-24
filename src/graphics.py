from tkinter import Tk, BOTH, Canvas

class Window:
  def __init__(self, width, height, title="Maze Solver") -> None:
    # Initialize the root widget
    self.root = Tk()
    self.root.title(title) # Set the window title

    # Create a Canvas widget
    self.canvas = Canvas(self.root, width=width, height=height)
    self.canvas.pack()  # Pack the canvas to make it visible

    # Data member to represent the window's running state
    self.is_running = False

    # stop window from running if closed
    self.root.protocol("WM_DELETE_WINDOW", self.close)

  def redraw(self):
    self.root.update_idletasks()
    self.root.update()

  def wait_for_close(self):
    self.is_running = True
    while self.is_running == True:
      self.redraw()
    print("window closed...")
  
  def draw_line(self, line, fill_color="black"):
    line.draw(self.canvas, fill_color)

  def close(self):
    self.is_running = False


class Point:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y


class Line:
  def __init__(self, point1, point2) -> None:
    self.point1 = point1
    self.point2 = point2

  def draw(self, canvas, fill_color="black"):
    canvas.create_line(
    self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
)
