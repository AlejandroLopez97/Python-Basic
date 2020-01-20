
inf=int(input("Limite inferior del intervalo: "))
sup=int(input("Limite superior del intervalo: "))
print("Lo numeros primos entre ",inf,"y ",sup,"son: ")

for num in range(inf,sup+1):
    es_primo = True
    i=2
    while (es_primo and i<num):
        es_primo=(num%i)!=0
        i+=1
        if es_primo:
            print(num," Es numero primo")