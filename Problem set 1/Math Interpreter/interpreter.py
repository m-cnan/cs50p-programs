x,y,z=input("Expression: ").strip().split(" ")
match y:
    case "+":
        print(round(float(x)+float(z),1))
    case "-":
        print(round(float(x)-float(z),1))
    case "*":
        print(round(float(x)*float(z),1))
    case "/":
        print(round(float(x)/float(z),1))
    case _:
        print("Retry")


