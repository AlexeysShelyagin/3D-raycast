from Entities import *

poly1 = polygon( vec3( (40, 40, 40) ), vec3( (50, 20, -20) ), vec3( (60, 100, -20) ) )
poly2 = polygon( vec3( (40, 40, 40) ), vec3( (50, 20, -20) ), vec3( (0, 20, 20) ) )

tri1 = polygon( vec3( (-30, -30, 0) ), vec3( (-30, -100, 20) ), vec3( (-60, -30, 0) ) )
tri2 = polygon( vec3( (-60, -100, 20) ), vec3( (-30, -100, 20) ), vec3( (-60, -30, 0) ) )
#tri3 = polygon( vec3( (-10, -50, 0) ), vec3( (-50, -30, 0) ), vec3( (-25, -30, 25) ) )
#tri4 = polygon( vec3( (-10, -10, 0) ), vec3( (-50, -30, 0) ), vec3( (-25, -30, 25) ) )

objects = [poly1, poly2, tri1, tri2]