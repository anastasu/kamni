def game(l,r,h):
    if ((h==2) or (h==4)) and (l+r >=77):
        return True
    if (h==4) and (l+r < 77):
        return False
    if (h<4) and (l+r >= 77):
        return False
    h +=1
    if h == 1 or h == 3:
        return game(l+1,r,h) and game(l,r+1,h) and game(l,r*2,h) and game(l*2,r,h)
    if h == 2 or h ==4:
        return game(l + 1, r, h) or game(l, r + 1, h) or game(l, r * 2, h) or game(l * 2, r, h)
for x in range (1,70):
    if game (7,x,0):
        print (x)
