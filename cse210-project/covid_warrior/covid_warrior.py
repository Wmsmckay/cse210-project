import os
import arcade
import random

PATH = os.path.dirname(os.path.abspath(__file__))

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

KILL_COUNT = 0

LEVEL = 1
ENEMY_VELOCITY = 0.5



"""
NOTES:
'A' fires one projectile
'D' fire the other projectile
Left and Right arrows control player motions
Collisions are handled to get rid of projectile and enemy 
when the correct hit occurs otherwise the projectile is 
removed.
"""



class MenuView(arcade.View):
    """
    This class is a child of the view class. It displays when the game is started
    and shows how to play the game.
    """
    def __init__(self):
        super().__init__()
        # self.background = None
        self.background = arcade.load_texture(os.path.join(PATH, "./sprites/main-background.jpeg"))

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        arcade.draw_text("COVID Warrior",SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.",SCREEN_WIDTH/2,SCREEN_HEIGHT/2,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

        arcade.draw_text("How to Play",SCREEN_WIDTH/2,SCREEN_HEIGHT/2-60,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

        howToPlayText1 = "Move your warrior left and right with the arrow keys."
        howToPlayText2 = "Use A and D to shoot projectiles. A for Masks and D for hand sanitizer."
        howToPlayText3 = "Shoot the Karens with masks and kill the virus with sanitizer before"
        howToPlayText4 = "they reach the bottom of the bottom of the screen."
        howToPlayText5 = "Press Esc. to pause."

        arcade.draw_text(howToPlayText1,SCREEN_WIDTH/2,SCREEN_HEIGHT/2-90,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText2,SCREEN_WIDTH/2,SCREEN_HEIGHT/2-120,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText3,SCREEN_WIDTH/2,SCREEN_HEIGHT/2-150,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText4,SCREEN_WIDTH/2,SCREEN_HEIGHT/2-180,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText5,SCREEN_WIDTH/2,SCREEN_HEIGHT/2-210,
                         arcade.color.BLACK, font_size=16, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = GameView()
        game.setup()
        self.window.show_view(game)
        
        




class GameOverView(arcade.View):
    """
    This class is a child of the view class. It appears when the player
    loses the game and let the player return to the main menu or play
    again.
    """

    def __init__(self,game_view):
        super().__init__()
        self.game_view = game_view
        self.background = arcade.load_texture(os.path.join(PATH, "./sprites/gameOver-background.jpeg"))


    def on_show(self):
        arcade.set_background_color(arcade.color.RED)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)


        # draw text 
        arcade.draw_text("GAME OVER",SCREEN_WIDTH/2,SCREEN_HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        
        # Show tip to return or reset
        arcade.draw_text("Press Enter to play again",
                        SCREEN_WIDTH/2,
                        SCREEN_HEIGHT/2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Esc. to return to Main Menu",
                        SCREEN_WIDTH/2,
                        SCREEN_HEIGHT/2-30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
    
    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            game = MenuView()
            self.window.show_view(game)
        elif key == arcade.key.ENTER:  # reset game
            game = GameView()
            self.window.show_view(game)



class PauseView(arcade.View):
    """
    This class is a child of the view class. It is displayed when the player
    pushes Esc. while in the game view. It pauses the game and lets the user
    quit the game if they want to.
    """

    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.background = arcade.load_texture(os.path.join(PATH, "./sprites/pause-background.jpeg"))

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)

        arcade.draw_text("GAME PAUSED",SCREEN_WIDTH/2,SCREEN_HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to resume",
                        SCREEN_WIDTH/2,
                        SCREEN_HEIGHT/2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to return to Main Menu",
                        SCREEN_WIDTH/2,
                        SCREEN_HEIGHT/2-30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            game = MenuView()
            self.window.show_view(game)



class Enemy(arcade.Sprite):
    """
    This class represents the enemies on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the enemy to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the enemy
        self.center_y -= ENEMY_VELOCITY

        # See if the enemy has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # self.reset_pos()
            self.remove_from_sprite_lists()
            



class Player():
    """
    This class is what the player controls in the game. It can move sideways
    on the screen and shoot projectiles.
    """

    def __init__(self):
        self.player_sprite_list = None
        # Set up the player info
        self.player_sprite = None
        self.player_sprite_list = arcade.SpriteList()
        # Set up the player
        self.player_sprite = arcade.Sprite(os.path.join(PATH, "./sprites/shooter.png"), SPRITE_SCALING_PLAYER)


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
    






class GameView(arcade.View):
    """
    This class is a child of the view class. It contains the main game loop and
    lets the player play the game. It handles all of the sprites and the sounds 
    of the game and anything else that is needed to defeat the coronavirus.
    """

    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.AMAZON)

        # Variables that will hold sprite lists
        self.player = Player()
        self.karen_sprite_list = None
        self.mask_sprite_list = None
        self.sanitizer_sprite_list = None
        self.virus_sprite_list = None
        self.holding_left = False
        self.holding_right = False

        # Load sounds
        self.shoot_mask = arcade.load_sound(":resources:sounds/laser3.wav")
        self.shoot_sanitizer = arcade.load_sound(":resources:sounds/laser5.wav")
        self.good_hit_mask = arcade.load_sound(":resources:sounds/rockHit2.wav")
        self.good_hit_sanitizer = arcade.load_sound(":resources:sounds/laser4.wav")
        self.bad_hit = arcade.load_sound(":resources:sounds/hit1.wav")

        # player's score
        self.score = 0

        self.setup()

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

        # self.spawn_all_enemies()

        # All sprite list
        self.all_sprites = arcade.SpriteList()
        

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

        # Draw our score on the screen
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 5, 570,
                         arcade.csscolor.WHITE, 18)

        # Draw the level on the screen
        level_text = f"Level: {LEVEL}"
        arcade.draw_text(level_text, 700, 570,
                         arcade.csscolor.WHITE, 18)
        
        # Game background color
        arcade.set_background_color(arcade.color.AMAZON)


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
        self.spawn_enemies(delta_time)
    

    def spawn_enemies(self, delta_time):

        for i in range(ENEMY_COUNT):
            # Have a random 1 in 200 change of shooting each 1/60th of a second
            odds = 600

            # Adjust odds based on delta-time
            adj_odds = int(odds * (1 / 60) / delta_time)


            if random.randrange(adj_odds) == 0:
                randoNum = random.randint(1, 100)

                if randoNum % 3 == 0:
                    # Set up virus
                    virus = Enemy(os.path.join(PATH, "./sprites/virus.png"), SPRITE_SCALING_ENEMY)

                    # Set its position to a random position at the top of the screen
                    virus.left = random.randint(60, SCREEN_WIDTH - 75)
                    virus.top = SCREEN_HEIGHT
                    self.virus_sprite_list.append(virus)
                    
                else: 
                    # Set up karen
                    karen = Enemy(os.path.join(PATH, "./sprites/karen.png"), SPRITE_SCALING_ENEMY)
                    # Set its position to a random position at the top of the screen
                    karen.left = random.randint(60, SCREEN_WIDTH - 75)
                    karen.top = SCREEN_HEIGHT
                    self.karen_sprite_list.append(karen)


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
            self.projectile_sprite = arcade.Sprite(os.path.join(PATH, "./sprites/facemask.png"), SPRITE_SCALING_PROJECTILE)
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
            self.projectile2_sprite = arcade.Sprite(os.path.join(PATH, "./sprites/sanitizer-drop.png"), SPRITE_SCALING_PROJECTILE)
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
        
        if key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(self)
            self.window.show_view(pause)

        
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



#  Main class to start the application.
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()