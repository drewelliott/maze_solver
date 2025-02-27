from typing import Optional
from graphics import Window, Point, Line


class Cell:
    def __init__(self, win: Window):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
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

    def draw_move(self, to_cell, undo: Optional[bool] = False):
        # We must force integer on the grid, so we can not
        # use standard (x1 + y1) / 2 as we may end up with
        # a float
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
