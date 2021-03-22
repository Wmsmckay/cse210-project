import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "COVID Warrior"

ENEMY_SCALING_PLAYER = 0.5
ENEMY_SCALING_COIN = 0.2
ENEMY_COUNT = 12

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ENEMY = 0.1
SPRITE_SCALING_PROJECTILE = 0.7
BULLET_SPEED = 6

PLAYER_VELOCITY = 7




"""
NOTES:
'A' fires one projectile
'D' fire the other projectile
Left and Right arrows control player motions
Collisions are handled to get rid of projectile and enemy 
when the correct hit occurs otherwise the projectile is 
removed.
"""





class Enemy(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the enemy to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the enemy
        self.center_y -= 1

        # See if the enemy has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # self.reset_pos()
            self.remove_from_sprite_lists()
            self



            
            



class Player():
    def __init__(self):
        self.player_sprite_list = None
        # Set up the player info
        self.player_sprite = None
        self.player_sprite_list = arcade.SpriteList()
        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        # self.player_sprite = arcade.Sprite("./sprites/mustache-logo.png")
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)


    
    def move_left(self):
        if self.player_sprite.center_x > 0:
            self.player_sprite.center_x -= PLAYER_VELOCITY
        
        
    def move_right(self):
        if self.player_sprite.center_x < SCREEN_WIDTH:
            self.player_sprite.center_x += PLAYER_VELOCITY
        
    def draw(self):
        self.player_sprite_list.draw()
    






class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

        # Variables that will hold sprite lists
        self.player = Player()
        self.karen_sprite_list = None
        self.mask_sprite_list = None
        self.sanitizer_sprite_list = None
        self.virus_sprite_list = None
        self.holding_left = False
        self.holding_right = False

        # Load sounds
        self.shoot_mask = arcade.load_sound(":resources:sounds/laser4.wav")
        self.shoot_sanitizer = arcade.load_sound(":resources:sounds/laser5.wav")
        self.good_hit_mask = arcade.load_sound(":resources:sounds/rockHit2.wav")
        self.good_hit_sanitizer = arcade.load_sound(":resources:sounds/laser4.wav")
        self.bad_hit = arcade.load_sound(":resources:sounds/hit1.wav")

        # player's score
        self.score = 0

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        # Sprite lists
        
        self.karen_sprite_list = arcade.SpriteList()
        self.mask_sprite_list = arcade.SpriteList()
        self.sanitizer_sprite_list = arcade.SpriteList()
        self.virus_sprite_list = arcade.SpriteList()

        # player's score
        self.score = 0

        self.spawn_all_enemies()
        # All sprite list
        self.all_sprites = arcade.SpriteList()


    def spawn_all_enemies(self):
        # set up enemies
        for i in range(1, ENEMY_COUNT):
            randoNum = random.randint(1, 100)

            if randoNum % 3 == 0:
                # # Set up virus
            # for i in range(1, ENEMY_COUNT):
                virus = Enemy("./sprites/virus.png", SPRITE_SCALING_ENEMY)
                # Set its position to a random height and off screen right
                virus.left = random.randint(20, SCREEN_WIDTH - 20)
                # virus.top = random.randint((SCREEN_HEIGHT / 2) + 10, SCREEN_HEIGHT - 10)
                virus.top = SCREEN_HEIGHT
                self.virus_sprite_list.append(virus)
                
            else: 
                # # Set up karen
                # for i in range(1, ENEMY_COUNT):
                #     # enemy = Enemy(":resources:images/items/coinGold.png", SPRITE_SCALING_ENEMY)
                karen = Enemy("./sprites/karen.png", SPRITE_SCALING_ENEMY)

                # Set its position to a random height and off screen right
                karen.left = random.randint(20, SCREEN_WIDTH - 20)
                # karen.top = random.randint((SCREEN_HEIGHT / 2) + 10, SCREEN_HEIGHT - 10)
                karen.top = SCREEN_HEIGHT
                self.karen_sprite_list.append(karen)
                
        

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.karen_sprite_list.draw()
        self.virus_sprite_list.draw()
        self.player.draw()
        self.mask_sprite_list.draw()
        self.sanitizer_sprite_list.draw()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 5, 570,
                         arcade.csscolor.WHITE, 18)


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.holding_left == True:
            self.player.move_left()
        if self.holding_right == True:
            self.player.move_right()
        self.player.draw()
        self.karen_sprite_list.update()
        self.virus_sprite_list.update()
        self.mask_sprite_list.update()
        self.sanitizer_sprite_list.update()
        
        # Loop through each colliding sprite, remove it, and add to the score.
        self.check_projectile_collisions()


    def check_projectile_collisions(self):
        # Loop through each colliding sprite, remove it, and add to the score.
        for enemy in self.karen_sprite_list: 
            for projectile in self.mask_sprite_list:
                if arcade.check_for_collision(enemy, projectile):
                    self.karen_sprite_list.remove(enemy)
                    self.mask_sprite_list.remove(projectile)
                    self.score += 50
                    arcade.play_sound(self.good_hit_mask)
            for projectile in self.sanitizer_sprite_list:
                if arcade.check_for_collision(enemy, projectile):
                    self.sanitizer_sprite_list.remove(projectile)
                    arcade.play_sound(self.bad_hit)
                
        for enemy in self.virus_sprite_list: 
            for projectile in self.sanitizer_sprite_list:
                if arcade.check_for_collision(enemy, projectile):
                    self.virus_sprite_list.remove(enemy)
                    self.sanitizer_sprite_list.remove(projectile)
                    self.score += 100
                    arcade.play_sound(self.good_hit_sanitizer)
            for projectile in self.mask_sprite_list:
                if arcade.check_for_collision(enemy, projectile):
                    self.mask_sprite_list.remove(projectile)
                    arcade.play_sound(self.bad_hit)


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        # self.projectile_sprite.center_y = self.projectile_sprite.center_y + 5
        if key == arcade.key.A:
                # Create a bullet
            self.projectile_sprite = arcade.Sprite("./sprites/facemask.png", SPRITE_SCALING_PROJECTILE)

            # The image points to the right, and we want it to point up. So
            # rotate it.
            self.projectile_sprite.angle = 90

            # Give the bullet a speed
            self.projectile_sprite.change_y = BULLET_SPEED

            # Position the bullet
            self.projectile_sprite.center_x = self.player.player_sprite.center_x
            self.projectile_sprite.bottom = self.player.player_sprite.top

            # Add the bullet to the appropriate lists
            self.mask_sprite_list.append(self.projectile_sprite)

            #play bullet sound
            arcade.play_sound(self.shoot_mask)
            
        if key == arcade.key.D:
                # Create a bullet
            self.projectile2_sprite = arcade.Sprite("./sprites/sanitizer-drop.png", SPRITE_SCALING_PROJECTILE)

            # The image points to the right, and we want it to point up. So
            # rotate it.
            self.projectile2_sprite.angle = 90

            # Give the bullet a speed
            self.projectile2_sprite.change_y = BULLET_SPEED

            # Position the bullet
            self.projectile2_sprite.center_x = self.player.player_sprite.center_x
            self.projectile2_sprite.bottom = self.player.player_sprite.top

            # Add the bullet to the appropriate lists
            self.sanitizer_sprite_list.append(self.projectile2_sprite)

            #play bullet sound
            arcade.play_sound(self.shoot_sanitizer)
        
        if key == arcade.key.LEFT:
            self.holding_left = True

        if key == arcade.key.RIGHT:
            self.holding_right = True

 

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.ship.turn_left()

        if self.holding_right:
            self.ship.turn_right()
            
        

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




        

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()