
total=capturar_datos()
imprimir_resultado(total)

def imprimir_resultado(valor):
    print("Usted posee un acumulado de: ",str(valor)," dolares americanos")
#end imprimir_resultado
    
def capturar_datos():
    contar=0
    total=0.0
    print("Criptomonedas validas: ","BTC,BCC,LTC,ETH,ETC,XRP")
    while (contar<3):
        cripto=input("Digite el nombre de la criptomoneda:  ")
        while validar(cripto):
            contar=contar+1
            monto=float(input("Digite el monto de la criptomoneda ingresada:  "))
            cot=float(input("Digite la cotizacion en dolares:  "))
            total=total+(monto*cot)
            break
        else:
            print("La moneda "+cripto+" no existe.")
        #end while    
    
    #end while
    return total
#end capturar_datos 

def validar(cripto):
    criptos=["BTC","BCC","LTC","ETH","ETC","XRP"]
    return cripto in criptos
      
#end validar   
       
    
   