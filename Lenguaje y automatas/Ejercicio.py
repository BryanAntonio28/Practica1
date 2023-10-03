#----------------------------------
#30/08/23
#----------------------------------
texto = "Son las 7 de la noche"
for letra in texto:
    if letra.isdigit() and int(letra) == 7:
        print("Es hora de irnos, son las 7")