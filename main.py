import funzione_rimozione_vocali as v
import comuni as com
import carattere_di_controllo as C

cognome=input("Inserire il tuo cognome ")
cognome=cognome.upper()
cognome_senza_vocali=v.rimuovi_vocali(cognome)
consonanti = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
cognome_senza_consonanti = ""    
for carattere in cognome:
        if carattere not in cognome:
            cognome_senza_consonanti += carattere
if len(cognome_senza_vocali)>2:
    p=cognome_senza_vocali[0]+cognome_senza_vocali[1]+cognome_senza_vocali[2]
    tren_cifra = str(str(p)[0])
    qua_cifra = str(str(p)[1])
    cin_cifra = str(str(p)[2])
elif len(cognome_senza_vocali)==2 :
    p=cognome_senza_vocali[0]+cognome_senza_vocali[1]+cognome_senza_consonanti[0]
    tren_cifra = str(str(p)[0])
    qua_cifra = str(str(p)[1])
    cin_cifra = str(str(p)[2])
elif len(cognome_senza_vocali)==1 and len(cognome_senza_consonanti)==2:
    p=cognome_senza_vocali[0]+cognome_senza_consonanti[0]+cognome_senza_consonanti[1]
    tren_cifra = str(str(p)[0])
    qua_cifra = str(str(p)[1])
    cin_cifra = str(str(p)[2])
elif len(cognome_senza_vocali)==1 and len(cognome_senza_consonanti)==1:
    p=cognome_senza_vocali[0]+cognome_senza_consonanti[0]+"x"
    tren_cifra = str(str(p)[0])
    qua_cifra = str(str(p)[1])
    cin_cifra = str(str(p)[2])
if len(cognome_senza_consonanti)==2:
    p=cognome_senza_vocali[1]+cognome_senza_vocali[2]+"x"
    tren_cifra = str(str(p)[0])
    qua_cifra = str(str(p)[1])
    cin_cifra = str(str(p)[2])
nome=input("Inserire il tuo nome ")
nome=nome.upper()
nome_senza_vocali=v.rimuovi_vocali(nome)
consonanti = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
nome_senza_consonanti = ""    
for carattere in nome:
    if carattere not in nome:
        nome_senza_consonanti += carattere
if len(nome_senza_vocali)>3:
    s=nome_senza_vocali[0]+nome_senza_vocali[2]+nome_senza_vocali[3]
    ses_cifra = str(str(s)[0])
    set_cifra = str(str(s)[1])
    ott_cifra = str(str(s)[2])
elif len(nome_senza_vocali)==3 :
    s=nome_senza_vocali[0]+nome_senza_vocali[1]+nome_senza_vocali[2]
    ses_cifra = str(str(s)[0])
    set_cifra = str(str(s)[1])
    ott_cifra = str(str(s)[2])
elif len(nome_senza_vocali)==2:
    s=nome_senza_vocali[0]+nome_senza_vocali[2]+nome_senza_consonanti[0]
    ses_cifra = str(str(s)[0])
    set_cifra = str(str(s)[1])
    ott_cifra = str(str(s)[2])
elif len(nome_senza_vocali)==1 and len(nome_senza_consonanti)==2:
    s=nome_senza_vocali[0]+nome_senza_consonanti[0]+nome_senza_consonanti[1]
    ses_cifra = str(str(s)[0])
    set_cifra = str(str(s)[1])
    ott_cifra = str(str(s)[2])
elif len(nome_senza_vocali)==1 and len(nome_senza_consonanti)==1:
    s=nome_senza_vocali[0]+nome_senza_consonanti[0]+"x"
    ses_cifra = str(str(s)[0])
    set_cifra = str(str(s)[1])
    ott_cifra = str(str(s)[2])
if len(nome_senza_consonanti)==2:
    s=nome_senza_vocali[1]+nome_senza_vocali[2]+"x"
    ses_cifra = str(str(s)[0])
    set_cifra = str(str(s)[1])
    ott_cifra = str(str(s)[2])
anno=input("Inserire il tuo anno di nascita ")
T=anno[2]
Q=anno[3]
t=str(T+" "+Q)
mese=input("Inserire il mese di nascita ")
mese=mese.lower()
match mese:
    case "gennaio":
        q="A"
    case "febbraio":
        q="B"
    case "marzo":
        q="C"
    case "aprile":
        q="D"
    case"maggio":
        q="E"
    case "giugno":
        q="H"
    case "luglio":
        q="L"
    case "agosto":
        q="M"
    case "settembre":
        q="P"
    case "ottobre":
        q="R"
    case "novembre":
        q="S"
    case "dicembre":
        q="T"
sesso=input("Inserire il proprio sesso ")
sesso=sesso.upper()
match sesso:
    case "MASCHIO":
        giorno=input("Inserire il proprio giorno di nascita ")
        c=giorno
    case "UOMO":
        giorno=input("Inserire il proprio giorno di nascita ")
        c=giorno
    case "MASCHILE":
        giorno=input("Inserire il proprio giorno di nascita ")
        c=giorno
    case "M":
        giorno=input("Inserire il proprio giorno di nascita ")
        c=giorno
    case  "FEMMINA":
        giorno=int(input("Inserire il proprio giorno di nascita "))
        c=giorno+40
    case "DONNA":
        giorno=int(input("Inserire il proprio giorno di nascita "))
        c=giorno+40
    case "FEMMINILE":
        giorno=int(input("Inserire il proprio giorno di nascita "))
        c=giorno+40
    case "F":
        giorno=int(input("Inserire il proprio giorno di nascita "))
        c=giorno+40
prima_cifra = str(str(c)[0])
seconda_cifra = str(str(c)[1])
c= str(c)
Comune=input("Inserire il luogo di nascita ")
si=com.Cerca_comune(Comune)
tre_cifra = str(str(si)[0])
quattro_cifra = str(str(si)[1])
cinque_cifra = str(str(si)[2])
sei_cifra = str(str(si)[3])
codice=tren_cifra+" "+qua_cifra+" "+cin_cifra+" "+ses_cifra+" "+set_cifra+" "+ott_cifra+" "+t+" "+q+" "+prima_cifra+" "+seconda_cifra+" "+tre_cifra+" "+quattro_cifra+" "+cinque_cifra+" "+sei_cifra
codice=codice.split()
se=C.calcola_carattere_controllo(codice)
codice=p+s+T+Q+q+c+si+se
codice.replace(" ", "")
print("Il tuo codice fiscale è:", codice)