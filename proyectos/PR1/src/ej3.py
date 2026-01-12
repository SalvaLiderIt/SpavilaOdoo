def contar_vocales(texto: str) -> int:
    # Contar el número de vocales en el texto dado
    vocales = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vocales)

#esto es equivalente a:

#contador = 0
#for letra in texto:  # ← Aquí se crea "letra"
#   if letra in vocales:
#       contador = contador + 1
#return contador

print(contar_vocales("Salvador"))