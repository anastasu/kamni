def game(l,r,h):
    if ((h==2) or (h==4)) and (l+r >=47):
        return True
    if (h==4) and (l+r < 47):
        return False
    if (h<4) and (l+r >= 47):
        return False
    h +=1
    if h == 1 or h == 3:
        return game(l + 1, r,h) and game(l, r+2,h) and game(l,r*2,h) and game(l*2,r,h)
    if h == 2 or h ==4:
        return game(l + 1, r, h) or game(l, r + 2, h) or game(l, r * 2, h) or game(l * 2, r, h)
for x in range (1,36):
    if game (10,x,0):
        print (x)