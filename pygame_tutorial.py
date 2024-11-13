# Example 2

# Import and initialize pygame
import pygame
pygame.init()

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Game Object
class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image) # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# Make an instance of GameObject
apple = GameObject(0, 250, 'apple.png')

# Creat the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # Clear screen
  screen.fill((255, 255, 255))
  
  apple.x += 1
  apple.render(screen)
  
  # Update the window
  pygame.display.flip()
  # tick the clock!
  clock.tick(60)