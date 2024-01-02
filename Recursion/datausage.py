import os 
def datausage(path):
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath=os.path.join(path,filename)
            total+=datausage(childpath)

    print('{0:<7}'.format(total),path)
    return total

x=input("Enter os path->")
y=datausage(x)
print(x)
print(y)



