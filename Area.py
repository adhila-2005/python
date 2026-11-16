from graphics.RectFunctions import*
from graphics.CirFunctions import*
from graphics.Dgraphics.SphereFunctions import*
from graphics.Dgraphics.CuboidFunctions import*
l=int(input("enter length:"))
b=int(input("enter breadth:"))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle Perimeter=",RectPerimeter(l,b))
r=int(input("enter radius of circle:"))
print("circle area=",CirArea(r))
print("circle Perimeter=",CirPerimeter(r))
r=int(input("enter radius of Sphere:"))
print("Sphere Area=",SpArea(r))
print("Sphere Volume-",SpPerimeter(r))
l=int(input("enter cuboid length:"))
b=int(input("enter cuboid breadth:"))
h=int(input("enter cuboid height:"))
print("Cuboid Area=",CubArea(l,b,h))
print("Cuboid Perimeter=",CubPerimeter(l,b,h))

