def superReducedString(s):

    letras = []

    for letra in s:

        if len(letras) > 0 and letras[-1] == letra:
            letras.pop()
        else:
            letras.append(letra)

    resultado = "".join(letras)

    if resultado == "":
        return "Empty String"
    else:
        return resultado


s = input("Ingrese una cadena: ")

print(superReducedString(s))