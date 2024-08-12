def main():
    b=0
    while True:
        a={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}
        try:
            b+=bill(a)
            
        except(KeyError,TypeError,ValueError):
            b+=bill(a)
            print(f"Total: ${b}")

        else:
            print(f"Total: ${b}")






def bill(y):
    return y[input("Item: ").title()]

main()
    
      
    
        





