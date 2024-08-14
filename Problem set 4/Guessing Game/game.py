#importing package
from random import randint

#starting an infunite loop
while True:
#Using try except for error catching   
    try:
        #using randint to return a random no in the range
        x=randint(1,int(input("Level: ")))
        y=0
        while x!=y:
            y=int(input("Guess: "))
            if x>y:
                print("Too small!")
            elif x<y:
                print("Too large!")
        print("Just right!")
        break

#incase if user inputs out of range or alpha
    except ValueError:
        pass
    