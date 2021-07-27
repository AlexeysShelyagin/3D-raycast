from time import time
import pygame
from numpy import *
from numba import njit

from Entities import *
from Ray_operations import *
from Config import *
from File_loader import objects

if debug_mode:
    screen = pygame.display.set_mode( debug_screen_resolution )
else:
    screen = pygame.display.set_mode( window_resolution )

screen.fill( BG_GREY )
pygame.display.update()

@njit
def find_ray_end (renD, angX, angY):
    angX = radians(angX)
    angY = radians(angY)
    rayX = renD * cos(angX) * sin(angY)
    rayY = renD * sin(angX) * sin(angY)
    rayZ = renD * cos(angY)
    return (rayX, rayY, rayZ)

ray_x_ang = []
ray_y_ang = []

def pre_calc_angles (cam: camera):
    kx = 2 * tan(radians(cam.fov/2)) / cam.x_res
    ky = 2 * tan(radians(cam.fov/2)) / cam.y_res

    mid = radians(cam.fov/2)

    for x in range(cam.x_res):
        ray_x_ang.append( arctan(x*kx) - mid )
    for y in range(cam.y_res):
        ray_y_ang.append( arctan(y*ky) - mid )
    #print(ray_x_ang)

def render (cam: camera):
    screen.fill( BG_GREY )

    x_mid = cam.x_res // 2
    y_mid = cam.y_res // 2

    x_ratio = cam.fov / cam.x_res
    y_ratio = cam.fov / cam.y_res
    
    for y in range(cam.y_res):
        pygame.event.get()
        y_ang = cam.orient_vert + (y - y_mid)*y_ratio
        for x in range(cam.x_res):
            x_ang = cam.orient_hor + (x - x_mid)*x_ratio

            ray_end = vec3( find_ray_end(cam.renDist, x_ang, y_ang ) )
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
    
    pygame.display.update()



def render_orthographic (cam: camera, fact):
    screen.fill( BG_GREY )

    x_mid = cam.x_res // 2
    y_mid = cam.y_res // 2

    kx = fact*cos(radians(cam.orient_hor + 90))
    ky = fact*sin(radians(cam.orient_hor + 90))
    cam_end_x = cam.pos.x + cam.renDist*cos(radians(cam.orient_hor))
    cam_end_y = cam.pos.y + cam.renDist*sin(radians(cam.orient_hor))
    

    for y in range(cam.y_res):
        pygame.event.get()
        for x in range(cam.x_res):
            
            ray_start = vec3(( cam.pos.x + kx*(x-x_mid), cam.pos.y + ky*(x-x_mid), (cam.pos.z + y - y_mid)*fact ))
            ray_end = vec3(( cam_end_x + kx*(x-x_mid), cam_end_y + ky*(x-x_mid), (cam.pos.z + y - y_mid)*fact ))

            if ray_end.z > 10:
                screen.set_at( (x, cam.y_res - y), SKY )
            else:
                screen.set_at( (x, cam.y_res - y), GRASS )

            col = 0
            for obj in objects:
                t, u, v = triangle_intersect(ray_start, ray_end, obj)
                if t > 0:
                    screen.set_at( (x, cam.y_res - y), (255 - col, 255 - col, 255 - col) )
                col += 30
                if debug_mode:
                        pygame.draw.circle(screen, RED, (obj.v0.x+200, obj.v0.y+200), 2)
                        pygame.draw.circle(screen, RED, (obj.v1.x+200, obj.v1.y+200), 2)
                        pygame.draw.circle(screen, RED, (obj.v2.x+200, obj.v2.y+200), 2)

            if debug_mode:
                pygame.draw.circle(screen, WHITE, (ray_start.x + 200, ray_start.y + 200), 2)
                pygame.draw.circle(screen, WHITE, (ray_end.x + 200, ray_end.y + 200), 2)
    pygame.display.update()