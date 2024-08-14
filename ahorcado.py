import random

def obtener_palabra():
    palabras = ['python', 'desarrollador', 'programacion', 'juego', 'ordenador']
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

def ahorcado():
    palabra = obtener_palabra()
    letras_adivinadas = set()
    intentos = 6

    print("Bienvenido al juego de Ahorcado!")
    print(mostrar_estado(palabra, letras_adivinadas))

    while intentos > 0:
        letra = input("Adivina una letra: ").lower()

        if letra in palabra:
            letras_adivinadas.add(letra)
            print("¡Buena adivinanza!")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Intentos restantes: {intentos}")

        estado = mostrar_estado(palabra, letras_adivinadas)
        print(estado)

        if '_' not in estado:
            print("¡Felicidades, has ganado!")
            break

    if '_' in estado:
        print(f"Lo siento, has perdido. La palabra era: {palabra}")

if __name__ == "__main__":
    ahorcado()
