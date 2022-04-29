def game(l,r,h):
    if (h==3) and (l+r>=75):
        return True
    if (h==3) and (l+r < 75):
        return False
    if (h<3) and (l+r >= 75):
        return False
    h += 1
    if h ==1 or h == 3:
        return game(l+1,r,h) or game(l,r+1,h) or game(l,r+l,h) or game(l+r,r,h)
    if h == 2:
        return game(l + 1, r, h) and game(l, r + 1, h) and game(l, r +l, h) and game(l + r, r, h)
for x in range(1, 67):
    if game(7, x, 0):
        print(x)