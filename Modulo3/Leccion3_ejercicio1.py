import random
cripto=input("Digite el nombre de la criptomoneda:  ")
monto=float(input("Digite el monto de la criptomoneda ingresada:  "))
contar=0
while (contar<7):
    porcen=random.uniform(-0.03,0.03)
    monto=monto+(monto*porcen)
    contar=contar+1
    if (porcen>0):
        print("El saldo de",cripto," del dia",contar," es de: ",str(monto)," con una ganancia positiva")
    else:
         print("El saldo de",cripto," del dia",contar," es de: ",str(monto)," con una ganancia negativa")
            
        

