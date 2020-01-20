
contar=0
criptos=["BTC","BCC","LTC","ETH","ETC","XRP"]
total=0.0
print("Criptomonedas validas: ","BTC,BCC,LTC,ETH,ETC,XRP")
while (contar<3):
    cripto=input("Digite el nombre de la criptomoneda:  ")
    while (cripto in criptos):
        contar=contar+1
        monto=float(input("Digite el monto de la criptomoneda ingresada:  "))
        cot=float(input("Digite la cotizacion en dolares:  "))
        total=total+(monto*cot)
        break
    else:
        print("La moneda "+cripto+" no existe.")
    #end while    
    
#end while
print("Usted posee un acumulado de: ",str(total)," dolares americanos")
    
       
    
        
        

