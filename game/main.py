import random


def juego():

  vidasdeljugador = 0
  vidasdemaquina = 0
  seleccionu = ""
  computadoras = ""
  while True:
    seleccionu, computadoras = opcion()

    if seleccionu == computadoras:

      print("Empate")
    elif seleccionu == "piedra":
      if computadoras == "papel":
        print(" Has perdido")
        vidasdemaquina += 1

      else:
        print("Has ganado")
        vidasdeljugador += 1

    elif seleccionu == "papel":
      if computadoras == "tijera":
        print("Has perdido")
        vidasdemaquina += 1

      else:
        print(" Has ganado")
        vidasdeljugador += 1

    elif seleccionu == "tijera":
      if computadoras == "piedra":
        print(" Has perdido")
        vidasdemaquina += 1
        return vidasdemaquina
      else:
        print(" Has ganado")
        vidasdeljugador += 1

    if vidasdemaquina == 3:
      print(" Has perdido la partida ")
      break

    if vidasdeljugador == 3:
      print(" Has ganado la partida ")
      break
    else:
      continue


def opcion():

  opciones = ("piedra", "papel", "tijera")

  computadoras = random.choice(opciones)
  while True:
    seleccionu = str(
      input(" Escoja entre las opciones de piedra, papel o tijera "))
    seleccionu = seleccionu.lower()
    if not seleccionu in opciones:
      print("Incorrecto no es valido")
      continue

    else:
      print(" Opcion que escogiste " + seleccionu)
      print(" Opcion de computadora " + computadoras)
      return seleccionu, computadoras


def reiniciarjuego():

  while True:
    print(" Responder: SI/NO ")
    respuesta = input(str(" Deseas reiniciar la partida? "))

    respuesta = respuesta.lower()
    if respuesta == "si":
      juego()
    elif respuesta == "no":
      exit()
    else:
      print(" Porfavor digite una opcion valida ")
      continue


juego()
reiniciarjuego()
