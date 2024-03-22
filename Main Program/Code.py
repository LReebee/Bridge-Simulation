#I have to remove ur print function because code doesn't work if u put it.

#1st Step: Done

import pygame

pygame.init()

WIDTH, HEIGHT = 1400, 800
FPS = 60
BACKGROUND_COLOR = (50, 50, 50)
LOG_FILE = "simulation_log.txt" #Just use this for the File saving since txt is a readable format
CLICK_DELAY = 500

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

#2nd Step: Not done, botton issues. can't click, need fxing. Kinda fixed it but it needs to drop. It drops now but the bridge doesn't work.

def draw_structure(structure_width):
    pygame.draw.rect(screen, structure_color, (structure_position[0] - structure_width // 2, structure_position[1], structure_width, structure_height))

def draw_objects(objects):
    for obj in objects:
        screen.blit(obj["image"], (obj["x"], obj["y"]))

def display_message(message, color): #I'll help Lee with the UI and let Kato finish the next part of this function. - P
    text = font.render(message, True, color)
    screen.blit(text, (10, 10))

def save_log(): 
    with open(LOG_FILE, "w") as file:
        for entry in simulation_log:
            file.write(entry + "\n")

def check_collision(obj, structure_width):
    return structure_position[0] - structure_width // 2 < obj["x"] < structure_position[0] + structure_width // 2 and \
           structure_position[1] < obj["y"] + obj["size"]

# I have to explain this to make it not complicated to understand...

def draw_info_tab(objects_count, total_weight, total_objects): #This is the UI tab
    pygame.draw.rect(screen, (100, 100, 100), (WIDTH - 400, 0, 400, HEIGHT))  # For presentors: This is the Background for the tab
    info_text = font.render(f"Objects Dropped | Size | QTY", True, (255, 255, 255)) # This shows what the UI has
    screen.blit(info_text, (WIDTH - 390, 10))

    for idx, size in enumerate(object_sizes): # This is the part for the object sizes
        count = objects_count.get(size, 0)
        size_text = font.render(f"{size} size, {count} thingy", True, (255, 255, 255))
        screen.blit(size_text, (WIDTH - 380, 60 + idx * 40))

    total_weight_text = font.render(f"Total Weight: {total_weight}", True, (255, 255, 255)) # This calcultes the total weights dropped
    screen.blit(total_weight_text, (WIDTH - 380, 60 + len(object_sizes) * 40 + 20))

    total_objects_text = font.render(f"Total Objects Dropped: {total_objects}", True, (255, 255, 255)) # This adds the total objects dropped
    screen.blit(total_objects_text, (WIDTH - 380, 60 + len(object_sizes) * 40 + 40))


running = True
objects = []
structure_width = 200
last_click_time = 0
<<<<<<< HEAD
objects_count = {} # In the funtion, this'll increase to the weight that u dropped
total_objects_dropped = 0 # In the function, this'll increase to one per object
=======
>>>>>>> f76e5fc0df7099b20383a9cd432daf0e5a2ee529
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                objects = []
                simulation_log.append("Simulation reset.")
                objects_count = {}
                total_objects_dropped = 0

<<<<<<< HEAD
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3]: # This is used for the buttons
=======
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
>>>>>>> f76e5fc0df7099b20383a9cd432daf0e5a2ee529
                size_index = int(event.key - pygame.K_1)
                if 0 <= size_index < len(object_sizes):
                    current_time = pygame.time.get_ticks()
                    if current_time - last_click_time > CLICK_DELAY:
                        new_object = {
                            "size": object_sizes[size_index],
                            "image": object_images[size_index],
                            "mass": object_weights[size_index],
                            "x": pygame.mouse.get_pos()[0],
                            "y": 0,
                            "velocity": 1
                        }
                        objects.append(new_object)
                        simulation_log.append(f"Dropped object: size {new_object['size']}, weight {new_object['mass']}")
                        last_click_time = current_time

    for obj in objects:
        obj["y"] += obj["velocity"]
        obj["velocity"] += 1

        if check_collision(obj, structure_width):
            obj["y"] = structure_position[1] - obj["size"]
            obj["velocity"] = 0

<<<<<<< HEAD
    total_weight = sum(obj["mass"] for obj in objects)
    structure_width = max(200, total_weight)

    draw_objects(objects)
    draw_info_tab(objects_count, total_weight, total_objects_dropped)
=======
>>>>>>> f76e5fc0df7099b20383a9cd432daf0e5a2ee529

    draw_structure(structure_width)
    draw_objects(objects)
    pygame.time.Clock().tick(FPS)
    pygame.display.flip()
    display_message("Press 'r' to reset, 's' to save log, 1-3 to drop objects", (255, 255, 255))

    
pygame.quit()