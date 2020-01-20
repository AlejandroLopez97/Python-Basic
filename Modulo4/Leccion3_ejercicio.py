from requests import request

cripto_list=[]
data=request.get("https://api.coinmarketcap.com/v2/listings/").json()
for cripto in data["data"]:
    cripto_list.append(cripto["symbol"])
#end for   
criptos=tuple(cripto_list)
cripto=input("Digite el nombre de la criptomoneda: ")

while not verificar_moneda(cripto):
    print("Criptomoneda no valida.")
    cripto=input("Digite el nombre de la criptomoneda: ")
else:
    print("Criptomoneda ",cripto," es valida porque existe en coimnmarketcap.com")
#end while   
def verificar_moneda(cripto):
    return cripto in criptos
#end verificar_moneda    

    