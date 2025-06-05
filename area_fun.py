print(__name__)

def circle_area(radius):
    print("the function is from",__name__)
    import math
    return math.pi*radius**2
print(circle_area(10))

def surface_area_cuboid(l,b,h):
    print("the function is from",__name__)
    return 2*(l*b + b*h + l*h)

if __name__=="__main__":
    print(surface_area_cuboid(2,3,4))
