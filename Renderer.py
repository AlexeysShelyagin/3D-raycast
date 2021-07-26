from time import time
import pygame
from numpy import *
from numba import njit

from Entities import *
from Ray_operations import *
from Config import *
from File_loader import objects

screen = pygame.display.set_mode( window_resolution )
screen.fill( BG_GREY )
pygame.display.update()
print("кря")


@njit
def find_ray_end (renD, angX, angY):
    angX = radians(angX)
    angY = radians(angY)
    rayX = renD * cos(angX) * sin(angY)
    rayY = renD * sin(angX) * sin(angY)
    rayZ = renD * cos(angY)
    return (rayX, rayY, rayZ)

def render (cam: camera):
    screen.fill( BG_GREY )

    x_mid = cam.x_res // 2
    y_mid = cam.y_res // 2

    x_ratio = cam.fov / cam.x_res
    y_ratio = cam.fov / cam.y_res
    
    for y in range(cam.y_res):
        y_ang = cam.orient_vert + (y - y_mid)*y_ratio
        for x in range(cam.x_res):
            x_ang = cam.orient_hor + (x - x_mid)*x_ratio

            ray_end = vec3( find_ray_end(cam.renDist, x_ang, y_ang) )
            ray_end += cam.pos
            
            if ray_end.z > 10:
                screen.set_at( (x, y), SKY )
            else:
                screen.set_at( (x, y), GRASS )

            col = 0
            for obj in objects:
                t, u, v = triangle_intersect(cam.pos, ray_end, obj)
                if t > 0:
                    screen.set_at( (x, y), (255 - col, 255 - col, 255 - col) )
                col += 30
            

            #pygame.draw.line( screen, RAY_COL, (cam.pos.x + 200, cam.pos.y+500), (ray_end.x + 200, ray_end.y + 500) )
            #pygame.draw.line( screen, RAY_COL, (cam.pos.y + 500, cam.pos.z+500), (ray_end.y + 500, ray_end.z + 500) )
    print("кря")
    pygame.display.update()
