
class Zombies:
  '''
    El objeto CantidadZombies contiene la cantidad de zombies que hay en un camino entre dos ciudades 

  '''
  def __init__(self, cantidad_zombies):
    '''
      Inicializa el objeto Zombies 

      Atributes:
          cantidad_zombies (int): se utiliza para definir el peso de un arco entre dos vertices, o cuantos zombies hay en un camino entre dos ciudades
    '''
    self.cantidad_zombies = cantidad_zombies