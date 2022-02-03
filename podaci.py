# KORISNIK
def napraviKorisnikaOdReda(red):
    delovi_reda = red.strip().split("|")
    username = delovi_reda[0]
    password = delovi_reda[1]
    ime = delovi_reda[2]
    prezime = delovi_reda[3]
    telefon = delovi_reda[4]
    email = delovi_reda[5]
    aktivan = delovi_reda[6]
    vrsta_korisnika = delovi_reda[7]
    korisnik = {
        'username': username,
        'password': password,
        'ime': ime,
        'prezime': prezime,
        'telefon': telefon,
        'email': email,
        'aktivan': aktivan,
        'vrsta_korisnika': vrsta_korisnika
    }
    if vrsta_korisnika == "korisnik":
        rezervacije = delovi_reda[8:]
        korisnik["rezervacije"] = rezervacije
    elif vrsta_korisnika == "recepcioner":
        hotelID = delovi_reda[8]
        korisnik["hotelID"] = hotelID

    return korisnik

def napraviRedOdKorisnika(k):
    res = k["username"] + "|" + k["password"] + "|" + k["ime"] + "|" + k["prezime"] + "|" + k["telefon"] + "|" + k[
        "email"] + "|" + k["aktivan"] + "|" + k["vrsta_korisnika"]
    if k["vrsta_korisnika"] == "recepcioner":
        res += "|" + k["hotelID"]
    elif k["vrsta_korisnika"] == "korisnik":
        if len(k["rezervacije"]) > 0:
            for r in k["rezervacije"]:
                res += "|" + r
    return res + "\n"

def citanjeKorisnika():
    f = open("korisnici.txt", "r")
    sviKorisnici = []
    for red in f.readlines():
        k = napraviKorisnikaOdReda(red)
        sviKorisnici.append(k)
    f.close()
    return sviKorisnici

def snimanjeKorisnika(korisnici):
    f = open("korisnici.txt", "w")
    for k in korisnici:
        f.write(napraviRedOdKorisnika(k))
    f.close()



# SOBE
def napraviSobuOdReda(red):
    delovi_reda = red.strip().split("|")
    id_sobe = delovi_reda[0]
    broj_sobe = delovi_reda[1]
    broj_kreveta = delovi_reda[2]
    tip_sobe = delovi_reda[3]
    klima = delovi_reda[4]
    tv = delovi_reda[5]
    cena = delovi_reda[6]
    aktivan = delovi_reda[7]
    soba = {
        'id_sobe': id_sobe,
        'broj_sobe': broj_sobe,
        'broj_kreveta': broj_kreveta,
        'tip_sobe': tip_sobe,
        'klima': klima,
        'tv': tv,
        'cena': cena,
        'aktivan': aktivan
    }
    return soba

def napraviRedOdSobe(s):
    rez = s["id_sobe"] + "|" + s["broj_sobe"] + "|" + s["broj_kreveta"] + "|" + s["tip_sobe"] + "|" + s["klima"] + "|" + \
          s["tv"] + "|" + s["cena"] + "|" + s["aktivan"]
    return rez + "\n"

def citanjeSoba():
    f = open("sobe.txt", "r")
    sveSobe = []
    for red in f.readlines():
        s = napraviSobuOdReda(red)
        sveSobe.append(s)
    f.close()
    return sveSobe

def snimanjeSoba(sobe):
    f = open("sobe.txt", "w")
    for s in sobe:
        f.write(napraviRedOdSobe(s))
    f.close()



# HOTELI
def napraviHotelOdReda(red):
    delovi_reda = red.strip().split("|")
    id_hotela = delovi_reda[0]
    naziv = delovi_reda[1]
    adresa = delovi_reda[2]
    lista_soba = delovi_reda[3]
    bazen = delovi_reda[4]
    restoran = delovi_reda[5]
    ocena = delovi_reda[6]
    aktivan = delovi_reda[7]
    hotel = {
        'id_hotela': id_hotela,
        'naziv': naziv,
        'adresa': adresa,
        'lista_soba': lista_soba.split(","),
        'bazen': bazen,
        'restoran': restoran,
        'ocena': float(ocena),
        'aktivan': aktivan
    }
    return hotel

def napraviRedOdHotela(h):
    sobe = ""
    for s in h["lista_soba"]:
        sobe += s + ","
    resenje = h["id_hotela"] + "|" + h["naziv"] + "|" + h["adresa"] + "|" + sobe[:-1] + "|" + h["bazen"] + "|" + h[
        "restoran"] + "|" + str(h["ocena"]) + "|" + h["aktivan"]
    return resenje + "\n"

def citanjeHotela():
    f = open("hoteli.txt", "r")
    sviHoteli = []
    for red in f.readlines():
        h = napraviHotelOdReda(red)
        sviHoteli.append(h)
    f.close()
    return sviHoteli

def snimanjeHotela(hoteli):
    f = open("hoteli.txt", "w")
    for h in hoteli:
        f.write(napraviRedOdHotela(h))
    f.close()



# REZERVACIJE
def napraviRezervacijuOdReda(red):
    delovi_reda = red.strip().split("|")
    id_rezervacije = delovi_reda[0]
    rez_sobe = delovi_reda[1]
    datum_vreme_rez = delovi_reda[2]
    datum_prijave = delovi_reda[3]
    datum_odjave = delovi_reda[4]
    korisnik = delovi_reda[5]
    status_rez = delovi_reda[6]
    ocena_hotela = delovi_reda[7]
    aktivan = delovi_reda[8]
    rezervacija = {
        "id_rezervacije": id_rezervacije,
        "rez_sobe": rez_sobe.split(","),
        "datum_vreme_rez": datum_vreme_rez,
        "datum_prijave": datum_prijave,
        "datum_odjave": datum_odjave,
        "korisnik": korisnik,
        "status_rez": status_rez,
        "ocena_hotela": int(ocena_hotela),
        "aktivan": aktivan
    }
    return rezervacija

def napraviRedOdRezervacije(r):
    sobe = ""
    for l in r["rez_sobe"]:
        sobe += l + ","
    rezultat = r["id_rezervacije"] + "|" + sobe[:-1] + "|" + r["datum_vreme_rez"] + "|" + r["datum_prijave"] + "|" + r[
        "datum_odjave"] + "|" + r["korisnik"] + "|" + r["status_rez"] + "|" + str(
        r["ocena_hotela"]) + "|" + r["aktivan"]
    return rezultat + "\n"

def citanjeRezervacije():
    f = open("rezervacije.txt", "r")
    sveRezervacije = []
    for red in f.readlines():
        r = napraviRezervacijuOdReda(red)
        sveRezervacije.append(r)
    f.close()
    return sveRezervacije

def snimanjeRezervacije(rezervacija):
    f = open("rezervacije.txt", "w")
    for r in rezervacija:
        f.write(napraviRedOdRezervacije(r))
    f.close()

#Jedinstven ID
def generisanjeId(lista, kljuc):
    id = []
    for element in lista:
        id.append(int(element[kljuc]))
    return str(max(id) + 1)
