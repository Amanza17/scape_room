import time
import os
FIRST_ANSWER = "8 1 6 1"
FIRST_CLUES = ["Busca códigos usados por informáticos", "Puedes utilizar un traductor online", "Como sigas jugando asci vas a perder tus archivos"]
SECOND_ANSWER = "COW"
SECOND_CLUES = ["Como ya hemos dicho, es un lenguaje usado por mooy poca gente", "No es el lenguaje grass, pero se alimenta de ella", "Moo moo mooooOo"]


def limpiar_terminal():
    """limpia la terminal"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

import os

def apagar_equipo():

    if os.name == 'nt':
        os.system('shutdown /s /t 1')
    else:
        os.system('shutdown -h now')


def welcome():
    """mensaje de bienvenida y recomendaciones del juego"""
    print("Bienvenido a este juego de scape room\nLe sugerimos que antes de jugar este juego se asegure de guardar y cerrar todos",
          "los documentos en los que esté trabajando.\nMuchas gracias por jugar al juego, esperamos que se lo pase bien.")
    ready = 0
    while ready != 1:
        ready = int(input("Escribe 1 cuando estés listo: "))
    print("En 5 segundos comenzará el juego, prepárese para sumergirse en esta experiencia")
    time.sleep(5)
    limpiar_terminal()

def lore():
    """da contexto al usuario sobre el scape room"""
    print("Buenas tardes Sr. presidente.\nNos enorgullece informarle que desde TechLocker, el mayor grupo de hackers hemos bloqueado su dispositivo")
    print("""   
                 ------------
                |  .------.  |
                | /        \ |
                | |        | |
               _| |________| |_
             .' |_|        |_| '.
             '._____ ____ _____.'
             |     .'____'.     |
             '.__.'.'    '.'.__.'
             '.__  TECHLOKER __.'
             |   '.'.____.'.'   |
             '.____'.____.'____.'GITHUB Amanza17
             '.________________.'\n""")

    print("Tiene usted una única oportunidad para salir de esta situación, o todos sus archivos se perderán")

    time.sleep(1)
    print("Para siempre")
    time.sleep(1)

    ready = int(input("Escribe 1 si quieres intentar desbloquear el dispositivo, escribe cualquier otra cosa si te das por vencido: "))
    if ready == 1:
        #si el jugador quiere jugar lleva a la pagina principal del juego
        print("Bienvenido a la decisión que no deberías haber tomado")
        return
    else:
        #si el jugador se rinde apaga el equipo
        #apagar_equipo()
        print("apagar equipo")
        exit(1)

def lore_primera_prueba():
    limpiar_terminal()
    print("Como usted sabrá, somos programadores, y entre nosotros, nos entendemos, tenemos nuestro propio código")
    print("76 97 32 114 101 115 112 117 101 115 116 97 32 97 32 108 97 32 115 105 103 117 105 101 110 116 101 32 99 111\n"
          " 110 116 114 97 115 101 195 177 97 32 101 115 32 101 108 32 117 108 116 105 109 111 32 110 117 109 101 114 111\n"
          " 32 100 101 32 99 97 100 97 32 117 110 97 32 100 101 32 108 97 115 32 108 101 116 114 97 115 32 100 101 108 32\n"
          " 115 105 103 117 105 101 110 116 101 32 97 99 101 114 116 105 106 111 46 32 34 67 117 97 108 32 101 115 32 108 97\n"
          " 32 115 101 103 117 110 100 97 32 117 110 105 100 97 100 32 109 97 115 32 112 101 113 117 101 195 177 97 32 100\n"
          " 101 32 108 97 32 105 110 102 111 114 109 97 116 105 99 97 44 32 113 117 101 32 115 101 32 112 117 101 100 101 32\n"
          " 100 105 118 105 100 105 114 32 101 110 32 56 32 98 108 111 113 117 101 115 32 105 110 100 105 118 105 115 105 98 108 101 115 34")
    #La respuesta a la siguiente contraseña es el último número de cada una de las letras del siguiente acertijo. "Cual es la segunda unidad mas pequeña de la informatica, que se puede dividir en 8 bloques indivisibles"
    print("Mucha suerte\n*Pista: hallar la respuesta en minúscula*\n*Pista: el formato de respuestas es 'N N N N' siendo N diferentes enteros de 1 cifra*")




def primera_prueba():
    lore_primera_prueba()
    sol = 0
    i = 0
    while sol != FIRST_ANSWER:
        sol = input("Escriba aquí la solución, o escriba pista para obtener una pista: ")
        if sol == "pista":
            if i == 3:
                print("Ya no quedan pistas")
            else:
                print(FIRST_CLUES[i])
                i+= 1
        else:
            if sol != FIRST_ANSWER:
                print("Esa no es la respuesta correcta")
    return True

def lore_segunda_prueba():
    limpiar_terminal()
    print("Parece ser que ha podido con el código ASCII, pero no se crea que todo va a ser tan fácil")
    print("Es curiosa la cantidad de lenguajes de programación que podemos llegar a utilizar los informáricos, hay moochos distintos")
    print("La siguiente prueba consistirá en decir un lenguaje de programación de lo más extraño. Tiene 3 oprtundiades\n"
          "Si alguno es el que nosotros utilizamos para hackear su sistema, perfecto, sino...")
#   el lenguaje es COW
    print("Mucha suerte\n*Pista: introduzca todo el nombre en mayúsulas*\n*Pista: es un nombre en ingles*")

def segundaa_prueba():
    lore_segunda_prueba()
    sol = 0
    i = 0
    chances = 3
    while sol != SECOND_ANSWER:
        sol = input("Escriba aquí la solución, o escriba pista para obtener una pista: ")
        if sol == "pista":
            if i == 3:
                print("Ya no quedan pistas")
            else:
                print(SECOND_CLUES[i])
                i+= 1
        else:
            if sol != FIRST_ANSWER:
                chances -= 1
                print("Esa no es la respuesta correcta\nTe quedan " , chances , "oportunidades")
                if chances == 0:
                    print("Lo sentimos mucho, diga adiós a sus archivos en")
                    print("3")
                    time.sleep(1)
                    print("2")
                    time.sleep(1)
                    print("1")
                    time.sleep(1)
                    print("0")
                    print("apagar pc")
                    #apagar_equipo()
    return True


def main():
    welcome()
    lore()
    pass_first = primera_prueba()
    if (pass_first):
        limpiar_terminal()
        print("Conseguiste pasar la primera prueba, pero no va a ser así de facil todo")


if __name__ == "__main__":
    main()