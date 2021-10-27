import random
from math import pow
a=random.randint(2,10)

def mcd(a,b):
    if a<b:
        return mcd(b,a)
    elif a%b==0:
        return b
    else:
        return mcd(b,a%b)

def gen_key(q):
    key= random.randint(pow(10,20),q) #GENERA NÚMERO ALEATORIO ENTRE 10^20 Y q
    while mcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key

def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c
        y=(y*y)%c
        b=int(b/2)
    return x%c

#########################ENCRIPTAR###############################################
def encriptar(Mensaje,q,h,g):
    ct=[]
    k = gen_key(q) #Llave privada del usuario que escribe el mensaje
    s=power(h,k,q)
    p=power(g,k,q)
    for i in range(0,len(Mensaje)):
        ct.append(Mensaje[i])
    mensajeentrada=open("mensajeentrada.txt","w")
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
        CifradoTxt = str(ct[i])
        mensajeentrada.write(CifradoTxt + "\n")
    mensajeentrada.close()
    return ct,p

#####################DESCIFRAR################################################
def descifrar(p,key,q):

    pt=[]
    h=power(p,key,q)
    datos = []
    with open("mensajeentrada.txt") as fname:
    	lineas = fname.readlines()
    	for linea in lineas:
		    datos.append(linea.strip('\n'))

    MensajeDeSalida=open("mensajerecibido.txt", "w")
    for ix in datos:
        try:
            auxcito = int(ix)
            Escritura = chr(int(auxcito/h))
            pt.append(chr(int(auxcito/h)))
            MensajeDeSalida.write(Escritura)
        except:
            pass

    MensajeDeSalida.close()
    MensajeDescifrado=''.join(pt)
    print("El mensaje descifrado es: ", MensajeDescifrado)
    if MensajeDescifrado == Mensaje:
        print("Es seguro.")
    else:
        print("El mensaje fue alterado.")

    return pt

boton = True
aux = []
while boton:
    if len(aux) == 0:
        Mensaje=input("Ingrese el mensaje que desee codificar: ")
        q=random.randint(pow(10,20),pow(10,50)) #GENERA UN NÚMERO ALEATORIO ENTRE 10^20 Y 10^50
        g=random.randint(2,q)                   #GENERA UN NÚMERO ENTRE 2 Y q
        key = gen_key(q)                        #Llave privada del servidor
        h = power(g,key,q)                      #Llave pública
        aux.append(Mensaje)
    else:
        pass
    Opcion = input("¿Qué desea hacer?: \n a) Codificar \n b) Descifrar \n c) Ingresar un mensaje nuevo \n d) Cerrar \n")
    if Opcion == "a":
        ct, p = encriptar(Mensaje, q, h, g)
        boton = True
    elif Opcion == "b":
        try:
            pt =[]
            pt=descifrar(p,key,q)

        except:
            print("No existe mensaje encriptado.")

        boton = True
    elif Opcion == "c":
        aux = []
        boton = True
    elif Opcion == "d":
        print("Chaito uwu")
        boton = False
    else:
        print("Ingrese una opción válida.")
        boton = True