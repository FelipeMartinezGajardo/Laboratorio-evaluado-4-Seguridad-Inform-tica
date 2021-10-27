import random

def primo(Numero):
    for n in range(2, Numero):
        if Numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

################FUNCIÓN PARA GENERAR LLAVE PRIVADA############################
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('El módulo inverso no existe.')
    else:
        return x % m
##############################################################################

aux = []
botoncito = True
while botoncito:
    try:
        if len(aux) == 0:
            p = int(input("Escriba un número primo para P: "))
            validacionP = primo(p)
            if validacionP is True:
                aux.append(p)
            else:
                None
            print(aux)

        elif len(aux) == 1:
            q = int(input("Escriba un número primo para Q: "))
            validacionQ = primo(q)
            if validacionQ is True:
                aux.append(q)
            else:
                None
        else:
            n = p*q #Público
            FiDe_n = (p-1)*(q-1)
            e = random.randint(2, FiDe_n - 1) #Público
            Validar = mcd(e, FiDe_n)
            if Validar == 1:
                d = modinv(e, FiDe_n) #Privado
                botoncito = False
            else:
                botoncito = True
    except:
        print("Ingrese número válido.")
    
boton = True

aux2 = []
while boton:
    if len(aux2) == 0:
        try:
            NumeroCodificar = int(input("¿Qué número quiere modificar?: "))
            aux2.append(NumeroCodificar)
        except:
            print("Ingrese un número válido.")
    else:
        pass
    Opcion = input("¿Qué desea hacer? \n a) Cifrar \n b) Descifrar \n c) Cambiar mensaje \n d) Cerrar \n")

    if Opcion == "a":
        Cifrado = (NumeroCodificar**e)%n
        mensajeentrada=open("mensajeentrada.txt","w")
        CifradoTxt = str(Cifrado)
        mensajeentrada.write(CifradoTxt)
        mensajeentrada.close()
        aux2.append(Cifrado)
        boton = True

    elif Opcion == "b":
        texto = open('mensajeentrada.txt', 'r')
        TextoCifrado = texto.readline()
        print("------DESCIFRANDO NÚMERO-----")
        TextoCifradoInt = int(TextoCifrado)
        Descifrado = (TextoCifradoInt**d)%n
        DescifradoStr = str(Descifrado)
        MensajeDeSalida=open("mensajerecibido.txt", "w")
        MensajeDeSalida.write(DescifradoStr)
        MensajeDeSalida.close()
        if Descifrado == NumeroCodificar:
            print("Es seguro")
        else:
            print("El mensaje fue alterado")
            boton = True

    elif Opcion == "c":
        aux2 = []
        boton = True

    elif Opcion == "d":
        print("chaito uwu")
        boton = False

    else:
        print("Ingrese una opción válida.")
        boton = True
