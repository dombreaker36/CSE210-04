class Color:
    """Takes 3 to 4 interger inputs between 0 and 255 (inclusive) and stores them for the instance of Color"""
    def __init__(self,red, green, blue, alpha = 255):
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def combine_rgb(self):
        """Takes the individual rgba numbers and makes a color out of them
        I was told this was a 'Tuple'
        """
        return (self._red, self._green, self._blue, self._alpha)