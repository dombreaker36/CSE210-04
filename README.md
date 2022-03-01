# CSE210-04

# Greed Game

# Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
# The player (#) can move left or right along the bottom of the screen.
# If the player touches a gem they earn a point.
# If the player touches a rock they lose a point.
# Gems and rocks are removed when the player touches them.
# The game continues until the player closes the window.


Gunnar - Make them fall (Probably fix the spawning and when they fall off the screen)

Alvaro - Add or subtract points (display the points)

Martin - Make them disappear when touched


New plan:

__main__.py will be used to set up all of the window and parameters, director.py will then take those parameters and tell all of the actors what to do.

Actors will have gems, rocks, and a player. gems rocks and player will have point and color.

I think according to our original diagram, director will tell Color and Point what to do too (as a parent class), but those will ultimately come from main where all of the parameters are editable. 

Will I need to import all of the classes into main?
