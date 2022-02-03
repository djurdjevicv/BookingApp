import podaci
import korisnik
import recepcioner
import administrator


def registracija():
    print('REGISTRACIJA!')
    korisnici = podaci.citanjeKorisnika()

    username = input('Unesite korisnicko ime: ')
    lozinka = input('Unesite lozinku: ')
    telefon = input('Unesite kontakt telefon: ')
    email = input('Unesite Email adresu: ')
    ime = input('Unesite ime: ')
    prezime = input('Unesite prezime: ')
    vrsta_korisnika = "korisnik"
    aktivan = 'True'

    korisnik = {
        'username': username,
        'password': lozinka,
        'ime': ime,
        'prezime': prezime,
        'telefon': telefon,
        'email': email,
        'aktivan': aktivan,
        'vrsta_korisnika': vrsta_korisnika,
        'rezervacije' : []
    }
    korisnici.append(korisnik)
    podaci.snimanjeKorisnika(korisnici)

    print("Uspesno ste se registrovali!")

def login():
    print('**** Ovo je login ****')
    while True:
        username = input("Unesite vas username: ")
        password = input("Unesite password: ")
        korisnici = podaci.citanjeKorisnika()
        for k in korisnici:
            if k["username"] == username and k["password"] == password and k["aktivan"] == 'True':
                return k
                
        print("Korisnik ne postoji ili se ne poklapa sifra!\n")


def uvod():
    print("**** Vodic kroz meni! ****")
    print("1) Prijavi se!")
    print("2) Registruj se!")
    print("3) Izadji!")


def main():
    while True:
        uvod()
        unos = input('Unesite odgovarajuci broj: ')        
        if unos == '1':
            ulogovani_korisnik = login()
            if ulogovani_korisnik['vrsta_korisnika'] == "korisnik":
                print("Ulogovani ste kao korisinik!")
                korisnik.meniZaKorisnika(ulogovani_korisnik)
            elif ulogovani_korisnik['vrsta_korisnika'] == "recepcioner":
                print("Ulogovani ste kao recepcioner!")
                recepcioner.meniZaRecepcionera()
            elif ulogovani_korisnik['vrsta_korisnika'] == "administrator":
                print("Ulogovani ste kao administrator!")
                administrator.meniZaAdministratora()
        elif unos == '2':
            registracija()
        elif unos == '3':
            print('Hvala na poseti! Dovidjenja!')
            break
        else:
            print('!GRESKA! Niste uneli odgovarajucu funkciju.')
main()