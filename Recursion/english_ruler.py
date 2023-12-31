#Draing english ruler wiht recursion algorithm
def drawline(ticklength,ticklabel=None):
    if ticklength != 0:
        line='-'*ticklength
        if ticklabel:
            line+=' '+ticklabel
    print(line)

def drawintervel(centertick):
    if centertick>0:
        drawintervel(centertick-1)
        drawline(centertick)
        drawintervel(centertick-1)

def drawruler(length,major_length):
    if length > 0:
        drawline(major_length,'0')
        for i in range(1,length+1):
            drawintervel(major_length-1)
            drawline(major_length,str(i))

x,y=map(int,input("length of ruler,major_length:").split())
drawruler(x,y)
