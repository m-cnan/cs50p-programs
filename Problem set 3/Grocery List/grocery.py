x={}
while True:
    try:
        a=input("")
        if a not in (x):
            x[a]=1
        else:
            x[a]+=1
    except EOFError:
        y=sorted(x.keys())
        for a in y:
            print(f"{x[a]} {a.upper()}")
        break
         
        

    
        



    