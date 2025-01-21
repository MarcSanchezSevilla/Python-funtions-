
saldo = 1200
xº



def retirar(cantidad):
   global saldo 
   if saldo < cantidad: 
    print ("No hay saldo suficiente para retirar crack")
    diferencia= saldo - cantidad 
    print("Te faltan", diferencia, "€ para poder retirar ;)")
   else: 
    totalsaldoactual = saldo - cantidad 
    saldo= totalsaldoactual 
    print("Tu saldo actual es" , saldo )

def ingresar(cantidad): 
   global saldo 
   totalsaldoactual = saldo + cantidad 
   slado=totalsaldoactual
   print("Tu saldo actual es", saldo)

def login():
    #login segur amb un maxim de 3 intents 
    intento=0
    print("Bienvenido al cajero ")
    while intento <3:
        usuario =int(input ("Usuario: "))
        password = int(input ("Contraseña: "))
        if usuario == "skibidi" and password == "toilet777": 
            print ("Bienvenido")
            opcion=int(input("1. para Ingresar o 2. para Retirar"))
            if opcion==1:
                ingresar()
            elif opcion ==2: 
                cantidad= int(input("Introduce la cantidad a retirar"))
                retirar()
            else: 
                print ("Opción incorrecta ")
                
                
            break
        else: 
            print("Usuario o contraseña incorrectos")
            intento +=1
            print ("Te quedan", 3 - intento , "intentos")
            if intento ==3: 
                print ("Usuario bloqueado")
                break 
