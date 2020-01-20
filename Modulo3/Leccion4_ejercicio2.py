import requests 
_ENDPOINT = "https://api.binance.com"

def _url(api):
    return _ENDPOINT+api
#end _url

def capturar_datos():
    cripto=""
    print("Criptomonedas validas: ","BTC,BCC,LTC,ETH,ETC,XRP")
    cripto=input("Digite la criptomoneda:  ")
    while validar(cripto):
        data =obtener_precio(cripto+"USDT").json()
        imprimir_resultado(data,cripto)
        break
    else:
        print("La moneda "+cripto+" no existe.")
    #end while    
    
#end capturar_datos 

def validar(cripto):
    criptos=["BTC","BCC","LTC","ETH","ETC","XRP"]
    return cripto in criptos  
#end validar 

def obtener_precio(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))
#end obtener_precio    

def imprimir_resultado(valor,cripto):
    print("El valor de ",cripto," es: ",valor["price"])
#end imprimir_resultado