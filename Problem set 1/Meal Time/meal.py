
def main():
        x=input("What time is it?").strip()
        if 7.00 <= convert(x) <=8.00:
                print("breakfast time")
        elif 12.00 <= convert(x) <=13.00:
                print("lunch time")
        elif 18.00 <= convert(x) <=19.00:
                print("dinner time")
        


def convert(time):
            x,y=time.split(":")
            return(float(x)+(float(y)/60))


if __name__ == "__main__":
        main()
