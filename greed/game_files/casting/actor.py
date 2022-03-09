from game_files.shared.color import Color
from game_files.shared.point import Point

class Actor:     
    """builds an actor using basic parameters, which can be edited and called upon later, that will represent one object on the screen. Everything on the screen is an actor which is a parent class to Gem, Player, and Rock. """
    ###Consider taking these defaults here and placing them in the main, then to director, then to here, it would be a lot of passing down, but then we could do all of the changing of the color and starting location etc in the main which would be nice (to not have to look through all the files to find these default settings)
    def __init__(self, symbol = "", font_size = 15, color = Color(255, 255, 255), position = Point(0, 0), velocity = Point(0, 0)):
        self._symbol = symbol
        self._font_size = font_size #default
        self._color = color #default (is white)
        self._position = position # default starting position
        self._velocity = velocity # default speed



    # Symbol
    def set_symbol(self, symbol):
        """uses the given symbol as the symbol for this actor."""
        self._symbol = symbol

    def get_symbol(self):
        """returns the symbol saved for this actor"""
        return self._symbol
    


    # Font Size
    def set_font_size(self, new_size):
        """uses given interger for new font size"""
        self._font_size = new_size
    
    def get_font_size(self):
        """returns current font size (int)"""
        return self._font_size



    # Color
    def set_color(self, new_color):
        """takes the given value for color and replaces the old color"""
        self._color = new_color

    def get_color(self):
        """returns current color"""
        return self._color
    


    # Position
    def set_position(self, new_point):
        """takes the given point and uses it as the new location of the object"""
        self._position = new_point

    def get_position(self):
        """returns the current point (position) of the actor"""
        return self._position



    # Velocity
    def set_velocity(self, point_to_agregate):
        """updates current velocity to match point agregate given. The point agregate is added to the x and y values respectively of the current position to get a velocity."""
        self._velocity = point_to_agregate
    
    def get_velocity(self):
        """returns the point amount that is added to make this version of velocity happen, eg Point(0, 1) would mean move zero on the x axis and positive one on the y axis."""
        return self._velocity
    