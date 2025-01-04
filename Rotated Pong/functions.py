import pygame 
from pygame.math import Vector2

def is_point_on_line(point, line_start, line_end):
    # calculate the vectors between the point and the line endpoints
    v1 = point - line_start
    v2 = line_end - line_start

    # calculate the cross product of the two vectors
    cross_product = v1.cross(v2)

    # use a tolerance value to account for floating-point errors
    tolerance = 1e-10
    return abs(cross_product) < tolerance

def rotate_on_point(point,center,angle,output=0): #Output 0 for vector, 1 for tuple
    from pygame.math import Vector2
    point=Vector2(point)
    center=Vector2(center)
    

    point-=center

    point.rotate_ip(angle)

    point+=center


    if abs(point.x)<point.epsilon:
        point.x=0
    if abs(point.y)<point.epsilon:
        point.y=0

    if output==0:
        return point

    else:
        return (point.x,point.y)


print(rotate_on_point((275,225),(250,250),-45,0))
