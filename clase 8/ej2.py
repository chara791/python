diccionario={"hola":"hello","adios":"bye"}
while True:
    palabra=input("ingrese una palabra para traducir: ")
    if(palabra in diccionario):
        print("español:ingles")
        print(f"[{palabra}:{diccionario[palabra]}]")
    else:
        print("la palabra no existe en el diccionario")
        resp=input("desea regisatrarlo(si/no) salir (x): ")
        if resp=="si" or resp=="yes":
            tra=input("ingrese su tradducion: ")
            if tra !="":
                diccionario[palabra]=tra
        elif(resp=="x"):
            break
           