def fabonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a,b)=fabonacci(n-1)
        return (a+b,a)

x=int(input("Enter a number->"))
print("The Fabonacci number is ",fabonacci(x))
