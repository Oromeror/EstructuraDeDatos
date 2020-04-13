import numpy as np

class GrafoMatrizAdyacente:
    '''
    Gestiona la matriz adyacente del conjunto de ciudades llamadas vértices, unidas por los caminos llamados arcos y la cantidad de zombies por cada arco, llamado este último el peso del arco.
    
    '''
    def __init__(self):
      '''
      Inicializa la matriz adyacente.

      Atributes:
          vertices ([]]): lista dinámica de vertices o ciudades 
          matriz_adyacente (np.array): matriz adyacente del conjunto de vertices o ciudades
      '''
      self._vertices = []
      self._matriz_adyacente = np.array([])

    def obtener_matriz(self):
      '''
      Ontiene la matriz adyacente

      Returns:
          _matriz_adyacente: devuelve la matriz adyacente compuesta por el conjunto de vertices o ciudades  
      '''
      return self._matriz_adyacente

    def obtener_vertices(self):
      '''
      Obtiene los vertices o ciudades que hay en la matriz de adyacencia

      Returns:
          _vertices: devuelve la lista dinámica de ciudades o vertices  
      '''
      return self._vertices
    
    def cantidad_arcos(self):
      '''
      Muestra la cantidad de arcos o caminos que hay en el conjunto de ciudades de la matriz adyacente

      Returns:
        el número de arcos o caminos que hay entre las ciudades  
      '''
      return self._matriz_adyacente[self._matriz_adyacente!=np.float('inf')].sum()

    def insertar_vertice(self, nombre_vertice):
      '''
      Inserta un vertice o ciudad a la matriz de adyacencia

      Args:
          nombre_vertice (srt): nombre del vertice o de la ciudad a agregar al conjunto de ciudades del mapa 
      
      Atributes:
          vetice (str): guarda el nombre del vertice o ciudad a agregar a la matríz de adyacencia

      Returns:
          vertice: nombre de la ciudad o vertice agregado 
      '''
      vertice = None
      if not self.buscar_vertice(nombre_vertice):
          vertice = nombre_vertice
          self._vertices.append(vertice)
          if self._matriz_adyacente.shape[0] == 0:
              self._matriz_adyacente = np.hstack([self._matriz_adyacente, self._matriz_adyacente.shape])
          elif self._matriz_adyacente.shape[0] == 1:
              self._matriz_adyacente = np.hstack([self._matriz_adyacente, np.zeros(self._matriz_adyacente.shape) + + np.float('inf')])
              self._matriz_adyacente = np.vstack([self._matriz_adyacente, np.zeros(self._matriz_adyacente.shape) + + np.float('inf')])                
              self._matriz_adyacente[-1, -1] = 0
          else:
              self._matriz_adyacente = np.hstack([self._matriz_adyacente, np.zeros([self._matriz_adyacente.shape[0], 1]) + np.float('inf')])
              self._matriz_adyacente = np.vstack([self._matriz_adyacente, np.zeros([1, self._matriz_adyacente.shape[1]]) + np.float('inf')])
              self._matriz_adyacente[-1, -1] = 0
      return vertice

    def insertar_arco(self, origen, destino, elemento=None):
      '''
      Inserta un arco o camino a la matriz de adyacencia

      Args:
          origen (srt): nombre del vertice o de la ciudad de partida
          destino (srt): nombre del vertice o de la ciudad de destino
          elemento (int): es el peso del arco que une a la ciudad de origen y de destiono o la cantidad de zombies entre estas. 
      Returns:
          true si el arco o camino se agregó con éxito o false en caso de no haberse agregado. 
      '''
      if self.buscar_vertice(origen) and self.buscar_vertice(destino):
          vertices = np.array(self._vertices)
          origen_i = np.argmax(vertices == origen)
          destino_i = np.argmax(vertices == destino)

          self._matriz_adyacente[origen_i, destino_i] = elemento
          # self._matriz_adyacente[destino_i, origen_i] = elemento
          return True
      return False

    def buscar_vertice(self, nombre_vertice):
      '''
      Busca un vertice o ciudad dentro de la matriz de adyacencia
      
      Args:
        nombre_vertice: nombre del vertice o ciudad a eliminar

      Returns:
          true si el vertice o ciudad se encontró con éxito o false en caso de no haberse encontrado
      '''     
      if nombre_vertice in self._vertices:
          return True
      return False

    def eliminar_vertice(self, nombre_vertice):
      '''
      Elimina un vertice o ciudad de la matriz de adyacencia

      Args:
         nombre_vertice: nombre del vertice o ciudad a eliminar 
      
      Returns:
          true si el vertice o ciudad se eliminó con éxito o false en caso de no haberse eliminado
      '''
      try:
          cursor = np.argmax(np.array(self._vertices) == nombre_vertice)
          self._matriz_adyacente = np.delete(self._matriz_adyacente , cursor, axis=0)
          self._matriz_adyacente = np.delete(self._matriz_adyacente , cursor, axis=1)
          del self._vertices[self._vertices == nombre_vertice]
          return True
      except:
          return False

    def eliminar_arco(self, origen, destino):
      '''
      Elimina un arco o camino de la matriz de adyacencia

      Args:
         origen (srt): nombre del vertice o de la ciudad de partida
         destino (srt): nombre del vertice o de la ciudad de destino 

      Returns:
          true si el arco o camino se eliminó con éxito o false en caso de no haberse eliminado 
      '''
      if self.buscar_vertice(origen) and self.buscar_vertice(destino):
          vertices = np.array(self._vertices)
          origen_i = np.argmax(vertices == origen)
          destino_i = np.argmax(vertices == destino)
          self._matriz_adyacente[origen_i, destino_i] = np.float('inf')
          self._matriz_adyacente[destino_i, origen_i] = np.float('inf')
          return True
      return False

    def verificar_existencia_camino(self, origen, destino):
      '''
      Verifica que exista un arco o camino entre dos ciudades

      Args:
         origen (srt): nombre del vertice o de la ciudad de partida
         destino (srt): nombre del vertice o de la ciudad de destino 

      Returns:
          resultado: devolverá true si el camino existe, false en caso contraio
      '''
      resultado = None
      if self.buscar_vertice(origen) and self.buscar_vertice(destino):
          caminos = self.dijkstra()[origen][destino]
          if caminos != np.float('inf'):
              resultado = True
      return resultado
            
    def obtener_camino_mas_corto(self, origen, destino):
      '''
      Obtiene el camino más corte entre dos vertices o ciudades

      Args:
         origen (srt): nombre del vertice o de la ciudad de partida
         destino (srt): nombre del vertice o de la ciudad de destino 
         
      Returns:
          resultado: devolverá las ciudades y el camino más cercano entre estas. 
      '''
      resultado = None
      if self.buscar_vertice(origen) and self.buscar_vertice(destino):
          caminos = self.dijkstra()
          resultado = caminos[origen][destino]
      return resultado, caminos

    def dijkstra(self):
      '''
      Implementación del algorirmo Dijkstra

       Returns:
          distancias: devolverá la cantidad de zombies o pesos entre ciudades
      
      '''
      vertices = self.obtener_vertices()
      distancias = {}

      for i in vertices: 
          dict_i = {}
          for j in vertices:
              if i == j:
                  dict_i[j] = 0
              else:
                  dict_i[j] = float("inf")
          distancias[i] = dict_i

      for elemento_vertice in vertices: 
          Q = []
          for elemento in vertices: Q.append(elemento)

          while len(Q) != 0:
              v = 0
              min = float("inf")
              for auxiliar in Q:
                  if distancias[elemento_vertice][auxiliar] <= min:
                      min = distancias[elemento_vertice][auxiliar]
                      v = auxiliar
              
              Q.remove(v)

              vecinos = np.array(self._vertices)
              vecinos = vecinos[self._matriz_adyacente[np.argmax(vecinos == v)] == 1]

              for vertices_vecinos in vecinos:
                  w = 1
                  alt = distancias[elemento_vertice][v] + w
                  if alt < distancias[elemento_vertice][vertices_vecinos]:
                      distancias[elemento_vertice][vertices_vecinos] = alt
      return distancias

    def floyd_warshall(self):
      '''
      Muestra el camino más corto entre dos ciudades

      Returns:
           matriz_distancia: matriz con los caminos más cortos para llegar a cualquier vertice o ciudad  
      '''
      V = len(self)
      matriz_distancia = self._matriz_adyacente
      for k in range(V):
          # hace una copia de la matriz de distancia
          siguiente_matriz_distancia = [list(row) for row in matriz_distancia] 
          for i in range(V):
              for j in range(V):
                  # Elije si el vértice k puede funcionar como una ruta con una distancia más corta
                  siguiente_matriz_distancia[i][j] = min(matriz_distancia[i][j], matriz_distancia[i][k] + matriz_distancia[k][j])
          # Se actualiza        
          matriz_distancia = siguiente_matriz_distancia 
      return matriz_distancia

    def __str__(self):
      '''
      Muestra la matriz adyacente del conjunto de vertices o ciudades

      Returns:
          lista_string: matriz adyacente  
      '''
      lista_string = ''
      for index, vertice in enumerate(self._vertices):
          lista_string += f'{str(self._matriz_adyacente[index])} : {vertice} \n'
      return lista_string

    def __len__(self):
      '''
      Muestra cuantos vertices o ciudades hay

      '''
      return len(self._vertices)