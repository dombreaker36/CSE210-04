import pyray


class VideoServices:
    """Outputs the game state to the screen.
    
    """
    def __init__(self):
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        # self.debug = debug     # not using for now
    
    def close_window(self):     #also releases computing resources
        pyray.close_window()
    
    def clear_buffer(self):     #call at beginning of game's output phase
        """clears buffer to be ready for next rendering"""
        pyray.begin_drawing()
        pyray.clear_background(pyray.WHITE)
        # if self._debug == True:     #Not used unless debug is on
        #     self._draw_grid()
    
    def draw_actor(self, actor):
        """draws actor to screen"""
        symbol = actor.get_text()
        


