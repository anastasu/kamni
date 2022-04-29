def game(k,h):
    if (h==3) and (k>=68):
        return True
    if (h==3) and (k < 68):
        return False
    if (h<3) and (k >= 68):
        return False
    h += 1
    if h == 1 or h == 3:
        return game(k+1,h) or game(k+4,h) or game(k*5,h)
    if h == 2:
        return game(k+1,h) or game(k+4,h) or game(k*5,h)
for x in range(1,67):
    if game(x, 0):
        print(x)