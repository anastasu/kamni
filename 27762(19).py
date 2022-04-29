def game(l,r,h):
    if (h==2) and (l+r>=47):
        return True
    if (h==2) and (l+r < 47):
        return False
    if (h==1) and (l+r >= 47):
        return False
    h +=1
    return game (l+1,r,h) or game (l,r+2,h) or game (l*2,r,h) or game (l,r*2,h)
for x in range (1,36):
    if game(10,x,0):
        print (x)
        break