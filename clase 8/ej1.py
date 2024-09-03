notas = []
for x in range(3):
    while True:
        nota=float((input(f"Ingrese la nota {x+1}: ")))
        if 1 <= nota <= 5: 
            notas.append(nota)
            break
        else:
            print("ingresa una nota valida por favor ")
promedio= sum(notas) / len(notas)

estado = ""
if promedio >1.7:
    estado = "aprobado"
else:
    estado = "reprovado"

print(f"el promedio es de {promedio}. Su estado es {estado}")
