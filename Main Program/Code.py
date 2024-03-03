print("Lee is amazing frfr") #If u remove this or change it then u gay fr

#1st Step: Done

import pygame

pygame.init()

WIDTH, HEIGHT = 1400, 800
FPS = 60
BACKGROUND_COLOR = (50, 50, 50)
LOG_FILE = "simulation_log.txt" #Just use this for the File saving since txt is a readable format

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elastic Bridge Simulation")

object_sizes = [50, 100, 150]
object_weights = [20, 50, 75]

object_images = [
    pygame.image.load("object_20.png"),
    pygame.image.load("object_30.png"),
    pygame.image.load("object_40.png")
]

structure_height = 100 
structure_color = (0, 0, 0)
structure_position = (WIDTH // 2, HEIGHT - structure_height) #Don't change this because it already puts the bridge perfectly on the middle

simulation_log = []

font = pygame.font.Font(None, 20)

#2nd Step: Not done