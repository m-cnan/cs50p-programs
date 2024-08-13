m=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        a=input("Date: ")
        if a[0].isalpha():
            x,y,z=a.split(" ")
            v=x.capitalize()
            if v in m and int(y)<32:
                print(z,str((m.index(v)+1)).zfill(2),y.zfill(2),sep="-")
                break
        else:
            x,y,z=a.split("/")
            if int(x)<13 and int(y)<32:
                print(z,x.zfill(2),y.zfill(2),sep="-")
                break
    except ValueError:
        pass
