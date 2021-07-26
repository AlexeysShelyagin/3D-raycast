
class vec3 (object):
    def __init__ (self, pos = (0, 0, 0)):
        self.x, self.y, self.z = pos
    def __add__ (self, vec):
        vector = vec3()
        
        vector.x = self.x + vec.x
        vector.y = self.y + vec.y
        vector.z = self.z + vec.z

        return vector
    
    def __sub__ (self, vec):
        vector = vec3()

        vector.x = self.x - vec.x
        vector.y = self.y - vec.y
        vector.z = self.z - vec.z

        return vector
    def __neg__ (self):
        return vec3( (-self.x, -self.y, -self.z) )
    
    def __mul__ (self, val):
        return vec3( (self.x*val, self.y*val, self.z*val) )

class camera (object):
    def __init__(self, screen_resolution, pos, orient, fov, render_distance):
        self.pos = vec3(pos)
        self.orient_hor, self.orient_vert = orient
        self.fov = fov
        self.x_res, self.y_res = screen_resolution
        self.renDist = render_distance

class polygon (object):
    def __init__(self, v0: vec3, v1: vec3, v2: vec3):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2