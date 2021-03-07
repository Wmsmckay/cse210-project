import arcade
from game.player import Player
import game.constants



class Input_service:
    """[inert description]

    Stereotype:
        [insert stereotype]
        https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/august/patterns-in-practice-object-role-stereotypes
        

    Authors:
        John Stavast

    Attributes:
        [insert attributes]
    """
    
    def __init__(self):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        self.holding_left = False
        self.holding_right = False
        self.holding_a = False
        self.holding_d = False
        self.actor = Player()
    
    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.move_left()

        elif self.holding_right:
            self.move_right()
            
        # if self.holding_a:
        #    fire.fire_sanitizer()
            
        # if self.holding_d:
        #     fire.fire_mask()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT:
            self.holding_left = True
            self.actor.set_position

        if key == arcade.key.RIGHT:
            self.holding_right = True
            
        if key == arcade.key.A:
            self.holding_a = True
            
        if key == arcade.key.D:
            self.holding_d = True   

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT:
            self.holding_left = False

        if key == arcade.key.RIGHT:
            self.holding_right = False
            
        if key == arcade.key.A:
            self.holding_a = False
            
        if key == arcade.key.D:
            self.holding_d = False  
            
    def move_right(self):
        """
        Moves the player left when called and in required parameter
        """
        # allows character to move until they
        # reach the left of the screen
        if actor._position.get_x < SCREEN_WIDTH - X_VELOCITY:
            actor._position.set_x += X_VELOCITY
            # self.draw()
            
    def move_left(self):
        """
        Moves the player right when called and in required parameter
        """
        # allows player to move until they
        # reach the right of the screen
        if actor._position.get_x > X_VELOCITY:
            actor._position.set_x -= X_VELOCITY

    # def draw(self):
    #     arcade.draw_rectangle_filled(self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.BLUE)