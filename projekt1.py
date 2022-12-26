import random

def otsimine(ps, vs):
    run_kord = 0
    t_jrj = []    #järjend, kus juba läbi käidud tähed
    for t in ps:
        t_jrj.append(t)
        
        if vs.count(t) == 1:  #kui täht sõnas ühe korra
            if ps[run_kord] == vs[run_kord]:  #kui täht õiges kohas
                praegused.append(t.upper())
                t_jrj.append(t.upper())
                
            else:  #kui täht vales kohas
                if t.upper() in t_jrj:
                    praegused.append("_")
                else:
                    praegused.append(t.lower())
        
        elif vs.count(t) > 1:  #kui täht on sõnas mitu korda:
            if ps[run_kord] == vs[run_kord]:
                praegused.append(t.upper())
            else:
                praegused.append(t.lower())

        else: #kui tähte pole sõnas
            praegused.append("_")
            if t not in ei_sisalda:
                ei_sisalda.append(t)
        run_kord += 1
    print(praegused)
    del praegused[0:tähe_arv]
    print("Tähed, mida sõna ei sisalda: " + str(sorted(ei_sisalda)))
    print("Juba pakutud sõnad: " + str(pakutud_sõnad))


ei_sisalda = []
praegused = []
pakutud_sõnad = []

# Failist sõnad järjendisse
fail = open("EKI_etLex.txt", encoding="UTF-8")

sõna_järjend = []

for rida in fail:
    sõna_järjend.append(rida.lower().strip())

fail.close()


tähe_arv = int(input("Mitme tähelist sõna soovite pakkuda? "))

# valitud sõna
# kui võtta üks juhuslik N-täheline
while True:
    valitud = random.choice(sõna_järjend)
    if len(valitud) == tähe_arv:
        break

kord = 0
korrad = 6
näidatavad_korrad = 6

while kord < korrad:
    pakutud_sõna = input("Pakkuge sõna: ").lower()
    pakutud_sõnad.append(pakutud_sõna) # pakutud sõna järjendisse
    if pakutud_sõna in sõna_järjend and len(pakutud_sõna) == tähe_arv: # kontroll, kas sõna on olemas ja õige pikkusega
        if pakutud_sõna == valitud: 
            print("Õige!")
            break
        else:
            otsimine(pakutud_sõna, valitud) 
            näidatavad_korrad -= 1
            kord += 1
            if näidatavad_korrad > 0:
                print("Jäänud on veel " + str(näidatavad_korrad) + " korda")
            else:
                print("Mäng läbi! Õige sõna oli " + valitud)
    elif len(pakutud_sõna) != tähe_arv:
        print("Pakutud sõna vales pikkuses. ")
    else:
        print("ei sisaldunud sõnade hulgas")

#TÖÖTAB VALESTI NÄITEKS JUHUL:  
# Mitme tähelist sõna soovite pakkuda? 4
# kägu
# Pakkuge sõna: tulu
# ['_', 'u', '_', 'U']                     #esimene "u" peaks olema "_"
# Tähed, mida sõna ei sisalda: ['l', 't']
# Juba pakutud sõnad: ['tulu']
# Jäänud on veel 5 korda