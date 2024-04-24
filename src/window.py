from tkinter import Tk, BOTH, Canvas

class Window:
  def __init__(self, width, height, title="My Window") -> None:
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
  
  def close(self):
    self.is_running = False