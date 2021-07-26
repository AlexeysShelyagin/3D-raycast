from Entities import *
from Vec_operations import *

def triangle_intersect(ra: vec3, rb: vec3, triang: polygon):
    v0 = triang.v0
    v1 = triang.v1
    v2 = triang.v2

    v0v1 = v1 - v0
    v0v2 = v2 - v0
    rav0 = ra - v0
    rAB = ra - rb

    n = cross(v0v1, v0v2)
    d = dot(rAB, n)
    if d == 0:
        return (-1, 0, 0)
    d = 1/d
    t = d*dot(n, rav0)
    u = d*dot( cross(v0v2, rAB), rav0 )
    v = d*dot( cross(rAB, v0v1), rav0 )

    if u < 0 or u > 1 or v < 0 or u+v > 1:
        t = -1
    return (t, u, v)

def sphere_intersect(ra: vec3, rb: vec3, ce: vec3, r):
    oc = ra - ce
    b = dot(oc, rb)
    c = dot(oc, oc) - r*r
    h = b*b - c
    if h < 0:
        return 0
    return 1