
maxcripto=""
maxmonto=0.0
medcripto=""
medmonto=0.0
mincripto=""
minmonto=0.0

cripto1=input("Ingrese la primer criptomoneda: ")
monto1=float(input("Ingrese el monto de la primer criptomoneda: "))
cripto2=input("Ingrese la segunda criptomoneda: ")
monto2=float(input("Ingrese el monto de la segunda criptomoneda: "))
cripto3=input("Ingrese la tercer criptomoneda: ")
monto3=float(input("Ingrese el monto de la tercer criptomoneda: "))

if monto1>monto2  and monto1>monto3:
    maxcripto=cripto1
    maxmonto=monto1
    if monto2>monto3:    
        medcripto=cripto2
        medmonto=monto2
        mincripto=cripto3
        minmonto=monto3
    else:
        medcripto=cripto3
        medmonto=monto3
        mincripto=cripto2
        minmonto=monto2         
elif monto2>monto3 and monto2>monto1:
    maxcripto=cripto2
    maxmonto=monto2
    if monto3>monto1:
        medcripto=cripto3
        medmonto=monto3
        mincripto=cripto1
        minmonto=monto1
    else:
        medcripto=cripto1
        medmonto=monto1
        mincripto=cripto3
        minmonto=monto3
else:
    maxcripto=cripto3
    maxmonto=monto3 
    if monto2>monto1:
        medcripto=cripto2
        medmonto=monto2
        mincripto=cripto1
        minmonto=monto1
    else:
        medcripto=cripto1
        medmonto=monto1
        mincripto=cripto2
        minmonto=monto2
        
print("Estas son las criptomonedas que posee: ")
print(maxcripto+":"+str(maxmonto))
print(medcripto+":"+str(medmonto))
print(mincripto+":"+str(minmonto))
    
