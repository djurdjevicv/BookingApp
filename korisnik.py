import podaci
import datetime
from operator import itemgetter


def pregledHotela():
    lista_hotela = podaci.citanjeHotela()
    ispisHotelaUTabeli(lista_hotela)


def ispisHotelaUTabeli(lista_hotela):
    print("ID".ljust(7), "Naziv".ljust(12), "Adresa".ljust(12), "Lista soba".ljust(12), "Bazen".ljust(6),
          "Restoran".ljust(10), "Prosecna ocena".ljust(15))
    print("-------+------------+------------+------------+------+----------+---------------+")

    for hotel in lista_hotela:
        if hotel["aktivan"] == "True":
            sobe = ""
            for s in hotel["lista_soba"]:
                sobe += s + ","
            sobe = sobe[:-1]

            print(str(hotel["id_hotela"]).ljust(7) + "|" + hotel["naziv"][:12].ljust(12) + "|" + hotel["adresa"][:12].ljust(
                12) + "|" + sobe[:11].ljust(12) + "|" + str(hotel["bazen"]).ljust(6) + "|" + str(
                hotel["restoran"]).ljust(10) + "|" + str(hotel["ocena"]).ljust(4))
    print("\n")


def ispisRezervacijeUTabeli(lista_rezervacija):
    print("ID".ljust(7), "Soba".ljust(10), "Datum kreiranja".ljust(17), "Datum prijave".ljust(14),
          "Datum odjave".ljust(14), "Status rezervacije".ljust(19), "Ocena".ljust(6))
    print("-------+----------+-----------------+--------------+--------------+-------------------+------+")

    for rez in lista_rezervacija:
        sobe = ""
        for s in rez["rez_sobe"]:
            sobe += s + ","
        sobe = sobe[:-1]
        print(rez["id_rezervacije"].ljust(7) + "|" + sobe[:11].ljust(10) + "|" + rez["datum_vreme_rez"].ljust(17) + "|" +
              rez["datum_prijave"].ljust(14) + "|" + rez["datum_odjave"].ljust(14) + "|" + rez["status_rez"].ljust(
            19) + "|" + str(rez["ocena_hotela"]).ljust(6))
    print("\n")


def pretragaHotela():
    while True:
        print("1) Pretraga po jednom kriterijumu: ")
        print("2) Pretraga po vise kriterijuma: ")
        opcija = input("Unesi zeljenu opciju: ")
        if opcija == "1":
            pretragaJedanKriterjium()
            break
        elif opcija == "2":
            pretragaViseKriterjiuma()
            break
        else:
            print("!GRESKA! Niste uneli odgovarajucu funkciju.")


def pretragaJedanKriterjium():
    while True:
        print("1) Pretraga po nazivu: ")
        print("2) Pretraga po adresi: ")
        print("3) Pretraga po oceni: ")
        opcija = input("Unesi zeljenu opciju: ")
        lista_hotela = podaci.citanjeHotela()
        if opcija == "1":
            kriterijum = input("Unesite rec za pretragu: ")
            hoteliPretaga = []
            for hotel in lista_hotela:
                if hotel["naziv"].upper() == kriterijum.upper() and hotel["aktivan"] == "True":
                    hoteliPretaga.append(hotel)
            if len(hoteliPretaga) == 0:
                print("Ne postoji hotel sa datim krterijumom")
            else:
                ispisHotelaUTabeli(hoteliPretaga)
            break
        elif opcija == "2":
            kriterijum = input("Unesite rec za pretragu: ")
            hoteliPretaga = []
            for hotel in lista_hotela:
                if hotel["adresa"].upper() == kriterijum.upper() and hotel["aktivan"] == "True":
                    hoteliPretaga.append(hotel)
            if len(hoteliPretaga) == 0:
                print("Ne postoji hotel sa datim kriterijumom")
            else:
                ispisHotelaUTabeli(hoteliPretaga)
            break
        elif opcija == "3":
            kriterijum = input("Unesite broj za pretragu: ")
            hoteliPretaga = []
            for hotel in lista_hotela:
                if str(hotel["ocena"]) == kriterijum and hotel["aktivan"] == "True":
                    hoteliPretaga.append(hotel)
            if len(hoteliPretaga) == 0:
                print("Ne postoji hotel sa datim kriterijumom")
            else:
                ispisHotelaUTabeli(hoteliPretaga)
            break
        else:
            print("!GRESKA! Niste uneli odgovarajucu funkciju.")


def pretragaViseKriterjiuma():
    lista_hotela = podaci.citanjeHotela()
    kriterijum = input("Unesite reci za pretragu odvojene zarezom: ")
    hoteliPretaga = []
    uneteReci = kriterijum.split(",")
    for rec in uneteReci:
        rec = rec.upper()
        for h in lista_hotela:
            if (h["id_hotela"].upper() == rec or h["naziv"].upper() == rec or h["adresa"].upper() == rec or h[
                "bazen"].upper() == rec or h["restoran"].upper() == rec or str(h["ocena"]) == rec) and h[
                "aktivan"] == "True" and not h in hoteliPretaga:
                hoteliPretaga.append(h)
    if len(hoteliPretaga) == 0:
        print("Ne postoji hotel sa datim kriterijumima")
    else:
        ispisHotelaUTabeli(hoteliPretaga)


def najboljeOcenjivaniHoteli():
    lista_hotela = podaci.citanjeHotela()
    sortirani = sorted(lista_hotela, key=itemgetter('ocena'), reverse=True)
    bezObrisanih = []
    for hotel in sortirani:
        if hotel["aktivan"] == "True":
            bezObrisanih.append(hotel)

    ispisHotelaUTabeli(bezObrisanih[:5])


def proveriDaLiPostojiIdHotela(lista_hotela, unetId):
    for hotel in lista_hotela:
        if hotel["id_hotela"] == unetId and hotel["aktivan"] == "True":
            return True
    return False


def kreiranjeRezervacije(ulogovani_korisnik):
    lista_hotela = podaci.citanjeHotela()
    ispisHotelaUTabeli(lista_hotela)
    while True:
        odabranId = input("Unesite id hotela: ")
        if proveriDaLiPostojiIdHotela(lista_hotela, odabranId) == True:
            break
        else:
            print("Los id probajte opet")
    while True:
        pocetak = input("Unesite pocetak vase rezervacije: (yyyy-mm-dd) ")
        try:
            datetime.datetime.strptime(pocetak, "%Y-%m-%d")
            break
        except:
            print("Los format datuma, probajte opet")
    while True:
        kraj = input("Unesite kraj vase rezervacije: (yyyy-mm-dd) ")
        try:
            datetime.datetime.strptime(kraj, "%Y-%m-%d")
            break
        except:
            print("Los format datuma, probajte opet")
    lista_soba = input("Unesite listu soba sa zarezom: ")
    lista_rezervacija = podaci.citanjeRezervacije()
    id = podaci.generisanjeId(lista_rezervacija, "id_rezervacije")
    vremeKreiranja = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    nova_rezervacija = {
        "id_rezervacije": id,
        "rez_sobe": lista_soba.split(","),
        "datum_vreme_rez": vremeKreiranja,
        "datum_prijave": pocetak,
        "datum_odjave": kraj,
        "korisnik": ulogovani_korisnik["username"],
        "status_rez": "nije_zapoceta",
        "ocena_hotela": -1,
        "aktivan": "True"
    }

    lista_rezervacija.append(nova_rezervacija)
    podaci.snimanjeRezervacije(lista_rezervacija)


def pregledRezervacija(ulogovani_korisnik):
    while True:
        print("1) Pogledajte prethodne rezervacije: ")
        print("2) Pogledajte rezervacije koje nisu zapocete: ")
        print("3) Pogledajte rezervacije koje su u toku: ")
        opcija = input("Unesi zeljenu opciju: ")
        lista_rezervacija = podaci.citanjeRezervacije()

        if opcija == '1':
            odabranaRezervacija = 'zavrsena'
            rezervacijePretraga = []
            for rez in lista_rezervacija:
                if rez["status_rez"] == odabranaRezervacija and rez["korisnik"] == ulogovani_korisnik["username"] and rez["aktivan"] == "True" :
                    rezervacijePretraga.append(rez)
            if len(rezervacijePretraga) == 0:
                print("Jos uvek nemate rezervaciju sa odabranim kriterijumom! ")
            else:
                ispisRezervacijeUTabeli(rezervacijePretraga)
                break
        if opcija == '2':
            odabranaRezervacija = 'nije zapoceta'
            rezervacijePretraga = []
            for rez in lista_rezervacija:
                if rez["status_rez"] == odabranaRezervacija and rez["korisnik"] == ulogovani_korisnik["username"] and rez["aktivan"] == "True":
                    rezervacijePretraga.append(rez)
            if len(rezervacijePretraga) == 0:
                print("Jos uvek nemate rezervaciju sa odabranim kriterijumom! ")
            else:
                ispisRezervacijeUTabeli(rezervacijePretraga)
                break
        if opcija == '3':
            odabranaRezervacija = 'u toku'
            rezervacijePretraga = []
            for rez in lista_rezervacija:
                if rez["status_rez"] == odabranaRezervacija and rez["korisnik"] == ulogovani_korisnik["username"] and rez["aktivan"] == "True":
                    rezervacijePretraga.append(rez)
            if len(rezervacijePretraga) == 0:
                print("Jos uvek nemate rezervaciju sa odabranim kriterijumom! ")
            else:
                ispisRezervacijeUTabeli(rezervacijePretraga)
                break


def ocenjivanjeHotela(ulogovani_korisnik):
    lista_rezervacija = podaci.citanjeRezervacije()
    rezervacije_za_oceniti = []
    for rez in lista_rezervacija:
        if rez["status_rez"] == "zavrsena" and rez["korisnik"] == ulogovani_korisnik["username"] and rez[
            "ocena_hotela"] == -1 and rez["aktivan"] == "True":
            rezervacije_za_oceniti.append(rez)
    ispisRezervacijeUTabeli(rezervacije_za_oceniti)

    while True:
        idRez = input("Unesite ID rezervacije koji zelite da ocenite: ")
        dobarUnos = False
        for r in rezervacije_za_oceniti:
            if r["id_rezervacije"] == idRez:
                dobarUnos = True
        if dobarUnos:
            break
        else:
            print("Ne postoji rezervacija sa tim ID-em! ")

    while True:
        try:
            ocena = int(input("Unesi ocenu rezervacije: "))
            if ocena >= 1 and ocena <= 5:
                break
        except:
            print("Los unos ocene, probajte opet")

    for rez in lista_rezervacija:
        if rez["id_rezervacije"] == idRez:
            rez["ocena_hotela"] = ocena
    podaci.snimanjeRezervacije(lista_rezervacija)


def meniZaKorisnika(ulogovani_korisnik):
    while True:
        print('Registrovan korisnik ima sledece mogucnosti:')
        print('1) Pregled hotela: ')
        print('2) Pretraga hotela: ')
        print('3) Prikaz najbolje ocenjivanih hotela: ')
        print('4) Kreiranje rezervacije: ')
        print('5) Pregled rezervacija: ')
        print('6) Ocenjivanje hotela: ')
        print('7) Odjava sa sistema: ')

        opcija = input("Unesi zeljenu opciju: ")
        if opcija == '1':
            pregledHotela()

        elif opcija == '2':
            pretragaHotela()

        elif opcija == '3':
            print("Ovo je prikaz najbolje ocenjivanih hotela")
            najboljeOcenjivaniHoteli()

        elif opcija == '4':
            print("Ovo je kreiranje rezervacije")
            kreiranjeRezervacije(ulogovani_korisnik)

        elif opcija == '5':
            print("Ovo je pregled rezervacija")
            pregledRezervacija(ulogovani_korisnik)

        elif opcija == '6':
            print("Ovo je ocenjivanje hotela")
            ocenjivanjeHotela(ulogovani_korisnik)

        elif opcija == '7':
            print('Hvala na poseti! Dovidjenja!')
            break
        else:
            print("!GRESKA! Niste uneli odgovarajucu funkciju.")
