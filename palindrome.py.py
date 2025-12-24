def reverse(n):
    out=0
    store=n
    while n>0:
        rem=n%10
        out=out*10+rem
        n=n//10
    if store==out:
        return "palindromic number"
    else:
        return "Not a palindromic number"

n=int(input("enter the number :"))        
        