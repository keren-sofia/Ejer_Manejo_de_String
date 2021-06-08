def frase_polindroma(frase2):
  if frase2 != -1:
    return "True, sí es una frase polindroma"
  else: 
    return "False, no es una frase polindroma"

print("Escribe una frase sin espacio ni puntuaciones:")
frase = input()
frase2 = frase.rindex(frase)
frase_polindroma(frase2)
print(frase_polindroma(frase2))