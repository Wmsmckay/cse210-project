from game.point import Point
# from game.actor import Actor
import arcade

class Player(arcade.Sprite):
    """[inert description]

    Stereotype:
        [insert stereotype]
        https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/august/patterns-in-practice-object-role-stereotypes
        

    Authors:
        John Stavast

    Attributes:
        [insert attributes]
    """

    # def __init__(self, sprite):
    #     # self.set_sprite(sprite)
    #     # self._position = Point(0, 0)


    def on_update(self):
        self.update()