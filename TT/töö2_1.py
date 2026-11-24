#1a
eesnimi=input("sisesta oma eesnimi: ")
if eesnimi.lower()=="juku":
    print("lähme Jukuga kinno")
    if eesnimi.isupper():
        print("ära karju, Juku!")


    vanus= input("Sisesta oma vanus: ")
    if not vanus.isdigit():
        print("palun sisesta vanus täisarvuna")
    else:
        vanus= int(vanus)
#1b
    if vanus == 0<vanus<6:
        print("pilet on tasuta")
    elif vanus<15:
        print("sull on vaja lastepiletit")
    elif vanus<66:
        print("sul on vaja täispiletit")
    elif vanus<101:
        print("sul on vaja sooduspiletit")
    elif vanus<0 or vanus>100:
        print("Viga andmetes: vanus peab olema vahemikus 0-100")
else:
    print("täna kinno ei minda")
print()
#2
pinginaabrid=["mati", "Kati", "´Juku"]