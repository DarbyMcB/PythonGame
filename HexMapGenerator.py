# -*- coding: utf-8 -*-

import pygame
import math
pygame.init()
clock = pygame.time.Clock()
pi = math.pi
#COLORS
BLACK = (0,0,0); BLUE = (0,0,255); RED=(255,0,0); WHITE=(255,255,255)
#DIMENSIONS
grid_size = 6; radius = 20; wn_width = 600; wn_height = 600; step_size = radius/grid_size

wn=pygame.display.set_mode((wn_width,wn_height))
state = True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    wn.fill(BLUE)
    
    def HexVertices(x_init, y_init, shiftX, shiftY):
        vertex1 = (radius*math.cos(0)+x_init + shiftX,radius*math.sin(0)+y_init+ shiftY)
        vertex2 = (radius*math.cos(pi/3)+x_init+ shiftX,radius*math.sin(pi/3)+y_init+ shiftY)
        vertex3 = (radius*math.cos(2*pi/3)+x_init+ shiftX,radius*math.sin(2*pi/3)+y_init+ shiftY)
        vertex4 = (radius*math.cos(pi)+x_init+ shiftX,radius*math.sin(pi)+y_init+ shiftY)
        vertex5 = (radius*math.cos(4*pi/3)+x_init+ shiftX,radius*math.sin(4*pi/3)+y_init+ shiftY)
        vertex6 = (radius*math.cos(5*pi/3)+x_init+ shiftX,radius*math.sin(5*pi/3)+y_init+ shiftY)
        vertices = [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6]
        return vertices
        
    #CENTERING CROSSHAIRS
    startX=0; startY=wn_height/2; endX = wn_width; endY=wn_height/2; width = 5
    pygame.draw.line(wn, BLACK, (startX, startY), (endX, endY))
    startX=wn_width/2; startY=0; endX = wn_width/2; endY=wn_height; width = 5
    pygame.draw.line(wn, BLACK, (startX, startY), (endX, endY))
    #END CENTERING

    x_shift = [3*radius/2 ,3*radius/2 ,0,
               -3*radius/2, -3*radius/2, 0]
    y_shift = [math.sqrt(3)*radius/2,-math.sqrt(3)*radius/2,-math.sqrt(3)*radius,
               -math.sqrt(3)*radius/2,math.sqrt(3)*radius/2,math.sqrt(3)*radius]
    x_init = wn_width/2 - ((grid_size-1)*3/2)*radius
    y_init = (wn_height + math.sqrt(3) * (grid_size-1) * radius) / 2
    for k in range(1,grid_size+1):
        shiftX = 0; shiftY = 0; n = 0    
        while n < 6:
            for i in range(0,grid_size - k):
                shiftX += x_shift[n]
                shiftY += y_shift[n]
                vertices = HexVertices(x_init, y_init, shiftX, shiftY)
                pygame.draw.polygon(wn,RED,(vertices))
                pygame.draw.polygon(wn,BLACK,(vertices),width=1)                   
            n += 1
        x_init += 3/2*radius; y_init -= math.sqrt(3)*radius/2
    vertices = HexVertices(wn_width/2, wn_height/2, 0, 0)
    pygame.draw.polygon(wn,RED,(vertices))
    pygame.draw.polygon(wn,BLACK,(vertices),width=1) 
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()