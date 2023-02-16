import random
(piedra, papel, tijera, lagarto, spock) = range(5)

valores = ["piedra", "papel", "tijera", "lagarto", "spock"]


reglas = {0: [["aplasta", "aplasta"],[lagarto, tijera]], 1: [["tapa", "desautoriza"],[piedra, spock]],
          2: [["corta", "decapita"],[papel, lagarto]], 3: [["envenena", "come"],[spock, papel]], 4: [["rompe", "vaporiza"],[tijera, piedra]]}
(ganausuario, ganamaquina, empate) = range(3)

def valorTexto(codigo):
  return valores[codigo]


def textoValor(texto):
  for i, valor in enumerate(valores):
    if(texto == valor):
      return i

def sacaMaquina():
  tirada = random.randint(0,5)
  return tirada;

def sacaUsuario():
  tirada = " "
  while not tirada in valores:
    tirada = input('Introduce una jugada valida piedra, papel, tijera, lagarto, spock: ')
    return textoValor(tirada);
             


def juego(usuario, maquina):
  if maquina in reglas[usuario][1]:
    return ganausuario
  elif usuario in reglas[maquina][1]:
    return ganamaquina
  else:
    return empate

def explica (ganador, perdedor):
  for i, valor in enumerate(reglas[ganador][1]):
    if (perdedor == valor): 
      print(valorTexto(ganador), reglas[ganador][0][i], valorTexto(perdedor))


usuario = sacaUsuario()
maquina = sacaMaquina()
print(valorTexto(usuario), "VS", valorTexto(maquina))

resultado = juego(usuario, maquina)
if resultado == ganausuario:
  explica(usuario, maquina)
  print("Felicidades!!!")
elif resultado == ganamaquina: 
  explica(maquina, usuario)
  print("Suerte para la proxima")
else:
  print("Estoy seguro un 50 porciento de que hiciste trampa -.-")