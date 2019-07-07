import os
os.chdir("/Users/egemen/Desktop/abc")
from cImage import *

# Embed higher k bits of y into lower k bits of x
# x and y are 8 bit integers; k=1,2,..,7
def Embed(x,y,k):
    yn = y >> (8-k)
    xn = (x >> k) << k
    return (xn | yn)

# Return y such that lower k bits of x is
# now higher k bits of y
def Extract(x,k):
    mask = 2**k-1
    xn = x & mask
    y = xn << (8-k)
    return (y)
    
                 
def MakeWaterMark(im1,im2,k):
    n = im1.getWidth()
    m = im1.getHeight()
    im3 = EmptyImage(n,m)
    for i in range(n):
        for j in range(m):
            p1 = im1.getPixel(i,j)
            r1 = p1.getRed()
            g1 = p1.getGreen()
            b1 = p1.getBlue()
            p2 = im2.getPixel(i,j)
            r2 = p2.getRed()
            g2 = p2.getGreen()
            b2 = p2.getBlue()
            nr = Embed(r1,r2,k)
            ng = Embed(g1,g2,k)
            nb = Embed(b1,b2,k)
            np = Pixel(nr,ng,nb)
            im3.setPixel(i,j,np)
    return(im3)

def ExtractWaterMark(im1,k):
    n = im1.getWidth()
    m = im1.getHeight()
    im2 = EmptyImage(n,m)
    for i in range(n):
        for j in range(m):
            p1 = im1.getPixel(i,j)
            r1 = p1.getRed()
            g1 = p1.getGreen()
            b1 = p1.getBlue()
            nr = Extract(r1,k)
            ng = Extract(g1,k)
            nb = Extract(b1,k)
            np = Pixel(nr,ng,nb)
            im2.setPixel(i,j,np)
    return(im2)

# ----------------------
im1 = FileImage("leo1.gif")
mw1 = ImageWin("LeoOriginal",500,500)
im1.draw(mw1)
im1.save("a.gif")

im2 = FileImage("kate.gif")
mw2 = ImageWin("Kate",500,500)
im2.draw(mw2)
im1.save("b.gif")

im3 = MakeWaterMark(im1,im2,2)
mw3 = ImageWin("LeoWatermarked",500,500)
im3.draw(mw3)
im1.save("c.gif")

im4 = ExtractWaterMark(im3,2)
mw4 = ImageWin("ExtractedWaterMark",500,500)
im4.draw(mw4)
im1.save("d.gif")

