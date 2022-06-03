#UVG - Mate Discreta 
#Proyecto 2: Sistema Criptográfico RSA
#Gabriela y Lourdes

#Funciones de apoyo
def calculoPhi(p,q):        #calcular phi
    phi = int((p-1)*(q-1))
    return phi

def mod_inv(e,phi):         #calcular d: d*e congruente 1 mod(n)
    for d in range(1,phi):
        if((e%phi)*(d%phi) % phi==1):
            return d

def llavePublica(p,q):      #calcular n
    n= p*q
    return n

def mcd(a,b):               #mcd
    a,b = abs(a),abs(b)
    if a < b:
        a,b = b,a
    while b:
        r = a%b
        a,b = b,r 
    return a 

def bloques(n):             #calcular bloques del mensaje
    bloques=0
    lim="25"
    while int(lim)<n:
        bloques+=2
        lim+="25"
    return bloques

def modpower(n,p,m):       #exponenciacion modular
    if p==0:
        return 1
    if p%2==0:
        return (modpower(n,p/2,m)**2)%m
    else:
        return (n*modpower(n,(p-1)/2,m)**2)%m

def encriptar(mensaje,e,n,bloques):     #encriptar el mensaje
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
        c = str(modpower(c1,e,n))
        while len(c) < bloques:
            c = '0'+ c
        mensajeEncriptado += c + ' '
    return mensajeEncriptado

def desencriptar(mensaje,d,n,bloques):  #desencriptar el mensaje
    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    f_bloques = mensaje.split()
    resultado = ""
    for f_bloque in f_bloques:
        r = str(modpower(int(f_bloque),d,n))
        while len(r)<bloques:
            r = "0"+r
        for i in range(int(bloques/2)):
            usar = int(r[2*i:2+2*i])
            resultado += abc[usar]
    return resultado


#Codificación de un mensaje
#Input: M, p, q, e 
def encriptación(p,q,e,mensaje):
    n = llavePublica(p,q)
    b = bloques(n)
    mensajeEnc = encriptar(mensaje,e,n,b)
    return mensajeEnc


#Decodificación de un mensaje
#Input C & (n,e)
def desencriptacion(p,q,e,mensaje):
    phi = calculoPhi(p,q)
    d = mod_inv(e,phi)
    n = llavePublica(p,q)
    b = bloques(n)
    mensajeDes = desencriptar(mensaje,d,n,b)
    return mensajeDes

enc =encriptación(53,61,17,"upload")
des = desencriptacion(43,59,13,"0667 1947 0671")

print(enc)
print(des)

