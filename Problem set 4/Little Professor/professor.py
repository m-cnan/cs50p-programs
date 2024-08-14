# importing required libraries
import random

# main...
def main():
    
    # prompting for level and inititalising score
    a=get_level()
    scr=0
    # loop for 10 turns and prompting for digits
    for _ in range(10):
        x=generate_integer(a)
        y=generate_integer(a)
        #loop for three turns and showing answer after 3 tries
        for w in range(3):
            prompt=input(f"{x} + {y} = ")
            # checking if answer is correct or its not in the range
            if (prompt)==str(x+y):
                scr+=1
                break
            else:
                print("EEE")
                if w==2:
                    print(f"{x} + {y} = {x+y}")
    print(f"Score: {scr}")
            



# setting difficulty level
def get_level():
    # ensuring its int the range
    while True:
        try:
            x=int(input("Level[1,2,3]: "))
            if x in [1,2,3]:
                return(x)
        except ValueError:
            pass


# generates integers according to the level
def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    if level==2:
        return random.randint(10,99)
    if level==3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()