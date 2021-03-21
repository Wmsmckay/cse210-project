import os
import arcade
from game import constants
from time import sleep
# from game.virus import Virus
from game.player import Player
from game.input_service import Input_service
from game.output_service import Output_service
# from game.Karen import Karen
# from game.score import Score
# from game.mask import Mask
# from game.sanitizer import Sanitizer

class Director:
    """[A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Authors:
        McKay Williams

    Attributes:
        [insert attributes]
    """

    def __init__ (self):
        """[Desctiption]

        Args:
            self (Directory): An instance of the Class directory.
        """


        # self._arcade = arcade()
        arcade.open_window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        self.actors = []
        # self.player = Player("player")
        self.input_service = Input_service()
        self.output_service = Output_service()

        # self.score = Score()

        # add enemies to the enemy list based on difficulty
        # for i in range(constants.difficulty):
        #     if (i % 3 == 0):
        #         karen = Karen()
        #         self.actors.append(karen)
        #     else:
        #         virus = Virus()
        #         self.actors.append(virus)

        # add the enemy list and player to the actor list
        # self.actors.append(self.enemies)
        # self.actors.append(self.player)

    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.player = arcade.Sprite(os.path.join(constants.PATH, "../sprites/mustache-logo.png"), constants.SCALING)
        self.player.center_x = constants.SCREEN_WIDTH / 2
        self.player.center_y = constants.SCREEN_HEIGHT / 2
        self.player.left = 10
        
        self.actors.append(self.player)


    def start_game(self):
        """ """
        self.setup()
        while True:
            self._get_inputs()
            self._do_updates()
            self._do_ouputs()
            # sleep(constants.FRAME_LENGTH)
            # create list of karens and visus for enemies




    def _get_inputs(self):
        """
        - check for if weapon is changed
        - check if direction is input
        - check if player fired
        """
        # store the input so it can be checked and passed to updates
        self.input_service.check_keys()
        # returns value of a or d (mask or sanitizer)
        # self.projectile = self.input_service.check_projectile() 



    def _do_updates(self):
        """
        """
        for actor in self.actors:
            actor.update()
        # self.actors.update()
        # update the player's location, the enemy's location, and the 
        # projectile's location. If enemy's are hit then remove them 
        # # from the list
        # if self.projectile == 'mask':
        #     self.projectile = Mask()
        # else:
        #     self.projectile = Sanitizer()
        
        # self.actors.append(self.projectile)

        # self.actors = self.handle_collisions.check_collisions(self.actors)
        
        
    # def update(self, delta_time):
    #     """
    #     Update each object in the game.
    #     :param delta_time: tells us how much time has actually elapsed
    #     """
    #     self.check_collisions()
    #     self.check_off_screen()

    #     # decide if we should start a target
    #     if random.randint(1, 50) == 1:
    #         self.create_target()

    #     for bullet in self.bullets:
    #         bullet.advance()

    #     # TODO: Iterate through your targets and tell them to advance
    #     for target in self.targets:
    #         target.advance()

        

    def _do_ouputs(self):
        """
        """
        # print out all of the actors to the screen
        arcade.start_render()
        self.output_service.draw_actors(self.actors)
        arcade.finish_render()
        arcade.run()