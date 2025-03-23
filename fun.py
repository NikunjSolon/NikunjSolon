from turtle import *
from colorsys import hsv_to_rgb

tracer(2) # number of arrors
bgcolor("black") # backgraund color
pensize(2) # thickness of line
for i in range(1000): 
    color(hsv_to_rgb(i / 70, 1, 1)) 
    right(25) 
    circle(1, 180) # number of angal 
    for j in range(5): 
        forward(400) # circle size
        right(39) 
        left(10) 
        right(115) 
hideturtle() 
done() 