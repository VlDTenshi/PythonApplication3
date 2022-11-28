from math import *
print("Tere! Olen sinu sõber - Python")
nimi=input("Sisestage siia oma nime...")
print(f"{nimi} ,oi kui ilus nimi")
a=input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1- jah =>")
if a=="1":
    while True:
        try:
            pikkus=int(input("Pikkus: "))
            if pikkus>0 and pikkus<273: break
        except:
            pikkus=175
            print("Error")
    mass=-1
    while mass<0 or mass>400:   
        try:
            mass=int(input("Mass: "))
            if mass>0 and mass<400: break
        except:
            mass=55
            print("Error")
    try:
        indeks=mass/pikkus
        if indeks<16:
            print(f"Teie indeks on:{indeks}-Tervisele ohtlik alakaal")
        elif indeks>=16 and indeks<19:
            print("Alakaal")
        elif indeks>=19 and indeks<25:
            print("Normaalkaal")
        elif indeks>=25 and indeks<30:
            print("Ülekaal")
        elif indeks>=30 and indeks<35:
            print("Rasvumine")
        elif indeks>=35 and indeks<40:
            print("Tugev rasvumine")
        elif indeks>=40:
            print("Tervisele ohtlik rasvumine")
    except:
         print("Error")       
else:
    print("Kahju, see on väga kasulik info")
