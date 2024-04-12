import time
import os
FIRST_ANSWER = "8 1 6 1"
FIRST_CLUES = ["Busca códigos usados por informáticos", "Puedes utilizar un traductor online", "Como sigas jugando asci vas a perder tus archivos"]
SECOND_ANSWER = "COW"
SECOND_CLUES = ["Como ya hemos dicho, es un lenguaje usado por mooy poca gente", "No es el lenguaje grass, pero se alimenta de ella", "Moo moo mooooOo"]
CAPS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
LOWER = ["a","b","c","d","e","f","g","h","i","j","k", "l", "m", "n", "ñ", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
SPECIAL_CHARS = ["+", "-", "*", "!", "/", "?","¿","(",")", "¡"]


def limpiar_terminal():
    """limpia la terminal"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

import os

def apagar_equipo():
    print("Cuando reinicie el ordenador, busque en escritorio")
    create_loose()
    time.sleep(1)
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
             '.__ TECHLOCKER __.'
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
        apagar_equipo()
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

def secure_passwd(x):
    caps_flag = False
    low_flag = False
    num_flag = False
    special_flag = False
    length_flag = False
    array = list(x)
    for i in array:
        if i in CAPS:
            caps_flag = True
        if i in LOWER:
            low_flag = True
        if i in NUMS:
            num_flag = True
        if i in SPECIAL_CHARS:
            special_flag = True
    if len(array)>=8:
        length_flag = True
    return (caps_flag and low_flag and num_flag and special_flag and length_flag)



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

def segunda_prueba():
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
                    apagar_equipo()
    return True
def prueba_techloker():
    print("Para nosotros es muy importante que usted nos preste atención, por lo que le proponemos un reto, si recuerda usted el nombre"
          "del grupo hacker, le devolvemos sus archivos, en caso contrario, tendrá que enfrentar una útima prueba, a vida o muerte")
    name = input("Escriba el nombre del grupo: ")
    if name.lower() == "techlocker":
        print("Enhorabuena, ha conseguido desbloquear su equipo, espere unos instantes para que todo vuelva a su ser")
        return True
    return False

def ultima_prueba(y):
    lore_ultima_prueba()
    x = input("Introduzca su contraseña: ")
    if x == y:
        return True
    else:
        return False


def lore_ultima_prueba():
    limpiar_terminal()
    print("Parece ser que no se acuerda de que está usted hablando con TechLocker...")
    print("Nosotros nos depsedimos aqui, le dejamos con la última prueba, de usted depende todo")
    print("Recuerda que al principio le hicimos crear una contraseña segura no?\nPues lo mas impotante de toda contraseña es que usted la recuerde")

    print("Mucha suerte")

def psswd_get():
    print("Sr. presidente, es importante que aprenda de sus errores, así que antes de borrarle todos los datos le pedimos"
          "que cree una contraseña segura, para que aprenda. Nuestra IA averiguará si es lo suficientemente segura para una persona"
          "de su nivel.")
    sec = False
    while sec == False:
        passwd = input("Introduzca una contraseña segura: ")
        sec = secure_passwd(passwd)
    print("Menos mal que ha aprendido...")
    return passwd

def create_win():

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Define el nombre del archivo
    file_name = "LEEME_JUEGO_SCAPE_ROOOM.txt"

    # Crea la ruta completa del archivo
    file_path = os.path.join(desktop_path, file_name)

    # Crea y abre el archivo en modo de escritura
    with open(file_path, "w") as file:
        file.write("Enhorabuena, consiguió superar el reto"
                   '''
                            .,,uod8B8bou,,.
                    ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
                 ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
                 !...:!TVBBBRPFT||||||||||!!^^""'   ||||
                 !.......:!?|||||!!^^""'            ||||
                 !.........||||                     ||||
                 !.........||||  ##   GITHUB        ||||
                 !.........||||      Amanza17       ||||
                 !.........||||                     ||||
                 !.........||||      Follow         ||||
                 !.........||||                     ||||
                 `.........||||                    ,||||
                  .;.......||||               _.-!!|||||
           .,uodWBBBBb.....||||       _.-!!|||||||||!:'
        !YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
        !..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
        !....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
        !......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
        !........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
        `..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
         `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
          `........::::::::::::::::;iof688888888888888888888b.     `
           `......:::::::::;iof688888888888888888888888888888b.
            `....:::;iof688888888888888888888888888888888899fT!
             `..::!8888888888888888888888888888888899fT|!^"'
              `' !!988888888888888888888888899fT|!^"'
               `!!8888888888888888899fT|!^"'
                `!988888888899fT|!^"'
                 `!9899fT|!^"'
                  `!^"'"''')
        print("Github: https://github.com/Amanza17")

def create_loose():

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Define el nombre del archivo
    file_name = "LEEME_JUEGO_SCAPE_ROOOM.txt"

    # Crea la ruta completa del archivo
    file_path = os.path.join(desktop_path, file_name)

    # Crea y abre el archivo en modo de escritura
    with open(file_path, "w") as file:
        file.write("TUVISTE SUERTE, SOLO SE APAGÓ EL PC"
                   '''
                            .,,uod8B8bou,,.
                    ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
                 ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
                 !...:!TVBBBRPFT||||||||||!!^^""'   ||||
                 !.......:!?|||||!!^^""'            ||||
                 !.........||||                     ||||
                 !.........||||  ##   GITHUB        ||||
                 !.........||||      Amanza17       ||||
                 !.........||||                     ||||
                 !.........||||      Follow         ||||
                 !.........||||                     ||||
                 `.........||||                    ,||||
                  .;.......||||               _.-!!|||||
           .,uodWBBBBb.....||||       _.-!!|||||||||!:'
        !YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
        !..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
        !....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
        !......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
        !........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
        `..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
         `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
          `........::::::::::::::::;iof688888888888888888888b.     `
           `......:::::::::;iof688888888888888888888888888888b.
            `....:::;iof688888888888888888888888888888888899fT!
             `..::!8888888888888888888888888888888899fT|!^"'
              `' !!988888888888888888888888899fT|!^"'
               `!!8888888888888888899fT|!^"'
                `!988888888899fT|!^"'
                 `!9899fT|!^"'
                  `!^"'"''')
        print("Github: https://github.com/Amanza17")



def main():
    welcome()
    lore()
    passwd = psswd_get()

    pass_first = primera_prueba()

    if (pass_first):
        limpiar_terminal()
        print("Conseguiste pasar la primera prueba, pero no va a ser así de facil todo")
        pass_sec = segunda_prueba()
        if (pass_sec):
            limpiar_terminal()
            print("Conseguiste pasar la primera prueba, pero no va a ser así de facil todo")
            if prueba_techloker() == False:
                print("Lo sentimos mucho, pero se equivocó en el nombre, prepárese")
                win = ultima_prueba(passwd)
                if (win):
                    print("Enhorabuena, consiguió desbloquear los archivos")
                else:
                    print("Despídase de sus archivos para siempre")
                    apagar_equipo()
    create_win()
    print("muchas gracias por jugar, tienes un regalito en escritorio")




if __name__ == "__main__":
    main()