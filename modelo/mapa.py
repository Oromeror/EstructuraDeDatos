import os
import pickle
import numpy as np

from modelo.ciudad import Ciudad 
from modelo.zombie import Zombies
from modelo.camino import Camino
from modelo.grafo import GrafoMatrizAdyacente

class Mapa:
  '''
    Gestiona los caminos correspondientes a cada una de las ciudades o vertices
    
  '''
  def __init__(self):
    '''
      Inicializa el objeto Mapa 
      
      Atributes:
          caminos(): almacena la ejecución de cargar_caminos()
    '''  
    self.caminos = self.cargar_caminos()

  def agregar_camino(self, nombre_ciudad_inicio, nombre_ciudad_final, cantidad_zombies):
    '''
    Agrega un camino correspondiente a dos ciudades o vertices

    Args:
        nombre_ciudad_inicio (str): nombre del vertice o ciudad de partida
        nombre_ciudad_final (str): nombre del vertice o ciudad de destino
        cantidad_zombies (int): número del peso del arco entre las ciudades o de zombies en el camino entre las ciudades

    Returns:
        true, si se agregó un camino con éxito o false en caso contrario.
    '''
    ciudad_inicio = Ciudad(nombre_ciudad_inicio)
    nombre_ciudad_final = Ciudad(nombre_ciudad_final)
    cantidad_zombies = Zombies(cantidad_zombies)

    try:
      camino = Camino(ciudad_inicio, nombre_ciudad_final, cantidad_zombies)
      self.caminos['caminos'].append(camino)
    except Exception:
      return False
    return True

  def mostrar_caminos(self):
    '''
    Muestra los caminos entre ciudades o vertices

    Returns:
        caminos_texto: muestra el peso del arco que hay entre la ciudad de partida y la de destino o el número de zombies que hay en el camino que las conecta
    '''
    caminos_texto = ''
    for camino in self.caminos['caminos']:
      nombre_ciudad_inicio = camino.ciudad_inicio.nombre_ciudad
      nombre_ciudad_fin = camino.ciudad_fin.nombre_ciudad
      cantidad_zombies = camino.cantidad_zombies.cantidad_zombies
      caminos_texto += f'{nombre_ciudad_inicio} - {nombre_ciudad_fin}: {cantidad_zombies} zombies \n'
    return caminos_texto

  def cargar_caminos(self):
    '''
    Carga los arcos o caminos que hay entre los vertices o ciudades abriendo el archivo 'MiColombia.in',en el caso de que el archivo no exsita no lo carga

    '''
    if os.path.exists('MiColombia.in'):
      with open('MiColombia.in', 'rb') as current_file:
        return pickle.load(current_file)
    else:
      return {'caminos': [], 'seguras': [], 'partida': None}

  def guardar_caminos(self):
    '''
    Guarda los arcos o caminos entre ciudades o vertices en el archivo 'MiColombia.in'

    '''
    try:
      with open('MiColombia.in', 'wb') as current_file:
        pickle.dump(self.caminos, current_file)
        return True
    except:
      return False

  def eliminar_camino(self, ciudad_inicio, ciudad_fin):
    '''
    Elimina un arco o camino dentro de la lista de arcos o caminos existentes entre los vertices o ciudades que existen

      Args:
        nombre_ciudad_inicio (str) = nombre del arco o de la ciudad de partida
        nombre_ciudad_final (str) = nombre del arco o de la la ciudad de destino

      Returns:
        true: si se elimino correctamente el arco o camino entre los vertices o ciudades
    '''
    for i in range(len(self.caminos['caminos'])):
      nombre_ciudad_inicio = self.caminos['caminos'][i].ciudad_inicio.nombre_ciudad
      nombre_ciudad_fin = self.caminos['caminos'][i].ciudad_fin.nombre_ciudad
      if ciudad_inicio == nombre_ciudad_inicio and ciudad_fin == nombre_ciudad_fin:
        csi = ciudad_inicio not in self.caminos['seguras']
        csf = ciudad_fin not in self.caminos['seguras']
        cpi = ciudad_inicio != self.caminos['partida']
        cpf = ciudad_fin != self.caminos['seguras']
        if csi and csf and cpi and cpf:
          self.caminos['caminos'].pop(i)
          return True
    return False

  def obtener_nombres_ciudades(self):
    '''
    Obtiene los nombres de los vertices o ciudades existentes

      Returns:
        una lista con los bombres de los vertices o ciudades existentes
    '''
    nombre_ciudades = []
    for camino in self.caminos['caminos']:
      nombre_ciudad_inicio = camino.ciudad_inicio.nombre_ciudad
      nombre_ciudad_fin = camino.ciudad_fin.nombre_ciudad
      nombre_ciudades.append(nombre_ciudad_inicio)
      nombre_ciudades.append(nombre_ciudad_fin)
    return list(np.unique(nombre_ciudades))


  def obtener_camino_corto(self):
    '''
    Obtiene los nombres de los vertices o ciudades con menor peso y además si esta o no dentro de la zona segura la ciudad de destino, en los arcos o caminos dentro de la lista de arcos o caminos existentes 
    
      Attributes:
        ciudades ([str]): esta es la lista de nombres de las ciudades o vetices existentes
        grafo (): se instancia el objeto Grafo 

      Returns:
        el grafo basado en el algoritmo de Warshall
    '''
    ciudades = self.obtener_nombres_ciudades()
    if not self.caminos['partida']:
      return False
    grafo = GrafoMatrizAdyacente()

    # Vertices
    for ciudad in ciudades:
      grafo.insertar_vertice(ciudad)

    # Arcos
    for camino in self.caminos['caminos']:
      nombre_ciudad_inicio = camino.ciudad_inicio.nombre_ciudad
      nombre_ciudad_fin = camino.ciudad_fin.nombre_ciudad
      cantidad_zombies = camino.cantidad_zombies.cantidad_zombies
      grafo.insertar_arco(nombre_ciudad_inicio, nombre_ciudad_fin, cantidad_zombies)

    vertices = np.array(grafo.obtener_vertices())
    ciudad_inicio_indice = np.argmax([self.caminos['partida'] == vertices])

    matriz_distancias = grafo.floyd_warshall()

    valor_minimo = None
    ciudad_optima = ''
    for vertice in vertices:
      if vertice in self.caminos['seguras']:
        ciudad_fin_indice = np.argmax([vertice == vertices])
        valor = matriz_distancias[ciudad_inicio_indice][ciudad_fin_indice]
        
        if not valor_minimo or valor_minimo > valor:
          ciudad_optima = vertice
          valor_minimo = valor

    return ciudad_optima, valor_minimo

  def asignar_punto_partida(self, punto_partida):
    '''
      Asígna el vertice o ciudad de partida

        Args:
          punto_partida: este es el vertice o ciudad de partida 

        Returns:
          true si el punto_partida se encuentra dentro del listado de vertices o ciudades, retorna falso en el caso contrario
    '''
    if punto_partida in self.obtener_nombres_ciudades():
      self.caminos['partida'] = punto_partida
      return True
    return False

  def mostrar_zonas_seguras(self):
    '''
      Muestra las zonas seguras o vertices o ciudades seguras

        Atributes:
          zonas_text ([]): se almacena un listado de los vertices o ciudades seguras 

        Returns:
          true si el punto_partida se encuentra dentro del listado de vertices o ciudades, retorna falso en el caso contrario
    '''
    zonas_text = ''
    for i, segura in enumerate(self.caminos['seguras']):
      zonas_text += f'{i+1}: {segura}\n'
    return zonas_text

  def mostrar_punto_partida(self):
    return self.caminos['partida']

  def agregar_zona_segura(self, zona_segura):
    '''
    Agrega un vertice o ciudad a la zona segura (listado de ciudades seguras) si el punto de partida hace parte del listado de nombres de ciudades y además no se ecnuentra dentro de la zona segura
    
      Attributes:
        ciudades ([str]): esta es la lista de nombres de las ciudades o vetices existentes

      Returns:
        true si se agrego al vertice o ciudad a la zona segura, falso de ser lo contrario.
    '''
    ciudades = self.obtener_nombres_ciudades()
    if zona_segura in ciudades and zona_segura not in self.caminos['seguras']:
      self.caminos['seguras'].append(zona_segura)
      return True
    return False

  def eliminar_zona_segura(self, zona_segura):
    '''
    Elimina un vertice o ciudad de la zona segura si el punto de partida hace parte del listado de nombres de ciudades
    
      Attributes:
        ciudades ([str]): esta es la lista de nombres de las ciudades o vetices existentes

      Returns:
        true si se eliminó el vertice o ciudad de la zona segura, falso de ser lo contrario.
    '''
    ciudades = self.obtener_nombres_ciudades()
    if zona_segura in ciudades:
      for i, zona in enumerate(self.caminos['seguras']):
          if zona_segura == zona:
            self.caminos['seguras'].pop(i)
            return True
    return False