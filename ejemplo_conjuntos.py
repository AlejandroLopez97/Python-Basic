
valid_alpha_user="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_."

while True: 
    usuario=input("Ingrese el usuario: ")
    if (len(usuario)>4):
        a=set(valid_alpha_user)
        b=set(usuario)
        if len(b-a)>0:
            print:("Usuario no valido.")
            continue
        else:
            print("Usuario valido.")
            break
    else:
        print("Usuario no valido.")
            
            