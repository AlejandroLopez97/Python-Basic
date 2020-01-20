
cripto=[]
cantidad=[]
precioUSD=[]

capturar_datos()
def capturar_datos():
    cont=0
    while cont<5:
        cripto.append=input("Digite la criptomoneda: ")
        cantidad.append=float(input("Digite la cantidad: "))
        precioUSD.append=float(input("Digite la cotizacion en dolares: "))
        cont=cont+1
    #end while
    imprimir_datos()
#end capturar_datos

def imprimir_datos():
    for i in range(0,5):
        print("Moneda ",str(cripto[i])," con una cantidad de: ",str(cantidad[i])," y una cotizacion de: ",str(precioUSD[i])," USD.")
    #end for    
#end imprimir_datos                