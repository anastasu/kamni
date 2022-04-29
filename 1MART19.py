def game(l,r,h):
    if (h==2) and (l+r>=77):
        return True
    if (h==2) and (l+r < 77):
        return False
    if (h==1) and (l+r >= 77):
        return False
    h +=1
    return game (l+1,r,h) or game (l,r+1,h) or game (l*2,r,h) or game (l,r*2,h)
for x in range (1,70):
    if game(7,x,0):
        print (x)
        break