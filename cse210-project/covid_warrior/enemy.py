from game import constants
from game.actor import Actor
from game.point import Point

# We should make Karens and Viruses the same class. The only difference between the two are that they should be in
# two different lists and should be drawn differently

class Enemy(Actor):
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
        """The class constructor. invokes a superclass constructor in order to change the variables in the Actor class
        according to the enemies needs.
        ARGS: 
            self: An instance of Actor"""
        super().__init__()
        self.set_position = Point(enemy.left, enemy.top)
        self.set_velocity = enemy.velocity #????? not sure if this is right
        
    def add_enemy(self, delta_time: float):
        """Adds a new karen to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # Create the KAREN
        enemy = arcade.Sprite("images/missile.png", SCALING)

        # Set its position to a random height and off screen right
        enemy.left = random.randint(self.width, self.width + 80) # Get the right variable name for the constants
        enemy.top = random.randint(10, self.height - 10)
        
    def move_enemy(self):
        # Set its speed to a random speed heading left
        enemy.velocity = (random.randint(-20, -5), 0)

        # Add it to the enemies list
        self.enemy_list.append(enemy)
        self.all_sprites.append(enemy)
