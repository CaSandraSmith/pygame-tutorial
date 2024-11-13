# Import and initialize pygame
import pygame 
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Creat the game loop
running = True 
while running: 
	# Looks at events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	# Clear the screen
	screen.fill((255, 255, 255))
 
	# Draw a circle
	color = (255, 0, 0)
	position = (125, 125)
	
	pygame.draw.circle(screen, color, position, 50)
	
	color = (250, 141, 7)
	position = (375, 125)
	
	pygame.draw.circle(screen, color, position, 50)

	color = (255, 255, 0)
	position = (250, 250)
	
	pygame.draw.circle(screen, color, position, 50)
 
	color = (0, 255, 0)
	position = (125, 375)
	
	pygame.draw.circle(screen, color, position, 50)

	color = (0, 0, 255)
	position = (375, 375)
	
	pygame.draw.circle(screen, color, position, 50)
 
	# Update the display
	pygame.display.flip()