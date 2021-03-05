from game import constants
from game.point import Point

class Actor:
    """Actor will keep track of position, velocity, and the appearance of the movable objects in the game

    Stereotype:
        information holder
        https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/august/patterns-in-practice-object-role-stereotypes
        


    Authors:
        Christine Helfrich

    Attributes:

        _sprite (string): The visual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor."""
  
        self._sprite = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

   

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_sprite(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._sprite

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_sprite(self, sprite):
        """Updates the actor's text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._sprite = sprite

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity
