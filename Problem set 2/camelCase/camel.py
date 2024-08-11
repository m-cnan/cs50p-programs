x=input("camelCase: ").strip()
for y in x:
    if y.islower():
        print(y,end="")
    else:
        print(f"_{y.lower()}",end="")
print("\n")
