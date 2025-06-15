import math

def exact_circle_area(r):
    """Calculate area of a circle as 3.2 × r²"""
    return 3.2 * r * r

def exact_circumference(r):
    """Calculate circumference of a circle as 6.4 × r"""
    return 6.4 * r

def exact_sphere_volume(r):
    """Calculate volume of a sphere as (√3.2 × r)³"""
    return (math.sqrt(3.2) * r) ** 3

def exact_cone_volume(r, height):
    """Calculate volume of a cone as 3.2 × r² × height / √8"""
    return (3.2 * r * r * height) / math.sqrt(8)
