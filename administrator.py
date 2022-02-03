import podaci
import korisnik


def dodajRecepcionera():
    korisnici = podaci.citanjeKorisnika()

    username = input('Unesite korisnicko ime: ')
    lozinka = input('Unesite lozinku: ')
    telefon = input('Unesite kontakt telefon: ')
    email = input('Unesite Email adresu: ')
    ime = input('Unesite ime: ')
    prezime = input('Unesite prezime: ')
    vrsta_korisnika = "recepcioner"
    hotelID = input("Unesite sifru hotela u kom je zaposlen: ")
    aktivan = 'True'

    korisnik = {
        'username': username,
        'password': lozinka,
        'ime': ime,
        'prezime': prezime,
        'telefon': telefon,
        'email': email,
        'vrsta_korisnika': vrsta_korisnika,
        'hotelID': hotelID,
        'aktivan': aktivan
    }

    korisnici.append(korisnik)
    podaci.snimanjeKorisnika(korisnici)


def dodajHotel():
    hoteli = podaci.citanjeHotela()
    
    id_hotela = podaci.generisanjeId(hoteli, "id_hotela")
    naziv = input("Unesite naziv hotela: ")
    adresa = input("Unesite adresu hotela: ")
    lista_soba = input("Unesite listu soba sa zarezom: ")
    bazen = input("Da li ima bazen(Da/Ne): ").upper()
    while bazen not in ["DA", "NE"]:
        bazen = input("Da li ima bazen(Da/Ne): ")
    restoran = input("Da li ima restoran(Da/Ne): ").upper()
    while restoran not in ["DA", "NE"]:
        restoran = input("Da li ima restoran(Da/Ne): ")
    ocena = -1
    aktivan = 'True'

    hotel = {
        'id_hotela': id_hotela,
        'naziv': naziv,
        'adresa': adresa,
        'lista_soba': lista_soba.split(","),
        'bazen': bazen,
        'restoran': restoran,
        'ocena': ocena,
        'aktivan': aktivan
    }
    hoteli.append(hotel)
    podaci.snimanjeHotela(hoteli)


def pregledRecepcionera():
    lista_recepcionera = podaci.citanjeKorisnika()
    ispisRecepcioneraUTabeli(lista_recepcionera)


def ispisRecepcioneraUTabeli(lista_recepcionera):
    print("Korisnicko ime".ljust(15), "Ime".ljust(10), "Prezime".ljust(14), "Broj telefona".ljust(15),
          "Email".ljust(20), "Sifra hotela".ljust(13))
    print("---------------+----------+--------------+---------------+--------------------+-------------+")
    for recepcioner in lista_recepcionera:
        print(
            recepcioner["username"].ljust(15) + "|" + recepcioner["ime"].ljust(10) + "|" + recepcioner["prezime"].ljust(
                14) + "|" + recepcioner["telefon"].ljust(15) + "|" + recepcioner["email"].ljust(20) + "|" + recepcioner[
                "hotelID"].ljust(13))
    print("\n")


def pregledHotela():
    lista_hotela_brisanje = podaci.citanjeHotela()
    ispisHotelaUTabeli(lista_hotela_brisanje)


def ispisHotelaUTabeli(lista_hotela_brisanje):
    print("ID".ljust(7), "Naziv".ljust(12), "Adresa".ljust(12), "Lista soba".ljust(12), "Bazen".ljust(6),
          "Restoran".ljust(10), "Prosecna ocena".ljust(15))
    print("-------+------------+------------+------------+------+----------+---------------+")

    for hotel in lista_hotela_brisanje:
        sobe = ""
        for s in hotel["lista_soba"]:
            sobe += s + ","
        sobe = sobe[:-1]

        print(str(hotel["id_hotela"]).ljust(7) + "|" + hotel["naziv"][:12].ljust(12) + "|" + hotel["adresa"][:12].ljust(
            12) + "|" + sobe[:11].ljust(12) + "|" + str(hotel["bazen"]).ljust(6) + "|" + str(
            hotel["restoran"]).ljust(10) + "|" + str(hotel["ocena"]).ljust(4))
    print("\n")


def ispisHotelaUTabeli1(azuriranje_hotela):
    print("ID".ljust(7), "Naziv".ljust(12), "Adresa".ljust(12), "Lista soba".ljust(12), "Bazen".ljust(6),
          "Restoran".ljust(10), "Prosecna ocena".ljust(15))
    print("-------+------------+------------+------------+------+----------+---------------+")

    for hotel in azuriranje_hotela:
        sobe = ""
        for s in hotel["lista_soba"]:
            sobe += s + ","
        sobe = sobe[:-1]

        print(str(hotel["id_hotela"]).ljust(7) + "|" + hotel["naziv"][:12].ljust(12) + "|" + hotel["adresa"][:12].ljust(
            12) + "|" + sobe[:11].ljust(12) + "|" + str(hotel["bazen"]).ljust(6) + "|" + str(
            hotel["restoran"]).ljust(10) + "|" + str(hotel["ocena"]).ljust(4))
    print("\n")


def pretragaRecepcionera():
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
            print("!GRESKA! Niste uneli odgovarajucu funkciju!")


def pretragaJedanKriterjium():
    while True:
        print("1) Pretraga po imenu: ")
        print("2) Pretraga po prezimenu: ")
        print("3) Pretraga po korisnickom imenu: ")
        print("4) Pretraga po email adresi: ")
        print("5) Pretraga po hotelu u kom je zaposlen: ")
        opcija = input("Unesi zeljenu opciju: ")
        lista_korisnika = podaci.citanjeKorisnika()
        lista_recepcionera = []
        for k in lista_korisnika:
            if k["vrsta_korisnika"] == "recepcioner" and k["aktivan"] == "True":
                lista_recepcionera.append(k)
        if opcija == "1":
            kriterijum = input("Unesite rec za pretragu: ")
            recepcioneriPretraga = []
            for recepcioner in lista_recepcionera:
                if recepcioner["ime"].upper() == kriterijum.upper() and k["aktivan"] == "True":
                    recepcioneriPretraga.append(recepcioner)
            if len(recepcioneriPretraga) == 0:
                print("Ne postoji recepcioner sa datim kriterijumom")
            else:
                ispisRecepcioneraUTabeli(recepcioneriPretraga)
                break
        elif opcija == "2":
            kriterijum = input("Unesite rec za pretragu: ")
            recepcioneriPretraga = []
            for recepcioner in lista_recepcionera:
                if recepcioner["prezime"].upper() == kriterijum.upper() and k["aktivan"] == "True":
                    recepcioneriPretraga.append(recepcioner)
            if len(recepcioneriPretraga) == 0:
                print("Ne postoji recepcioner sa datim kriterijumom")
            else:
                ispisRecepcioneraUTabeli(recepcioneriPretraga)
                break
        elif opcija == "3":
            kriterijum = input("Unesite rec za pretragu: ")
            recepcioneriPretraga = []
            for recepcioner in lista_recepcionera:
                if recepcioner["username"].upper() == kriterijum.upper() and k["aktivan"] == "True":
                    recepcioneriPretraga.append(recepcioner)
            if len(recepcioneriPretraga) == 0:
                print("Ne postoji recepcioner sa datim kriterijumom")
            else:
                ispisRecepcioneraUTabeli(recepcioneriPretraga)
                break
        elif opcija == "4":
            kriterijum = input("Unesite rec za pretragu: ")
            recepcioneriPretraga = []
            for recepcioner in lista_recepcionera:
                if recepcioner["email"].upper() == kriterijum.upper() and k["aktivan"] == "True":
                    recepcioneriPretraga.append(recepcioner)
            if len(recepcioneriPretraga) == 0:
                print("Ne postoji recepcioner sa datim kriterijumom")
            else:
                ispisRecepcioneraUTabeli(recepcioneriPretraga)
                break
        elif opcija == "5":
            kriterijum = input("Unesite ID hotela za pretragu: ")
            recepcioneriPretraga = []
            for recepcioner in lista_recepcionera:
                if recepcioner["hotelID"].upper() == kriterijum.upper() and k["aktivan"] == "True":
                    recepcioneriPretraga.append(recepcioner)
            if len(recepcioneriPretraga) == 0:
                print("Ne postoji recepcioner sa datim kriterijumom")
            else:
                ispisRecepcioneraUTabeli(recepcioneriPretraga)
                break
        else:
            print("!GRESKA! Niste uneli odgovarajucu funkciju.")


def pretragaViseKriterjiuma():
    lista_korisnika = podaci.citanjeKorisnika()
    lista_recepcionera = []
    for k in lista_korisnika:
        if k["vrsta_korisnika"] == "recepcioner" and k["aktivan"] == "True":
            lista_recepcionera.append(k)
    kriterijum = input("Unesite reci za pretragu odvojene zarezom: ")
    recepcioneriPretraga = []
    uneteReci = kriterijum.split(",")
    for rec in uneteReci:
        rec = rec.upper()
        for k in lista_recepcionera:
            if (k["username"].upper() == rec or k["ime"].upper() == rec or k["prezime"].upper() == rec or k[
                "email"].upper() == rec) and k["aktivan"] == "True" and not k in recepcioneriPretraga:
                recepcioneriPretraga.append(k)
    if len(recepcioneriPretraga) == 0:
        print("Ne postoji recepcioner sa datim kriterijumom!")
    else:
        ispisRecepcioneraUTabeli(recepcioneriPretraga)


def brisanjeHotela():
    lista_hotela = podaci.citanjeHotela()
    lista_hotela_brisanje = []

    for h in lista_hotela:
        if h["aktivan"] == "True":
            lista_hotela_brisanje.append(h)
    ispisHotelaUTabeli(lista_hotela_brisanje)

    sobeHotela = []
    while True:
        idHotel = input("Unesite ID hotela koji zelite da obrisete: ")
        dobarUnos = False
        for b in lista_hotela_brisanje:
            if b["id_hotela"] == idHotel:
                sobeHotela = b["lista_soba"]
                dobarUnos = True
        if dobarUnos:
            break
        else:
            print("Ne postoji hotel sa unetim ID-em! ")
    for h in lista_hotela:
        if h["id_hotela"] == idHotel:
            h["aktivan"] = "False"
    podaci.snimanjeHotela(lista_hotela)

    lista_korisnika = podaci.citanjeKorisnika()
    for k in lista_korisnika:
        if k["vrsta_korisnika"] == "recepcioner":
            if k["hotelID"] == idHotel:
                k["aktivan"] = "False"
    podaci.snimanjeKorisnika(lista_korisnika)

    lista_sobe = podaci.citanjeSoba()
    for soba in lista_sobe:
        if soba["broj_sobe"] in sobeHotela:
            soba["aktivan"] = "False"
    podaci.snimanjeSoba(lista_sobe)

    lista_rezervacija = podaci.citanjeRezervacije()
    for rez in lista_rezervacija:
        for brojSobe in sobeHotela:
            if brojSobe in rez["rez_sobe"]:
                rez["aktivan"] = "False"
    podaci.snimanjeRezervacije(lista_rezervacija)


def brisanjeRecepcionera():
    lista_korisnika = podaci.citanjeKorisnika()
    lista_recepcionera = []
    for k in lista_korisnika:
        if k["vrsta_korisnika"] == "recepcioner" and k["aktivan"] == "True":
            lista_recepcionera.append(k)
    ispisRecepcioneraUTabeli(lista_recepcionera)

    while True:
        korIme = input("Unesite korisnicko ime recepcionera za brsanje: ")
        dobarUnos = False
        for r in lista_recepcionera:
            if r["username"] == korIme:
                dobarUnos = True
        if dobarUnos:
            break
        else:
            print("Ne postoji recepcioner sa tim korisnickim imenom! ")
    for k in lista_korisnika:
        if k["username"] == korIme:
            k["aktivan"] = "False"
    podaci.snimanjeKorisnika(lista_korisnika)


def dodajSobu():
    sobe = podaci.citanjeSoba()
    hoteli = podaci.citanjeHotela()
    azuriranje_hotela = []
    for h in hoteli:
        if h["aktivan"] == "True":
            azuriranje_hotela.append(h)
    ispisHotelaUTabeli1(azuriranje_hotela)

    while True:
        idHotel = input("Unesite ID hotela u koji zelite da dodate sobu: ")
        dobarUnos = False
        for b in azuriranje_hotela:
            if b["id_hotela"] == idHotel:
                dobarUnos = True
        if dobarUnos:
            break
        else:
            print("Ne postoji hotel sa unetim ID-em! ")
    lista_soba = podaci.citanjeSoba()
    id_sobe = podaci.generisanjeId(lista_soba, "id_sobe")
    broj_sobe = input("Unesite broj sobe: ")
    broj_kreveta = input("Unesite broj kreveta: ")
    tip_sobe = input("Unesite tip sobe (jedna soba/apartman): ")
    klima = input("Unesite da li ima klimu: ").upper()
    while klima not in ["DA", "NE"]:
        klima = input("Unesite da li ima klimu: ")
    tv = input("Unesite da li ima TV: ").upper()
    while tv not in ["DA", "NE"]:
        tv = input("Unesite da li ima TV: ")
    cena = input("Unesite cenu sobe: ")
    aktivan = "True"
    soba = {
        'id_sobe': id_sobe,
        'broj_sobe': broj_sobe,
        'broj_kreveta': broj_kreveta,
        'tip_sobe': tip_sobe,
        'klima': klima,
        'tv': tv,
        'cena': cena,
        'aktivan': aktivan,
    }
    sobe.append(soba)
    podaci.snimanjeSoba(sobe)

    for h in hoteli:
        if h["id_hotela"] == idHotel:
            h["lista_soba"].append(broj_sobe)
    podaci.snimanjeHotela(hoteli)


def dodajBazen():
    hoteli = podaci.citanjeHotela()
    azuriranje_hotela = []
    for h in hoteli:
        if h["aktivan"] == "True":
            azuriranje_hotela.append(h)
    ispisHotelaUTabeli1(azuriranje_hotela)

    while True:
        idHotel = input("Unesite ID hotela gde zelite promeniti stanje za bazen: ")
        dobarUnos = False
        for b in azuriranje_hotela:
            if b["id_hotela"] == idHotel:
                dobarUnos = True
        if dobarUnos:
            break
        else:
            print("Ne postoji hotel sa unetim ID-em! ")
    for h in hoteli:
        if h["id_hotela"] == idHotel:
            h["bazen"] = input("Unesite trenutno stanje za bazen: ")
    podaci.snimanjeHotela(hoteli)


def dodajRestoran():
    hoteli = podaci.citanjeHotela()
    azuriranje_hotela = []
    for h in hoteli:
        if h["aktivan"] == "True":
            azuriranje_hotela.append(h)
    ispisHotelaUTabeli1(azuriranje_hotela)

    while True:
        idHotel = input("Unesite ID hotela gde zelite promeniti stanje za restoran: ")
        dobarUnos = False
        for b in azuriranje_hotela:
            if b["id_hotela"] == idHotel:
                dobarUnos = True
        if dobarUnos:
            break
        else:
            print("Ne postoji hotel sa unetim ID-em! ")
    for h in hoteli:
        if h["id_hotela"] == idHotel:
            h["restoran"] = input("Unesite trenutno stanje za restoran: ")
    podaci.snimanjeHotela(hoteli)

def azuriranjeHotela():
    while True:
        print("1) Dodajte sobu: ")
        print("2) Dodajte bazen: ")
        print("3) Dodajte restoran: ")

        unos = input("Odaberite opciju za azuriranje hotela: ")
        if unos == '1':
            dodajSobu()
            break
        elif unos == '2':
            dodajBazen()
            break
        elif unos == '3':
            dodajRestoran()
            break
        else:
            print("!GRESKA! Niste uneli odgovarajucu funkciju. ")


def meniZaAdministratora():
    while True:
        print("Administrator ima sledece mogucnosti:")
        print("1) Dodaj novi hotel:")
        print("2) Dodaj novog recepcionera:")
        print("3) Azuriranje hotela:")
        print("4) Pretraga recepcionera:")
        print("5) Brisanje hotela:")
        print("6) Brisanje recepcionera:")
        print("7) Odjavi se:")
        print("8) Izadjite iz aplikacije!")

        opcija = input("Unesi zeljenu opciju: ")
        if opcija == '1':
            dodajHotel()

        elif opcija == '2':
            print("Dodajte novog recepcionera!")
            dodajRecepcionera()

        elif opcija == '3':
            print("Azuriranje hotela: ")
            azuriranjeHotela()

        elif opcija == '4':
            print("Pretraga recepcionera: ")
            pretragaRecepcionera()

        elif opcija == '5':
            print("Brisanje hotela: ")
            brisanjeHotela()

        elif opcija == '6':
            print("Brisanje recepcionera: ")
            brisanjeRecepcionera()

        elif opcija == '7':
            print("Odjavili ste se!")
            break

        elif opcija == '8':
            print("Hvala na poseti! Dovidjenja!")
            exit()
        else:
            print("!GRESKA! Niste uneli odgovarajucu funkciju.")
