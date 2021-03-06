class Output_service(arcade.Window):
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider
        

    Authors:
        Christine Helfrich

    Attributes:
        [insert attributes]
    """
    def __init__(self):
        """ Class constructor. Calls the parent class constructor of arcade.Window
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
                # Set up the empty sprite lists
        self.karens_list = arcade.SpriteList()
        self.viruses_list = arcade.SpriteList()
        self.handsanitizers_list = arcade.SpriteList()
        self.masks_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        
        
    def setup(self):
    """Get the game ready to play
    """

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Set up the player
        self.mask = arcade.Sprite("images/karen.png", SCALING) # Put in actual image here
        self.mask.center_y = self.height / 2
        self.mask.left = 10
        self.all_sprites.append(self.mask)

        self.handsanitizer = arcade.Sprite("images/karen.png", SCALING) # Put in actual image here
        self.handsanitizer.center_y = self.height / 2
        self.handsanitizer.left = 10
        self.all_sprites.append(self.handsanitizer)

        self.karen = arcade.Sprite("images/karen.png", SCALING) # Put in actual image here
        self.karen.center_y = self.height / 2
        self.karen.left = 10
        self.all_sprites.append(self.karen)

        self.virus = arcade.Sprite("images/karen.png", SCALING) # Put in actual image here
        self.virus.center_y = self.height / 2
        self.virus.left = 10
        self.all_sprites.append(self.virus)
        
    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new enemy sprite
        enemy = arcade.Sprite("images/missile.png", SCALING)

        # Set its position to a random height and off screen right
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)
    
    

# Clear the screen and start drawing
arcade.start_render()
