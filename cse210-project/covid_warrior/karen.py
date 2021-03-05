from game import constants
from game.actor import Actor
from game.point import Point

# We should make Karens and Viruses the same class. The only difference between the two are that they should be in
# two different lists and should be drawn differently

class Karen(Actor):
    """This class will initialize, draw, and set a position nad velocity to a list of karens

    Stereotype:
        Structurer, Information Holder
        https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/august/patterns-in-practice-object-role-stereotypes
        

    Authors:
        Christine Helfrich

    Attributes:
        [insert attributes]
    """
    
    def __init__(self):
        """The class constructor
        ARGS: 
            self: An instance of Karen"""
        self.velocity = velocity
        
    def add_karen(self, delta_time: float):
        """Adds a new karen to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # Create the KAREN
        karen = arcade.Sprite("images/missile.png", SCALING)

        # Set its position to a random height and off screen right
        karen.left = random.randint(self.width, self.width + 80) # Get the right variable name for the constants
        karen.top = random.randint(10, self.height - 10)
        
    def move_karen(self):
        # Set its speed to a random speed heading left
        karen.velocity = (random.randint(-20, -5), 0)

        # Add it to the enemies list
        self.karen_list.append(karen)
        self.all_sprites.append(karen)
