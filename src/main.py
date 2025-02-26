from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    cell = Cell(Point(0, 0), Point(50, 50), win)
    cell.draw()
    cell = Cell(Point(0, 50), Point(50, 100), win)
    cell.draw()
    cell = Cell(Point(200, 200), Point(400, 400), win, has_right_wall=False)
    cell.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
