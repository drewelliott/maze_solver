from tkinter import Tk, BOTH, Canvas
from typing import Type, Optional


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white",
                               height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Window, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y,
            self.p2.x, self.p2.y,
            fill=fill_color, width=2
        )


class Cell:
    def __init__(self,
                 p1: Point, p2: Point,
                 win: Window,
                 has_left_wall: Optional[bool] = True,
                 has_right_wall: Optional[bool] = True,
                 has_top_wall: Optional[bool] = True,
                 has_bottom_wall: Optional[bool] = True,
                 ):
        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self):
        upper_left = Point(self._x1, self._y1)
        upper_right = Point(self._x2, self._y1)
        lower_left = Point(self._x1, self._y2)
        lower_right = Point(self._x2, self._y2)
        if self.has_top_wall:
            self._win.draw_line(Line(upper_left, upper_right))
        if self.has_left_wall:
            self._win.draw_line(Line(upper_left, lower_left))
        if self.has_right_wall:
            self._win.draw_line(Line(upper_right, lower_right))
        if self.has_bottom_wall:
            self._win.draw_line(Line(lower_left, lower_right))
