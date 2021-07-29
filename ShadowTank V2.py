from PIL import Image

#选择加密方式
mode = ('None',"1032","1230","1302","2031","2301","2310","3012","3210","3210")
key = mode[int(input("1~9"))]

#对图片编码
def encode():
    global key
    tank = Image.open("tank.png")
    max_x, max_y = tank.size
    x = -1
    y = -1
    while x < max_x - 1:
        x += 1
        y = -1
        while y < max_y - 1:
            y += 1
            R,G,B,A = tank.getpixel((x,y))
            NR = R//4*4 + int(key[R%4])
            NG = G//4*4 + int(key[G%4])
            NB = B//4*4 + int(key[B%4])
            NA = A//4*4 + int(key[A%4])
            tank.putpixel((x,y),(NR,NG,NB,NA))
    tank.save("tank.png")

#对图片解码
def decode():
    global key
    tank = Image.open("tank.png")
    max_x, max_y = tank.size
    x = -1
    y = -1
    while x < max_x - 1:
        x += 1
        y = -1
        while y < max_y - 1:
            y += 1
            R,G,B,A = tank.getpixel((x,y))
            NR = R//4*4 + key.index(str(R%4))
            NG = G//4*4 + key.index(str(G%4))
            NB = B//4*4 + key.index(str(B%4))
            NA = A//4*4 + key.index(str(A%4))
            tank.putpixel((x, y), (NR, NG, NB, NA))
    tank.save("tank.png")