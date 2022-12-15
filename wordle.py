import random

def otsimine(ps, vs):
    run_kord = 0
    for t in ps:
        #kui täht on sõnas
        if t in vs:
            if ps[run_kord] == vs[run_kord]:
                praegused.append(t.upper())
            else:
                praegused.append(t.lower())
        else:
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







#             if ps.index(t) == vs.index(t):
#                 print(t, "on õiges kohas")
#             else:
#                 print(t, "on vales kohas")
#         else:
#             print(t, "ei sisaldunud valitud sõnas")


#             counter = Counter(ps)
#             if counter[t] > 1:
#                 while run_kord < counter[t]:
#                     if ps[run_kord] == vs[run_kord]:
#                         print("töötab!!!!")
#                         run_kord += 1

#             elif counter[t] == 1:
#                 if vs[ps.index(t)] == t:
#                     praegused.append(t.upper())