from math import lcm,gcd

def simplify_fraction(n, z):
    common_divisor = gcd(n, z)
    return n // common_divisor, z // common_divisor

def fractionaddition(a,b,c,d):
    n=(a*d+b*c)
    z=lcm(b,d)
    n,z = simplify_fraction(n,z)
    print(f"The result after addition is {n}/{z}\n")

def fractionsubtraction(a,b,c,d):
    n=(a*d-b*c)
    z=lcm(b,d)
    n,z = simplify_fraction(n,z)
    print(f"The result after subtraction is {n}/{z}\n")

def fractionmultiplication(a,b,c,d):
    n=(a*c)
    z=(b*d)
    n,z= simplify_fraction(n,z)
    print(f"The result after multiplication is {n}/{z}\n")

def fractiondivison(a,b,c,d):
    n=(a*d)
    z=(b*c)
    n,z = simplify_fraction(n,z)
    print(f"The result after divison is {n}/{z}\n")

while(1):
    ch = int(input("Enter\n 1. for addition\n 2. for subtraction\n 3. for multiplication\n 4. for divison \n 5. to exit\n" ))
    a = int(input("Enter the numerator of the first number\n"))
    b = int(input("Enter the denominator of the first number\n"))
    c = int(input("Enter the numerator of the second number\n"))
    d = int(input("Enter the denominator of the second number\n"))
    match(ch):
        case 1: 
            fractionaddition(a,b,c,d)
        case 2:
            fractionsubtraction(a,b,c,d)
        case 3:
            fractionmultiplication(a,b,c,d)
        case 4:
            fractiondivison(a,b,c,d)
        case _:
            quit()
            break