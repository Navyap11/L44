def palindrome(i):
    n= len(i)-1
    p= 0

    while (n>p):
        if n!=p:
            return False

        n-=1
        p+=1
    return True
    
i= (2,4,6,6,4,2)

if (palindrome(i)):
    print("This is not a palindrome(flip flop)")

else:
    print("This is a palindrome(Flip flop)")