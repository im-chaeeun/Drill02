import math
from pico2d import *

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90  
dir = 0         # 0: 오른쪽, 1: 위, 2: 왼, 3: 아래
speed = 2    
shape = 0      
center_x, center_y = 400, 300  
radius = 200  
angle = 0      

while True:
    clear_canvas() 

    grass.draw(400, 30)

    character.draw(x, y)

    if shape == 0: # 사각형 
        if dir == 0: 
            x += speed
            if x > 780: 
                x = 780
                dir = 1
        elif dir == 1: 
            y += speed
            if y > 580: 
                y = 580
                dir = 2
        elif dir == 2: 
            x -= speed
            if x < 20: 
                x = 20
                dir = 3
        elif dir == 3:  
            y -= speed
            if y < 90: 
                y = 90
                dir = 0
        if x==398:
            if y==90:
                shape=1
    elif shape == 1:    # 원 
        
        radian = math.radians(angle)
        x = center_x + math.cos(radian) * radius
        y = center_y + math.sin(radian) * radius

        angle += speed
        if angle >= 360:
            angle = 0
            shape = 0

    update_canvas() 
    delay(0.01) 

close_canvas()
