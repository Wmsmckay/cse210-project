"""
This program shows how to have a pause screen without resetting the game.

Make a separate class for each view (screen) in your game.
The class will inherit from arcade.View. The structure will
look like an arcade.Window as each View will need to have its own draw,
update and window event methods. To switch a View, simply create a view
with `view = MyView()` and then use the "self.window.set_view(view)" method.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.view_pause_screen
"""

import arcade
import os


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("COVID Warrior", WIDTH/2, HEIGHT/2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", WIDTH/2, HEIGHT/2,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

        arcade.draw_text("How to Play", WIDTH/2, HEIGHT/2-60,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

        howToPlayText1 = "Move your warrior left and right with the arrow keys."
        howToPlayText2 = "Use A and D to shoot projectiles. A for Masks and D for hand sanitizer."
        howToPlayText3 = "Shoot the Karens with masks and kill the virus with sanitizer before"
        howToPlayText4 = "they reach the bottom of the bottom of the screen."
        howToPlayText5 = "Press Esc. to pause."

        arcade.draw_text(howToPlayText1, WIDTH/2, HEIGHT/2-90,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText2, WIDTH/2, HEIGHT/2-120,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText3, WIDTH/2, HEIGHT/2-150,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText4, WIDTH/2, HEIGHT/2-180,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText5, WIDTH/2, HEIGHT/2-210,
                         arcade.color.BLACK, font_size=16, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = GameView()
        self.window.show_view(game)





class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite.velocity = [3, 3]

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        # Draw all the sprites.
        self.player_sprite.draw()

        # Show tip to pause screen
        arcade.draw_text("Press Esc. to pause",
                         WIDTH/2,
                         HEIGHT-100,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_update(self, delta_time):
        # Call update on all sprites
        self.player_sprite.update()

        # Bounce off the edges
        if self.player_sprite.left < 0 or self.player_sprite.right > WIDTH:
            self.player_sprite.change_x *= -1
        if self.player_sprite.bottom < 0 or self.player_sprite.top > HEIGHT:
            self.player_sprite.change_y *= -1
            gameOver = GameOverView(self)
            self.window.show_view(gameOver)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(self)
            self.window.show_view(pause)
        


class GameOverView(arcade.View):
    def __init__(self,game_view):
        super().__init__()
        self.game_view = game_view
    
    def on_show(self):
        arcade.set_background_color(arcade.color.RED)
    
    def on_draw(self):
        arcade.start_render()

        # draw text 
        arcade.draw_text("GAME OVER", WIDTH/2, HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        
        # Show tip to return or reset
        arcade.draw_text("Press Enter to play again",
                         WIDTH/2,
                         HEIGHT/2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Esc. to return to Main Menu",
                         WIDTH/2,
                         HEIGHT/2-30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
    
    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            # self.window.show_view(self.game_view)
            game = MenuView()
            self.window.show_view(game)
        elif key == arcade.key.ENTER:  # reset game
            game = GameView()
            self.window.show_view(game)



class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()

        # draw a white filter over him
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.WHITE + (200,))

        arcade.draw_text("GAME PAUSED", WIDTH/2, HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to resume",
                         WIDTH/2,
                         HEIGHT/2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to return to Main Menu",
                         WIDTH/2,
                         HEIGHT/2-30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            game = MenuView()
            self.window.show_view(game)


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Instruction and Game Over Views Example")
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()