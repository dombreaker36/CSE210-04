class Point:
    """Very useful in all things placement related to elements on the screen.
    This could be used in a non grid format, but I will make those options in the main file
    """

    def __init__(self, x, y):
        """Makes a new Point"""
        self._x = x
        self._y = y
    
    ###These below here are handy and given in the original code. I wonder what other handy things we could add?

    # Combine
    def add(self, other_point):
        """adds two points together, likely to be used by velocity"""
        x = self._x + other_point.get_x()
        y = self._y + other_point.get_y()
        return Point(x, y)

    # X-Value
    def get_x(self):
        return self._x

    # Y-Value
    def get_y(self):
        return self._y

    # Equal?
    def equals(self, other_point):
        if self._x == other_point.get_x():
            if self._y == other_point.get_y():
                are_equal = True
            else:
                are_equal = False
        else:
            are_equal = False
        return are_equal
            
    def scale(self, factor):
        """This would be useful in velocity, but how do we use this to create bigger letters that can actually be recognized and collided with as bigger letters?
        Last time I tried to create bigger letters in the main program, the font size and cell size did increase, but the collide window, or recognized interaction space did not, many times the character could not collect what was needed becuase it was on a between grid space... could this help that?"""
        """This is what they used"""
        return Point(self._x * factor, self._y * factor)
