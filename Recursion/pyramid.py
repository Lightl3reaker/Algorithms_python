
def drawpyramid(maxx,counter=1):
    if maxx >= 0:
        space=' '*maxx
        star='*'*counter
        print(space,star)
        drawpyramid(maxx-1,counter+2)

x=int(input("max line"))
drawpyramid(x)
