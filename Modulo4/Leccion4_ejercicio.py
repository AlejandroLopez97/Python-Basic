import requests

def validar(cripto):
    return cripto in monedas
#end validar
monedas=()
monedas_dicc={}

data=requests.get("https://api.coinmarketcap.com/v2/listings/").json()
for cripto in data["data"]:
    monedas_dicc[cripto["symbol"]]=cripto["name"]

monedas = monedas_dicc.keys()

moneda=input("Digite el nombre de la criptomoneda a validar: ")
while not validar(moneda):
        print("Criptomoneda no valida .")
        moneda=input("Digite el nombre de la criptomoneda a validar: ")
else:
    print("La criptomoneda con simbolo:,",moneda,"y nombre:",monedas_dicc.get(moneda),
          "es valida porque existe en coimnmarketcap.com")