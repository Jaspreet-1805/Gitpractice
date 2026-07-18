def input_3num():
    a=int(input("Enter first number: ",))
    b=int(input("Enter second number: ",))
    c=int(input("Enter third number: ",))
    return a,b,c
def compare():
    x,y,z=input_3num()
    if x>y and x>z:
        return x
    elif x==y:
         if x>z:
            return x
         else:
            return z            
    elif y>x and y>z:
        return y
    elif y==z:
        if y>x:
            return y
        else:
            return x
    else:
        return z

largest=compare()
print("The largest number is:",largest)