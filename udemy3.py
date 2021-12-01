# Para comentar muchas lineas con ctrl + k + c
print("La suma de 2+2 es 5?")
pregunta1 = input("Respuesta:SI/NO\r\n")
resultado = 0
if pregunta1 == "NO":
    resultado += 1
else:
    resultado += 0

print("La suma de 1+1 es 2?")
pregunta2 = input("Respuesta:SI/NO\r\n")
if pregunta2 == "SI":
    resultado += 1
else:
    resultado += 0

print("La resta de 10 -2 es 8?")
pregunta3 = input("Respuesta:SI/NO\r\n")
if pregunta3 == "SI":
    resultado += 1
else:
    resultado += 0

print(f"Tu calificacion es {resultado}")
