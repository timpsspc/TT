#1
print("Tere, maailm")
nimi= input("Kuidas on teie nimi? ")
print("Tere, maailm! Tervitan sind", nimi)
while True:
    try:
        vanus= int(input("kui vana te olete? "))
        print("Tere, maailm! Tervitan sind", nimi,"! Sa oled", vanus, "aastat vana.")
        break
    except ValueError:
        print("palun sisesta arv")

#2
vanus = 18 #int
eesnimi = "Jaak" #str
pikkus = 16.5 #float
kas_käib_koolis = True #bool. False - teine võimalus, type() - kontrolliks 

#3
from random import *
while True:
    try:
        kommid=randint(1,100)
        print("Laual on", kommid, "kommi")
        eemalda=int(input("Mitu kommi sa tahad ära võtta? "))
        kommid=kommid-eemalda
        print("Laual on nüüd", kommid, "kommi")
        break
    except ValueError:
        print("palun sisesta arv")

#4
while True:
    try:
        import math
        umbermõõt=float(input("Sisesta puu ümbermõõt meetrites: "))
        diameter=umbermõõt/math.pi
        print("Puu läbimõõt on", round(diameter, 2), "meetrit.")
        break
    except ValueError:
        print("palun sisesta arv")

#5
while True:
    try:
        N=float(input("Sisesta maatüki pikkus: "))
        M=float(input("Sisesta maatüki laius: "))
        diagonaal=(N**2+M**2)**0.5
        print("Maatüki diagonaal on", round(diagonaal, 2), "meetrit.")
        break
    except ValueError:
        print("palun sisesta arvud")
    except ValueError:
        print("palun sisesta arvud")

#6
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = aeg / teepikkus #teepikkus/aeg

# print("Sinu kiirus oli " + str(kiirus) + " km/h")

#7
while True:
    try:
        arv1= float(input("Sisesta esimene arv: "))
        arv2= float(input("Sisesta teine arv: "))
        arv3= float(input("Sisesta kolmas arv: "))
        arv4= float(input("Sisesta neljas arv: "))
        arv5= float(input("Sisesta viies arv: "))
        summa= arv1 + arv2 + arv3 + arv4 + arv5
        keskmine=summa/5
        print("arvude summa on", summa)
        print("aritmeetiline keskmine on", keskmine)
        jagaja=int(input("millega soovid summat jagada? "))
        täisarv=summa//jagaja
        print("täisarvuline osa on", täisarv)
        jääk=summa%jagaja
        print("jääk on", jääk)
        break
    except ValueError:
        print("palun sisesta arvud")
    except ZeroDivisionError:
        print("jagaja ei tohi olla 0")

#8
print("   @..@")
print("  (----)")
print(" ( \__/ )")
print("  ^^ "" ^^ ")

#9
while True:
    try:
        a=float(input("Sisesta esimene arv: "))
        b=float(input("Sisesta teine arv: "))
        c=float(input("Sisesta kolmas arv: "))
        P=a+b+c
        print("Kolmnurga ümbermõõt on:", P)
        break
    except ValueError:
        print("palun sisesta arvud")
    except ValueError:
        print("palun sisesta arvud")

#10
while True:
    try:
        P=int(input("mitme sõbraga sa pitsat jagad? "))
        P=P+1
        hind=12.90
        jootraha=hind*0.1
        koguhind=hind+jootraha
        näo_hind=koguhind/P
        print("Igaühele tuleb maksta:", round(näo_hind, 2), "€")
        break
    except ValueError:
        print("palun sisesta täisarv")
