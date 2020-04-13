class Camino:
  '''
      El objeto Camino relaciona dos ciudades con el número de zombies que hay entre estas
  '''
  def __init__(self, ciudad_inicio, ciudad_fin, cantidad_zombies):
    '''
    Inicializa el objeto Camino

    Args:
          nombre_ciudad_inicio (str): nombre del vertice o ciudad de partida
          nombre_ciudad_final (str): nombre del verice o ciudad de destino
          cantidad_zombies (int): peso onúmero de zombies en el camino o arco entre los vertices ociudades
    '''      
    self.ciudad_inicio = ciudad_inicio
    self.ciudad_fin = ciudad_fin
    self.cantidad_zombies = cantidad_zombies