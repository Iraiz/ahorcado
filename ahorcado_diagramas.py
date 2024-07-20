import random

class Ahorcado():
  def __init__(self,nombre):
      self.__nombre=nombre

  @property
  def nombre(self):
      return self.__nombre

  @nombre.setter
  def nombre(self, otro):
      self.__nombre = otro
      print(f'El nombre modificado, es: {self.nombre} ')
      return self.__nombre

  def mostrar(self):
      print(f'>>>Nombre: {self.nombre} ')


  def jugar(self):
    figuras = ['''

        +----+
        |    |
             |
             |
             |
             |
             ==========''', '''

        +----+
        |    |
        O    |
             |
             |
             |
             ==========''', '''

        +----+
        |    |
        O    |
        |    |
             |
             |
             ==========''', '''

        +----+
        |    |
        O    |
       /|    |
             |
             |
             ==========''', '''

        +----+
        |    |
        O    |
       /|\   |
             |
             |
             ==========''', '''

        +----+
        |    |
        O    |
       /|\   |
        |    |
             |
             ==========''', '''

        +----+
        |    |
        O    |
       /|\   |
        |    |
       /     |
             ==========''', '''

        +----+
        |    |
        O    |
       /|\   |
        |    |
       / \   |
             ==========''', '''

    ''']

    letra_ingresada = [] #cada letra la ingresamos a una lista
    vidas = 7
    separador = "-"
    palabra_descompuesta = [] #la palabra secreta la volvemos lista
    aumento_figura=0  #cada que no le atine cambiara la figura
    palabras=['pilares','usuario','taller','codigo','moodle','github']
    palabra = random.choice(palabras)  #alamacena una palabra diferente cada ejecucion


    print("=======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")


    print("¡Adivina la palabra secreta! de ",(len(palabra))," letras\n") #len longitud de la palabra
    print(figuras[aumento_figura]) #imprime la primera figura de la lista

    for letra in palabra:   #recorre cada letra de la palabra y en palabra_descompuesta agrega _ dependiendo la longitud de la palabra
      palabra_descompuesta.append('_ ')


    usadas = len(palabra)  #servira comom contador para salir del ciclo

    while usadas  > 0 and vidas > 0:

      print(f'Tienes {vidas} vidas y las letras que has ingresado son: {separador.join(letra_ingresada)}') #puede ser '-'.join
      print("".join(palabra_descompuesta))   #para quitar las [ ] y poner un espacio


      letra_usuario = input("Ingresa una letra:\n")


      for char in palabra:   #itera a través de cada índice de caracteres de la  palabra  si la letra que ingreso el usuario coincidio con algna de la palbra la sustutuye
          if letra_usuario == char:
            palabra_descompuesta[char] = letra_usuario.upper() + " " #sustituye el _ por la letra donde la encuentre

      if letra_usuario in letra_ingresada:  #si la letra ya la ingreso
        print("Esa letra ya se utilizó, ingresa otra letra")
      else:
        letra_ingresada.append(letra_usuario)

        if letra_usuario in palabra:  #descuenta al contador el numero de veces que la encontro
          usadas = usadas - palabra.count(letra_usuario)
          print(f'La letra {letra_usuario}, si está {palabra.count(letra_usuario)} veces en la palabra secreta')

        else:
          vidas -= 1    #descuenta a vidas y va por ptra figura a mostrar
          aumento_figura = aumento_figura + 1
          print(figuras[aumento_figura])
          print(f'La letra {letra_usuario}, no se encuentra en la palabra secreta')


    if vidas == 0:
      print(f'\nYa no te quedan más oportunidades {self.nombre} .\n¡Lastima!\nLa palabra secreta era: {palabra.upper()}')
      print(figuras[aumento_figura])
    else:
      print(f'\n¡Felicidades {self.nombre} Adivinaste la Palabra! {" ".join(palabra.upper())}')




jugador1=Ahorcado('david')
jugador1.jugar()