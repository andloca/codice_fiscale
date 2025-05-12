def rimuovi_vocali(parola):
    vocali = "aeiouAEIOU"
    parola_senza_vocali = ""
    for carattere in parola:
        if carattere not in vocali:
            parola_senza_vocali += carattere
    
    return parola_senza_vocali