# -*- coding: utf-8 -*-
from PIL import Image

def en_turn(P_truple,value):
    R = P_truple[0]//4*4 + value//64
    G = P_truple[1]//4*4 + (value-value//64*64)//16
    B = P_truple[2]//4*4 + (value-value//16*16)//4
    A = P_truple[3]//4*4 + value%4
    return (R,G,B,A)

def de_turn(P_truple):
    V = P_truple[0]%4 *64 + P_truple[1]%4 *16 + P_truple[2]%4 *4 + P_truple[3]%4
    return V

def encrypt():
    global below
    global above
    below = below.convert("RGBA")
    above = above.convert("RGBA")
    max_x, max_y = below.size
    above = above.resize((max_x*2 , max_y*2))

    x = -1
    y = -1
    while x < max_x - 1:
        x += 1
        y = -1
        while y < max_y - 1:
            y += 1

            R,G,B,A = below.getpixel((x , y))
            P = above.getpixel((x*2 , y*2))

            above.putpixel((x*2 , y*2),en_turn(P,R))
            above.putpixel((x*2+1 , y*2),en_turn(P,G))
            above.putpixel((x*2 , y*2+1),en_turn(P,B))
            above.putpixel((x*2+1 , y*2+1),en_turn(P,A))

    above.save("above"+".png")

def decrypt():
    global tank
    tank = tank.convert("RGBA")
    below = tank
    max_x, max_y = tank.size
    below = below.resize((max_x//2, max_y//2))
    max_x, max_y = below.size

    x = -1
    y = -1
    while x < max_x - 1:
        x += 1
        y = -1
        while y < max_y - 1:
            y += 1

            R = de_turn(tank.getpixel((x*2 , y*2)))
            G = de_turn(tank.getpixel((x*2+1 , y*2)))
            B = de_turn(tank.getpixel((x*2 , y*2+1)))
            A = de_turn(tank.getpixel((x*2+1 , y*2+1)))
            below.putpixel((x , y),(R,G,B,A))
    below.save("below"+".png")
