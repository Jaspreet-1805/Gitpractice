def input_3num():
    a=int(input("Enter first number: ",))
    b=int(input("Enter second number: ",))
    c=int(input("Enter third number: ",))
    return a,b,c
def compare():
    x=input_3num({a})
    y=input_3num({b})
    z=input_3num({c})
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
largest=compare()
print("The largest number is:",largest)