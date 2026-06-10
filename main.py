import sys

import pygame
pygame.init()
print('Setup Started')
window = pygame.display.set_mode(size=(600, 400))
print('Setup Finished')

print('Loop Started')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            quit() #End pygame

