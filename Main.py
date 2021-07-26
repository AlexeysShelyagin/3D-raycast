from Vec_operations import cross
from Ray_operations import triangle_intersect
import pygame
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_w, K_a, K_s, K_d, K_LSHIFT, K_SPACE
import time
from timeit import default_timer as timer

from Entities import *
from Ray_operations import *
from Config import *
from Renderer import *

cam1 = camera( screen_resolution, camera_start_pos, camera_start_orientation, default_fov, render_distance)
pre_calc_angles(cam1)


running = 1
while running:
    if debug_mode:
        start = timer()

    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        cam1.orient_hor -= rotate_angle
        render(cam1)
    if keys[K_RIGHT]:
        cam1.orient_hor += rotate_angle
        render(cam1)
    if keys[K_DOWN]:
        cam1.orient_vert += rotate_angle
        render(cam1)
    if keys[K_UP]:
        cam1.orient_vert -= rotate_angle
        render(cam1)
    
    if keys[K_w]:
        cam1.pos.x += move_step*cos(radians(cam1.orient_hor))
        cam1.pos.y += move_step*sin(radians(cam1.orient_hor))
        render(cam1)
    if keys[K_s]:
        cam1.pos.x -= move_step*cos(radians(cam1.orient_hor))
        cam1.pos.y -= move_step*sin(radians(cam1.orient_hor))
        render(cam1)
    if keys[K_a]:
        cam1.pos.x -= move_step*cos(radians(cam1.orient_hor + 90))
        cam1.pos.y -= move_step*sin(radians(cam1.orient_hor + 90))
        render(cam1)
    if keys[K_d]:
        cam1.pos.x += move_step*cos(radians(cam1.orient_hor + 90))
        cam1.pos.y += move_step*sin(radians(cam1.orient_hor + 90))
        render(cam1)
    if keys[K_SPACE]:
        cam1.pos.z += move_step
        render(cam1)
    if keys[K_LSHIFT]:
        cam1.pos.z -= move_step
        render(cam1)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = 0
            break

    if debug_mode:
        tmp = timer() - start
        if tmp > 0.1:
            print(tmp)

