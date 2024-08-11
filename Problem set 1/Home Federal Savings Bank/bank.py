x=input("Greeting:")
if x.lower().strip()[0:5]=="hello":
    print("$0")
elif x[0].lower().strip()=="h":
    print("$20")
else:
    print("$100")
