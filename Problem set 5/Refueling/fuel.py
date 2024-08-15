def main():
    gauge(convert(input("Fraction: ")))


def convert(fraction):
    x,y=fraction.split("/")
    while True:
        try:
            a,b=int(x),int(y)
            frct=float(a/b)
            if frct<=1:
                return(round(frct*100,2))
        except (ValueError,ZeroDivisionError):
            pass


def gauge(prcnt):
    if prcnt<=1:
        print("E")
    elif prcnt>=99:
        print("F")
    else:
        print(f"{prcnt}%")


if __name__ == "__main__":
    main()

