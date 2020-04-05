
def distancia(let, let_d,pos_letd,pos_let):
    abec = "0abcdefghijklmnñopqrstuvwxyz"

    for i in range(0,len(abec)):
        if abec[i] == let:
            pos_let = i
        elif abec[i] == let_d:
            pos_letd = i

    if pos_let < pos_letd:
        dup = pos_letd - pos_let

    else:
        dup = pos_let - pos_letd

    return dup

def suma_cifra(value):
    value = str(value)
    sum = 0
    for num in value:
        num = int(num)
        sum += num
    return sum

def comprobar(cadena, iteracion):
    cont_c = iteracion
    aux = 0
    while cont_c < len(cadena):
        cont_c += 1
        aux += 1
        if aux == 5:
            break

    if aux == 5:
        return True
    else:
        return False

def suma_elem(agrupacion):
    sum = 0
    for number_ in agrupacion:
        sum += number_
    return sum

def cifrado_pal(word):
    aux = [] #Creamos una tupla auxiliar para esta duplicacion
    aux1 = []
    for i in range(0,len(word)-1): #Hacemos la multiplicacion de palabras
        if word[i+1] == '\n':
            d = distancia(word[i],word[0],0,0)
        else:
            d = distancia(word[i],word[i+1],0,0)

        for j in range(0,d):
            aux.append(word[i])
    for s__ in aux: #Ahora pasamos los parametros a ascii
        aux1.append(ord(s__))
    aux = [] #Destruimos la lista donde multiplicamos las letras de la palabra
    #Ahora hay que hacer la suma de cada cifra
    for n__ in aux1:
        aux.append(suma_cifra(n__))
    aux1 = []
    for n__ in aux: #Aplicamos el modulo de 10
        aux1.append(n__%10)
    aux = []
    cont = 0
    for z in range(0,len(aux1)):
        if z + 1 < len(aux1):
            if aux1[z] != aux1[z+1] and cont<aux1[z]:
                aux.append(aux1[z])
                cont = 0
            elif aux1[z] == aux1[z+1] and cont < aux1[z]:
                aux.append(aux1[z])
                cont += 1

            elif aux1[z] == 0:
                aux.append(0)

            elif aux1[z] != aux1[z+1] and cont == aux1[z]:
                cont = 0
        else:
            if aux1[z-1] == aux1[z] and cont<aux1[z]:
                aux.append(aux1[z])

    aux1 = []
    aux2 = [] #Guardaremos aqui la suma
    cont = 0
    c_aux = 0
    while cont < len(aux):
        if c_aux<5:
            aux1.append(aux[cont])
            c_aux += 1
            cont += 1
            if cont  == len(aux):
                suma = suma_elem(aux1)
                aux2.append(suma)
        elif c_aux == 5:
            c_aux = 0
            suma = suma_elem(aux1)
            aux1 = []
            aux2.append(suma)

    aux3=[]
    for i in range(0,len(aux2)):
        aux3.append(aux2[i]%16)

    aux3 = str(aux3)
    aux4 = "".join(aux3)
    print(aux4)










