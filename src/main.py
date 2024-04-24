from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    l = Line(Point(50, 50), Point(400, 50))
    win.draw_line(l, "black")
    win.wait_for_close()


main()