import inflect
p=inflect.engine()

d=[]
while True:
    try:
        d.append(input("Name:").strip().title())
    except EOFError:
        print("Adieu, adieu, to", p.join(d))
        break