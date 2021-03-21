from game.constants import MAX_X
from game.constants import MAX_Y
import random
from game.constants import constants

# NEED TO IMPORT CLASS WHERE KAREN, VIRUS, HAND SANITIZER, AND MASK LIST WAS CREATED
# NEED TO USE CORRECT VARIABLES FOR LISTS OF KAREN, VIRUS, HAND SANITIZER, AND MASK

class Handle_collisions:
    """The class will update the game to accomidate for the actions of when actors collide

    Stereotype:
        Controller
        https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/august/patterns-in-practice-object-role-stereotypes
        

    Authors:
        Christine Helfrich

    Attributes:
        delta_time {float} -- Time since the last update
    """
    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects

        Arguments:
            delta_time {float} -- Time since the last update
        """
         
        # Checks if a mask has hit a Karen, and removes the Karen if she has been hit
        if self.mask.collides_with_list(self.enemies_list):
            self.remove_from_karen_lists()
            
        # Checks if a hand sanitizer has hit a virus, and removes the virus if it has been hit
        if self.hand_sanitizer.collides_with_list(self.virus_list):
            self.remove_from_virus_lists()
            
        # If there are no more enemies onscreen, you win! 
        if len(self.player.collides_with_list(self.enemies_list)) > 0:
            arcade.play_sound(self.collision_sound)
            arcade.close_window()

        # Update everything
        self.all_sprites.update()

    def check_collisions(self, actors):
        
        for item in actors.items():
            if item.get_text() == player

    actors:[
    ['mask', point, radius, color(sprite)]
    ['karen', point, radius, color(sprite)]
    ['virus', point, radius, color(sprite)]
    ['player', point, radius, color(sprite)]
        ]