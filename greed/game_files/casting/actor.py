from game_files.shared.color import Color
from game_files.shared.point import Point

class Actor:     ###Consider taking these defaults here and placing them in the main, then to director, then to here, it would be a lot of passing down, but then we could do all of the changing of the color and starting location etc in the main which would be nice (to not have to look through all the files to find these default settings)
    def __init__(self):
        self._symbol = ""
        self._font_size = 15 #default
        self._color = Color(255, 255, 255) #default (is white)
        self._position = Point(0, 0) # default starting position
        self._velocity = Point(0, 0) # default speed

    def get_text():
        pass