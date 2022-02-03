import podaci
import datetime


def pregledSoba():
    lista_soba = podaci.citanjeSoba()
    ispisSobeUTabeli(lista_soba)


def ispisSobeUTabeli(lista_soba):
    print("Broj sobe".ljust(9), "Broj kreveta".ljust(13), "Tip sobe".ljust(11), "Klima".ljust(6), "Tv".ljust(3),
          "Cena".ljust(5))
    print("---------+-------------+-----------+------+---+-----+")
    for sobe in lista_soba:
        print(
            sobe["broj_sobe"].ljust(9) + "|" + sobe["broj_kreveta"].ljust(13) + "|" + sobe["tip_sobe"].ljust(11) + "|" +
            sobe["klima"].ljust(6) + "|" + sobe["tv"].ljust(3) + "|" + sobe["cena"].ljust(5))
    print("\n")


def pregledRezervacija():
    lista_rezervacija = podaci.citanjeRezervacije()
    ispisRezervacijeUTabeli(lista_rezervacija)


def ispisRezervacijeUTabeli(lista_rezervacija):
    print("Datum kreiranja".ljust(16), "Datim prijave".ljust(14), "Datum odjave".ljust(14), "Korisnik".ljust(10),
          "Status rezervacije".ljust(19))
    print("----------------+--------------+--------------+----------+-------------------+")
    for rez in lista_rezervacija:
        print(rez["datum_vreme_rez"].ljust(16) + "|" + rez["datum_prijave"].ljust(14) + "|" + rez["datum_odjave"].ljust(14) + "|" + rez["korisnik"].ljust(10) + "|" + rez["status_rez"].ljust(19))
    print("\n")


def pretragaSoba():
    while True:
        print("1) Pretraga po jednom kriterijumu: ")
        print("2) Pretraga po vise kriterijuma: ")
        opcija = input("Unesi zeljenu opciju: ")
        if opcija == "1":
            pretragaJedanKriterjiumSobe()
            break
        elif opcija == "2":
            pretragaViseKriterjiumaSobe()
            break
        else:
            print("!GRESKA! Niste uneli odgovarajucu funkciju.")


def pretragaJedanKriterjiumSobe():
    while True:
        print("1) Pretraga po broju sobe: ")
        print("2) Pretraga po broju kreveta: ")
        print("3) Pretraga po tipu sobe(apartman/jedna soba): ")
        print("4) Da li soba ima klimu: ")
        print("5) Da li soba ima TV: ")
        print("6) Pretraga po ceni: ")
        print("7) Pretraga po dostupnosti sobe: ")
        opcija = input("Unesi zeljenu opciju: ")
        lista_soba = podaci.citanjeSoba()

        if opcija == "1":
            kriterijum = input("Unesite broj sobe za pretragu: ")
            sobePretraga = []
            for sobe in lista_soba:
                if sobe["broj_sobe"] == kriterijum and sobe["aktivan"] == 'True':
                    sobePretraga.append(sobe)
            if len(sobePretraga) == 0:
                print("Ne postoji soba sa datim kriterijumom! ")
            else:
                ispisSobeUTabeli(sobePretraga)
                break
        if opcija == "2":
            kriterijum = input("Unesite broj kreveta za pretragu: ")
            sobePretraga = []
            for sobe in lista_soba:
                if sobe["broj_kreveta"] == kriterijum and sobe["aktivan"] == 'True':
                    sobePretraga.append(sobe)
            if len(sobePretraga) == 0:
                print("Ne postoji soba sa datim kriterijumom! ")
            else:
                ispisSobeUTabeli(sobePretraga)
                break
        if opcija == "3":
            kriterijum = input("Unesite tip sobe za pretragu (apartman/jedna soba): ")
            sobePretraga = []
            for sobe in lista_soba:
                if sobe["tip_sobe"].upper() == kriterijum.upper() and sobe["aktivan"] == 'True':
                    sobePretraga.append(sobe)
            if len(sobePretraga) == 0:
                print("Ne postoji soba sa datim kriterijumom! ")
            else:
                ispisSobeUTabeli(sobePretraga)
                break
        if opcija == "4":
            kriterijum = input("Unesite da li zelite sobu sa klimom (Da/Ne): ")
            sobePretraga = []
            for sobe in lista_soba:
                if sobe["klima"].upper() == kriterijum.upper() and sobe["aktivan"] == 'True':
                    sobePretraga.append(sobe)
            if len(sobePretraga) == 0:
                print("Ne postoji soba sa datim kriterijumom! ")
            else:
                ispisSobeUTabeli(sobePretraga)
                break
        if opcija == "5":
            kriterijum = input("Unesite da li zelite sobu sa TV-om (Da/Ne): ")
            sobePretraga = []
            for sobe in lista_soba:
                if sobe["tv"].upper() == kriterijum.upper() and sobe["aktivan"] == 'True':
                    sobePretraga.append(sobe)
            if len(sobePretraga) == 0:
                print("Ne postoji soba sa datim kriterijumom! ")
            else:
                ispisSobeUTabeli(sobePretraga)
                break
        if opcija == "6":
            kriterijum = input("Unesite cenu za pretragu sobe: ")
            sobePretraga = []
            for sobe in lista_soba:
                if sobe["cena"] == kriterijum and sobe["aktivan"] == 'True':
                    sobePretraga.append(sobe)
            if len(sobePretraga) == 0:
                print("Ne postoji soba sa datim kriterijumom! ")
            else:
                ispisSobeUTabeli(sobePretraga)
                break
        if opcija == "7":
            while True:
                pocetak = input("Unesite pocetni datum za pretragu: (yyyy-mm-dd) ")
                try:
                    datetime.datetime.strptime(pocetak, "%Y-%m-%d")
                    break
                except:
                    print("Los format datuma, probajte opet")
            while True:
                kraj = input("Unesite kranji datum za pretragu: (yyyy-mm-dd) ")
                try:
                    datetime.datetime.strptime(kraj, "%Y-%m-%d")
                    break
                except:
                    print("Los format datuma, probajte opet")
            lista_soba = podaci.citanjeSoba()
            sobePretraga = []
            for soba in lista_soba:
                if dostupnaSoba(soba, pocetak, kraj) == True and soba["aktivan"] == 'True':
                    sobePretraga.append(soba)
            if len(sobePretraga) == 0:
                print("Ne postoji soba sa datim kriterijumom! ")
            else:
                ispisSobeUTabeli(sobePretraga)


def dostupnaSoba(soba, pocetak, kraj):
    lista_rezervacija = podaci.citanjeRezervacije()
    pocetakDatum = datetime.datetime.strptime(pocetak, "%Y-%m-%d")
    krajDatum = datetime.datetime.strptime(kraj, "%Y-%m-%d")
    for rezervacija in lista_rezervacija:
        if soba["broj_sobe"] in rezervacija["rez_sobe"]:
            rezervacijaDatumPocetak = datetime.datetime.strptime(rezervacija["datum_prijave"], "%Y-%m-%d")
            rezervacijaDatumKraj = datetime.datetime.strptime(rezervacija["datum_odjave"], "%Y-%m-%d")
            if krajDatum > rezervacijaDatumPocetak and rezervacijaDatumKraj > pocetakDatum:
                return False
    return True


def pretragaViseKriterjiumaSobe():
    lista_soba = podaci.citanjeSoba()
    kriterijum = input("Unesite reci za pretragu odvojene zarezom: ")
    sobePretraga = []
    uneteReci = kriterijum.split(",")
    for rec in uneteReci:
        rec = rec.upper()
        for s in lista_soba:
            if (s["broj_sobe"].upper() == rec or s["broj_kreveta"].upper() == rec or s["tip_sobe"].upper() == rec or s[
                "klima"].upper() == rec or s["tv"].upper() == rec or s["cena"].upper() == rec) and s["aktivan"] == 'True' and not s in sobePretraga:
                sobePretraga.append(s)
    if len(sobePretraga) == 0:
        print("Ne postoji soba sa datim kriterijumom: ")
    else:
        ispisSobeUTabeli(sobePretraga)


def pretragaRezervacija():
    while True:
        print("1) Pretraga po jednom kriterijumu: ")
        print("2) Pretraga po vise kriterijuma: ")
        opcija = input("Unesi zeljenu opciju: ")
        if opcija == "1":
            pretragaJedanKriterjiumRez()
            break
        elif opcija == "2":
            pretragaViseKriterjiumaRez()
            break
        else:
            print("!GRESKA! Niste uneli odgovarajucu funkciju.")


def pretragaJedanKriterjiumRez():
    while True:
        print("1) Ptretraga po datumu i vremenu kreiranja rezervacije: ")
        print("2) Ptretraga po datumu i vremenu prijave u hotel: ")
        print("3) Ptretraga po datumu i vremenu odjave iz hotela: ")
        print("4) Ptretraga po korisniku koji je kreirao rezervaciju: ")
        print("5) Ptretraga po statusu rezervacije: ")
        opcija = input("Unesi zeljenu opciju: ")
        lista_rezervacija = podaci.citanjeRezervacije()

        if opcija == "1":
            kriterijum = input("Unesite datum i vreme kreiranja rezervacije (yyyy-mm-dd hh:mm):")
            rezervacijePretraga = []
            for rez in lista_rezervacija:
                if rez["datum_vreme_rez"] == kriterijum and rez["aktivan"] == 'True':
                    rezervacijePretraga.append(rez)
            if len(rezervacijePretraga) == 0:
                print("Ne postoji rezervacija sa zadatim kriterijumom! ")
            else:
                ispisRezervacijeUTabeli(rezervacijePretraga)
                break
        if opcija == "2":
            kriterijum = input("Unesite datum i vreme prijave u hotel (yyyy-mm-dd): ")
            rezervacijePretraga = []
            for rez in lista_rezervacija:
                if rez["datum_prijave"] == kriterijum and rez["aktivan"] == 'True':
                    rezervacijePretraga.append(rez)
            if len(rezervacijePretraga) == 0:
                print("Ne postoji rezervacija sa zadatim kriterijumom! ")
            else:
                ispisRezervacijeUTabeli(rezervacijePretraga)
                break
        if opcija == "3":
            kriterijum = input("Unesite datum i vreme odjave iz hotela (yyyy-mm-dd): ")
            rezervacijePretraga = []
            for rez in lista_rezervacija:
                if rez["datum_odjave"] == kriterijum and rez["aktivan"] == 'True':
                    rezervacijePretraga.append(rez)
            if len(rezervacijePretraga) == 0:
                print("Ne postoji rezervacija sa zadatim kriterijumom! ")
            else:
                ispisRezervacijeUTabeli(rezervacijePretraga)
                break
        if opcija == "4":
            kriterijum = input("Unesite korisnika koji je kreirao rezervaciju: ")
            rezervacijePretraga = []
            for rez in lista_rezervacija:
                if rez["korisnik"] == kriterijum and rez["aktivan"] == 'True':
                    rezervacijePretraga.append(rez)
            if len(rezervacijePretraga) == 0:
                print("Ne postoji rezervacija sa zadatim kriterijumom! ")
            else:
                ispisRezervacijeUTabeli(rezervacijePretraga)
                break
        if opcija == "5":
            kriterijum = input("Unesite status rezervacije koju trazite: ")
            rezervacijePretraga = []
            for rez in lista_rezervacija:
                if rez["status_rez"] == kriterijum and rez["aktivan"] == 'True':
                    rezervacijePretraga.append(rez)
            if len(rezervacijePretraga) == 0:
                print("Ne postoji rezervacija sa zadatim kriterijumom! ")
            else:
                ispisRezervacijeUTabeli(rezervacijePretraga)
                break


def pretragaViseKriterjiumaRez():
    lista_rezervacija = podaci.citanjeRezervacije()
    kriterijum = input("Unesite reci za pretragu odvojene zarezom: ")
    rezervacijePretraga = []
    uneteReci = kriterijum.split(',')
    for rec in uneteReci:
        rec = rec.upper()
        for r in lista_rezervacija:
            if (r["datum_vreme_rez"] == rec or r["datum_prijave"] == rec or r["datum_odjave"] == rec or r[
                "korisnik"].upper() == rec or r["status_rez"].upper() == rec) and r["aktivan"] == 'True' and not r in rezervacijePretraga:
                rezervacijePretraga.append(r)
        break
    if len(rezervacijePretraga) == 0:
        print("Ne postoji rezervacija sa datim kriterijumom!")
    else:
        ispisRezervacijeUTabeli(rezervacijePretraga)


def izvestavanje():
    while True:
        print("1) Dnevni izvestaj!")
        print("2) Nedeljni izvestaj!")
        print("3) Mesecni izvestaj!")
        opcija = input("Unesi zeljenu opciju: ")
        trenutniDatum = datetime.datetime.now().strftime("%Y-%m-%d")
        lista_rezervacija = podaci.citanjeRezervacije()
        brojIzdatihSoba = 0
        za_izvestaj = []
        if opcija == '1':
            for rez in lista_rezervacija:
                if rez["datum_odjave"] == trenutniDatum:
                    brojIzdatihSoba += len(rez["rez_sobe"])
                    za_izvestaj.append(rez)
        elif opcija == '2':
            pass
        elif opcija == '3':
            pass
        else:
            print("Los unos")
        ispisRezervacijeUTabeli(za_izvestaj)
        print("Ukupno realizovanih rezervacija", len(za_izvestaj))
        print("Ukupan broj izdatih soba", brojIzdatihSoba)
        break



def meniZaRecepcionera():
    while True:
        print("Recepcioner ima sledece mogucnosti: ")
        print("1) Pretraga soba: ")
        print("2) Pretraga rezervacija: ")
        print("3) Izvestavanje: ")
        print("4) Izadjite iz aplikacije!")

        opcija = input("Unesi zeljenu opciju: ")
        if opcija == '1':
            pretragaSoba()

        elif opcija == '2':
            pretragaRezervacija()

        elif opcija == '3':
            izvestavanje()

        elif opcija == '4':
            print("Hvala na poseti! Dovidjenja!")
            exit()

        else:
            print("!GRESKA! Niste uneli odgovarajucu funkciju.")

