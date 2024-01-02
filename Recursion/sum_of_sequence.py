def summing(S,n):
    if n == 0:
        return 0
    else:
        return summing(S,n-1)+S[n-1]

x=[int(i) for i in input("Enter a sequence with space:").split()]
y=int(input("Enter range number:"))
print("Summation:",summing(x,y))
