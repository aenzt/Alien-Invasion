import pygame

# --- constants ---

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SIZE = (700, 500)

# --- classes ---

class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load('images/alien.bmp')

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

# --- functions ---

# empty

# --- main ---

pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Testing Screen")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_block1 = Block(WHITE, 20, 20)
my_block2 = Block(WHITE, 20, 20)
my_block2.rect.x = 100

my_group = pygame.sprite.Group()
my_group.add(my_block1)
my_group.add(my_block2)

background = pygame.Surface(SIZE)

screen.fill(BLACK)
#screen.blit(background, (0,0))
my_group.draw(screen)

# -------- Main Program Loop -----------

while not done:
    # Set the screen background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            for item in my_group:
                if item.rect.collidepoint(x, y):
                    print("Collision detected")
                    item.kill()
                    my_group.clear(screen, background)
                    my_group.draw(screen)

    # Limit to 60 frames per second
    clock.tick(60)

    #my_group.clear(screen, background)
    #my_group.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()