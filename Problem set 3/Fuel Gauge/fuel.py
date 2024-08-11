def main():

    while True:
        try:
            x,y=((input("Fraction: ")).split("/"))
            z=round(fuel(x,y)*100,2)
        except (ValueError,ZeroDivisionError):
            pass
        else:
            if z>=99:
                print("F")
            elif z<=1:
                print("E")
            else:
                print(z)
            break
def fuel(a,b):
    return (float(a)/float(b))
main()


