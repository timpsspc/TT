
import math #eemaldasin * ja from
while True:
    try:
        ("Ruudu karakteristikud")
        a=float(input("Sisesta ruudu külje pikkus => ")) #eemaldasin ´´ ja lisasin "" lisasin float()
        S=a*a # võtsin
        print("Ruudu pindala", S)
        P=4*a
        print("Ruudu ümbermõõt", P)  #lisasin´´ aseml "
        di=a*math.sqrt(2)
        print("Ruudu diagonaal", round(di,2))
    except ValueError:
        print("palun sisesta arvud")

while True:
    try:
        print()
        print("Ristküliku karakteristikud") #eemaldasin )
        b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #lisasin float()
        c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #lisasin float()
        S=b*c
        print("Ristküliku pindala", S) #lisasin ""
        P=2*(b+c) # lisasin *
        print("Ristküliku ümbermõõt", P)
        di=math.sqrt(b*2+c*2)
        print("Ristküliku diagonaal", round(di)) #lisasin )
    except ValueError:
        print("palun sisesta arvud")

while True:
    try:
        print()
        print("Ringi karakteristikud")
        r=float(input("Sisesta ringi raadiusi pikkus => ")) #lisasin "" lisasin float()
        di=2*r #lisaisin *
        print("Ringi läbimõõt", di) # lisasin ,
        S=math.pi*r*2 # eemaldasin ()
        print("Ringi pindala", round(S))
        C=2*math.pi*r #lisain * ja eemaldasin ()
        print("Ringjoone pikkus", round(C)) #lisasin )
    except ValueError:
        print("palun sisesta arvud")