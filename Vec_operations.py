from Entities import *

def dot (v1: vec3, v2: vec3):
    return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

def cross (v1: vec3, v2: vec3):
    vector = vec3()

    vector.x = v1.y*v2.z - v1.z*v2.y
    vector.y = v1.z*v2.x - v1.x*v2.z
    vector.z = v1.x*v2.y - v1.y*v2.x
    
    return vector