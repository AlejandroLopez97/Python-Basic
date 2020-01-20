"""te proponemos como proyecto final del curso Fundamentos de Programación Python que desarrolles tu propia billetera digital de tipo Desktop con interfaz de texto, que soporte monedas registradas en coinmarketcap.com, y que permita:

    Enviar un monto en USD de alguna de las criptomonedas a un destinatario indicado (identificado por un código)
    Recibir de un enviador (identificado por un código) una cantidad de alguna criptomoneda
    Consultar el balance de cada una de las criptomonedas en USD
    Consultar el balance general del usuario en USD usando el precio de la criptomoneda provisto por las APIs de coinmarketcap.com
    Emitir un histórico de transacciones del usuario indicando fecha, moneda, cantidad y monto en USD para el momento de la transacción
    Todas las transacciones realizadas por el usuario deben ser almacenadas y mantenidas, así como las cantidades de cada una de las criptomonedas que posea

Colocar un menú de opciones con:

    Recibir cantidad:
        Solicitar moneda, cantidad a recibir, así como el código.
        Validar moneda, cantidad y código, éste debe ser diferente al propio.
        Sumar cantidad de monedas al saldo.
    Transferir monto:
        Solicitar moneda, monto y código del destinatario a enviar.
        Validar.
        Restar cantidad de monedas al saldo.
    Mostrar balance una moneda:
        Solicitar la moneda a mostrar
        Validar existencia de la moneda.
        Mostrar nombre de la moneda, cantidad y monto en USD para ese momento.
    Mostrar balance general:
        Mostrar nombre de cada moneda, cantidad y monto en USD para ese momento.
        Mostrar monto total en USD de todas las monedas.
    Mostrar histórico de transacciones:
        Mostrar todas las transacciones indicando fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
    Salir del programa

Recuerda hacer las validaciones de las monedas, de los montos, del saldo y de los códigos."""
from datetime import datetime
import requests
#Billetera digital
total=0.0
criptos=()
criptos_dic={}
data=requests.get("https://api.coinmarketcap.com/v2/listings/").json()
for cripto in data["data"]:
    criptos_dic[cripto["symbol"]]=cripto["name"]
#end for
criptos=criptos_dic.keys()

print("------MENU------","\n") 
print("Elige una de las siguientes opciones.","\n") 
print(">> 1-Recibir monto","\n") 
print(">> 2-Transferir monto","\n") 
print(">> 3-Balance a una moneda","\n") 
print(">> 4-Balance general","\n")
print(">> 5-Historico","\n")
print(">> 6-Salir","\n") 
opc=input(int(">> Opción: "))

def validar_cripto(cripto):
    return cripto in criptos
#end funcion 

def almacenar_cripto(nombre,saldo,cod,fecha):
    billetera=open("evaluacion_final.csv","w+")
    if validar_cripto(nombre):
        if nombre in billetera and cod in billetera:
            acumular_moneda(nombre,saldo,cod,fecha)
        else:    
            billetera.write=(nombre)
            billetera.write=(",")
            billetera.write=(saldo)
            billetera.write=(",")
            billetera.write=(cod)
            billetera.write=(",")
            billetera.write=(fecha)
            billetera.write=("\n")
        return True
    else:
        return False
    #end if 
    billetera.close()
#end funcion

def transferir(nombre,saldo,cod):
    print("------TRANSFERIR------")
    cripto=input("Digite el nombre de la moneda a transferir: ")
    cant=float(input("Digite la cantidad de ",cripto,": "))
    cod=input("Digite el codigo de la persona que recibe la transacción: ")
    ahora=datetime.now()
    restar_cripto(cripto,cant,cod,str(ahora))
#end
def recibir():
    print("------RECEPCION------")
    cripto=input("Digite el nombre de la moneda a recibir: ")
    cant=float(input("Digite la cantidad de ",cripto,": "))
    cod=input("Digite el codigo de la persona que envia la transaccion: ")
    ahora=datetime.now()
    if almacenar_cripto(cripto,cant,cod,str(ahora)):
        print("¡Moneda almacenada exitosamente!")
    else:
        print("")
#end
def balance_unico():
    print("------BALANCE UNICO------")
#end
def balance_general():
    print("------BALANCE GENERAL------")
#end
def historial():
    print("------HISTORIAL------")
#end
def acumular_moneda(nombre,saldo,cod,fecha):
    pass    
#end
def restar_cripto(nombre,saldo,cod,fecha):
    pass
#end
    
