z=50
while z>0:
    print("Amount Due:", z)
    x=int(input("Insert Coin: "))
    if x in [25,10,5]:
        z-=x
print("Change Owed:",abs(z))


