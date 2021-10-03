
#  RETO 1 EL EXTRAÑO BIBLIOTECARIO

# ---------------------------------------------------------------------------------------------------------------------------
# duplicar_letras(palabra)
# POSTCONDICION: Devuelve una lista de palabras duplicadas segun la distancia que esta una palabra de otra en el abecedario. Sin embargo
#               si es la ultima letra, la tomamos como si fuese la primera, es decir, duplicamos la letra el mismo numero de veces que la primera.

def duplicar_letras(palabra):
    abecedario = "abcdefghijklmnñopqrstuvwxyz" # Abecedario
    letras_duplicadas = [] # Lista donde guardaremos las letras duplicadas

    for i in range(0,len(palabra)):
        
        if i < len(palabra) - 1:
            dist = abs(abecedario.index(palabra[i]) - abecedario.index(palabra[i + 1]))

            for j in range(0, dist):
                letras_duplicadas.append(palabra[i])
        else:
            numero_veces = letras_duplicadas.count(palabra[0]) # Tomamos la primera palabra si estamos en la ultima

            for j in range(0,numero_veces):
                letras_duplicadas.append(palabra[i])

    return letras_duplicadas

# ---------------------------------------------------------------------------------------------------------------------------
# toASCII(letras_dup)
# PRECONDICION: Los elementos sean caracteres
# POSTCONDICION: Nos devuelve una lista con los caracteres convertidos en ASCII
def toASCII(letras_dup):
    caracter_ascii = []
    for let in letras_dup:
        caracter_ascii.append(ord(let))
    
    return caracter_ascii

# ---------------------------------------------------------------------------------------------------------------------------
# suma_letras(numerosASCII)
# PRECONDICION: Los elementos de la lista sean numeros
# POSTCONDICION: Devuelve una lista con la suma de los numeros descompuestos, es decir, 112 (1 + 1 + 2) = 4

def suma_letras(numerosASCII):

    suma = []

    for i in range(0, len(numerosASCII)):
        cifras = list(map(int,str(numerosASCII[i])))
        sum = 0

        for cif in cifras:
            sum += int(cif)
        
        suma.append(sum)
        cifras = []

    return suma

# ---------------------------------------------------------------------------------------------------------------------------
# aplicarMod(numeros)
# PRECONDICION:
# POSTCONDICION: Devuelve una lista con los elementos aplicados el módulo de 10
def aplicarMod(numeros):
    aplic = []
    for num in numeros:
        aplic.append(num%10)
    
    return aplic
# ---------------------------------------------------------------------------------------------------------------------------
# reducirNum(numeros)
# PRECONDICION:
# POSTCONDICION: Nos devuelve una lista con los elementos reducidos segun el numero que sea, en el caso de 
def reducirNum(numeros):
    reduccion = []

    actual = -1
    cont = 0

    for n in numeros:
        if actual != n:
            actual = n
            cont = 1
            reduccion.append(actual)
        else:
            if cont < actual and actual != 0:
                reduccion.append(actual)
            
            cont += 1
                

    return reduccion

# ---------------------------------------------------------------------------------------------------------------------------
# agrupar_sumar(numeros)
# PRECONDICION: Los elementos han de estar agrupados de 5 en 5
# POSTCONDICION: Nos devuelve la suma de esos agrupamientos
def agrupar_sumar(numeros):
    agrup = []
    sub_agrup = []

    cont = 0 
    for num in numeros:
        if cont < 5:
            sub_agrup.append(num)
            cont += 1
        else:
            agrup.append(sub_agrup)
            sub_agrup = []
            sub_agrup.append(num)
            cont = 1

    if len(sub_agrup) < 5:
        for i in range(len(sub_agrup),5):
            sub_agrup.append(0)
        
        agrup.append(sub_agrup)

    sum_agrup = []

    for i in range(0,len(agrup)):
        sum = 0
        for j in range(0,5):
            sum += agrup[i][j]
        
        sum_agrup.append(sum)

    return sum_agrup

# ---------------------------------------------------------------------------------------------------------------------------
# resultado(agrupamientos)
# PRECONDICION: Los elementos han de estar agrupados de 
# POSTCONDICION: Nos devuelve los elementos aplicados el módulo de 16 y ya concatenados
def resultado(agrupamientos):
    moddieciseis = []

    for n in agrupamientos:
        moddieciseis.append(n%16)
    
    return "".join(str(_) for _ in moddieciseis)

# ---------------------------------------------------------------------------------------------------------------------------

def convertir_palabra(palabra):
    let = duplicar_letras(palabra)
    toAscii = toASCII(let)
    suma = suma_letras(toAscii)
    mod = aplicarMod(suma)
    red = reducirNum(mod)
    ag = agrupar_sumar(red)
    return resultado(ag)


word = input("Palabra: ")
print("Resultado: " + convertir_palabra(word))