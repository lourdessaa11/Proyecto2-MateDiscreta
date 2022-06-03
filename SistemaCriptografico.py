#UVG - Mate Discreta 
#Proyecto 2: Sistema Criptográfico RSA


#Codificación de un mensaje
#Input: M, p, q, e 

def valores(p,q,e):
    phi = (p-1)*(q-1)
    d = pow(e,-1,phi)
    return phi, d

def llavePublica(p,q):
    n= p*q
    return n

def mcd(a,b):
    a,b = abs(a),abs(b)

    if a < b:
        a,b = b,a

    while b:
        r = a%b
        a,b = b,r 
    return a 

def bloques(n):
    bloques=0
    lim="25"
    while int(lim)<n:
        bloques+=2
        lim+="25"
    return bloques

def modpower3(n,b,m):
    if b==0:
        return 1
    if b%2==0:
        return (modpower3(n,b/2,m)**2)%m
    else:
        return (n*modpower3(n,(b-1)/2,m)**2)%m

def encriptar(mensaje,n,e,bloques):
    diccionario = { 'A':'00','B':'01','C':'02','D':'03','E':'04','F':'05','G':'06','H':'07','I':'08','J':'09','K':'10',
    'L':'11','M':'12','N':'13','O':'14','P':'15','Q':'16','R':'17','S':'18','T':'19','U':'20',
    'V':'21','W':'22','X':'23','Y':'24','Z':'25'}
    mensajeTraducido = ""
    for letra in mensaje.upper():
        mensajeTraducido += diccionario[letra]
    while not (len(mensajeTraducido)%bloques) == 0:
        mensajeTraducido += "00"
    mensajeEncriptado = ""
    for i in range(int(len(mensajeTraducido)/bloques)):
        c1 = int(mensajeTraducido[bloques*i:bloques+i*bloques])
        c = str(modpower3(c1,e,n))
        while len(c) < bloques:
            c = '0'+ c
        mensajeEncriptado += c + ' '
    return mensajeEncriptado

#Decodificación de un mensaje

def encriptación(p,q,e,mensaje):
    phi,d = valores(p,q,e)
    n = llavePublica(p,q)
    b = bloques(n)
    mensajeEnc = encriptar(mensaje,n,e,b)
    return mensajeEnc

enc =encriptación(43,59,19,"upload")

def desencriptar(mensaje,d,n,bloques):
    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    f_bloques = mensaje.split()
    resultado = ""
    for f_bloque in f_bloques:
        r = str(modpower3(int(f_bloque), d,n))
        while len(r)<bloques:
            r = "0"+r
        for i in range(int(bloques/2)):
            usar = int(r[2*i:2+2*i])
            resultado += abc[usar]
    return resultado

def desencriptacion(p,q,e,mensaje):
    phi,d = valores(p,q,e)
    n = llavePublica(p,q)
    b = bloques(n)
    mensajeDes = desencriptar(mensaje,n,e,b)
    return mensajeDes

des = desencriptacion(43,59,19,"2101 0696 0879")

print(enc)
print(des)
