from mymodule import *

Est_list =[] 
Rus_list=[] 
Rus_list=Loe_failist("rus.txt")
Est_list=Loe_failist("est.txt")

print(Rus_list)        
print(Est_list)        

while True:
    v=int(input(f"1-Tolkimine\n2-Lisa sona\n3-Muuda sona\n4-Mnag\n\n\nSisestage kauba number:"))
    if v==1:

        vene_letters =["а", "б", "в", "г","д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
        sona=input("Sissesta sona:")
        if sona.lower()[0] in vene_letters:
            try:
                ind = Rus_list.index(sona)
                vaste = Est_list[ind]
                print(f"{sona} - {vaste} on eesti keeles")
            except ValueError:
                print("Sona ei ole leitud")


        else:
            try:
                ind = Est_list.index(sona)
                vaste = Rus_list[ind] 
                print(f"{sona} - {vaste} on vene keeles")
            except ValueError:
                print("Sona ei ole leitud")


    elif v==2:
        uussona=input("Lisa vene sona:")
        Rus_list.append(uussona)
        Kirjuta_failisse("rus.txt",uussona)
        translate=input("Tolki seda sona:")
        Est_list.append(translate)
        Kirjuta_failisse("est.txt",translate)
        print(Rus_list)        
        print(Est_list)
    elif v==3:
        muuda_sona("rus.txt","est.txt",Rus_list,Est_list)
        print(Rus_list)
        print(Est_list)
    elif v==4:
        game(Rus_list,Est_list)