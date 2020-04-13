from vista.consola import Consola
from modelo.mapa import Mapa
from modelo.respuesta import Respuesta

'''
    El objeto Ejecutor gestiona la inicialización del programa y controla las elecciones que toma el sobreviviente en el

'''
class Ejecutor:
  def __init__(self):
      self.iniciar()
  
  def iniciar(self):
    '''
    Se quiere mostrar un menú al superviviente Colombiano en el mapa político del territorio nacional Colombiano (MiColombia.in)

    Atributes:
        consola (Consola): es la instancia del objeto Consola que es la vista que se mostrará al sobreviviente
        mapa (Mapa): es la instancia del objeto Mapa que se sirve para controlar las elecciones por el sobreviviente 

    Returns:
        opcion_seleccion: es la opción elegida por el superviviente 
    '''
    self.consola = Consola()

    self.mapa = Mapa()

    while True:
      opcion = self.consola.enviar_opcion_menu()
      if opcion == 1:
        self.agregar_camino()
      elif opcion == 2:
        self.guardar_caminos()   
      elif opcion == 3:
        self.mirar_mapa()
      elif opcion == 4:
        self.eliminar_camino()
      elif opcion == 5:
        self.obtener_menor_camino()
      elif opcion == 6:
        self.mostrar_ultima_respuesta()
      elif opcion == 7:
        self.asignar_punto_partida()
      elif opcion == 8:
        self.consola.mostrar(self.mapa.mostrar_punto_partida())
      elif opcion == 9:
        self.agregar_zona_segura()
      elif opcion == 10:
        self.consola.mostrar(self.mapa.mostrar_zonas_seguras())
      elif opcion == 11:
        self.eliminar_zona_segura()
      elif opcion == 12:
        break
      else:
        self.consola.mostrar_error('Seleccione una opción valida')

  def mirar_mapa(self):
    '''
     Muestra el mapa
      
      Returns:
        muestra los zombies o peso que hay entre la ciudad de partida y de destino
    '''
    self.consola.mostrar(self.mapa.mostrar_caminos())
  
  def agregar_camino(self):
    '''
     Agrega caminos al mapa

      Atributes:
        origen (srt): es el nombre de una ciudad a conectar
        destino (srt): es el nombre de la ciudad conectada
        cantidad_zombies: es el número de zombies en el camino entre las ciudades

      Raises:
        RuntimeError: se debe escribir un número para los zombies
    '''
    origen = self.consola.propiedad('inicio', 'agregar')
    destino = self.consola.propiedad('fin', 'agregar')
    cantidad_zombies = self.consola.propiedad('zombies', 'agregar')
    try:
      resultado = self.mapa.agregar_camino(origen, destino, int(cantidad_zombies))
      if not resultado:
          self.consola.mostrar_error('No existe un arco con esas propiedades.')
    except Exception:
      self.consola.mostrar_error('Debes escribir un NUMERO de zombies')

  def guardar_caminos(self):
    '''
     Guarda los caminos en el archivo 'MiColombia.in'

    '''
    if self.mapa.guardar_caminos():
      self.consola.mostrar("Se guardo correctamente el archivo")
    else:
      self.consola.mostrar_error('No se pudo guardar el archivo')

  def eliminar_camino(self):
    '''
     Elimina un camino del mapa y del archivo 'MiColombia.in'

      Atributes:
        origen (srt): es el nombre de una ciudad a conectar
        destino (srt): es el nombre de la ciudad conectad
    '''
    origen = self.consola.propiedad('inicio', 'eliminar')
    destino = self.consola.propiedad('fin', 'eliminar')
    if self.mapa.eliminar_camino(origen, destino):
      self.consola.mostrar('Se elimino correctamente el camino')
    else:
      self.consola.mostrar('Ocurrio un error eliminando el camino. No se encontro, está asociado a una zona segura o es un punto de partida')

  def obtener_menor_camino(self):
    '''
    Devuelve el peso más bajo, camino más corto o la menor cantidad de zombies entre una ciudad de partida y una ciudad de destino

    '''
    ciudad, valor = self.mapa.obtener_camino_corto()
    if valor:
      respuesta = Respuesta().escribir_respuesta(ciudad)
      self.consola.mostrar(f'El valor es {valor}. Ciudad {ciudad}')
    else:
      respuesta = Respuesta().escribir_respuesta(None)
      self.consola.mostrar('No se encontro un camino valido')
  
  def mostrar_ultima_respuesta(self):
    '''
     Busca la última respuesta brindada al sobreviviente sobre el camino con la menor cantidad de zombies o menor peso dentro del archivo respuesta.out

      Atributes:
        respuesta (srt): última respuesta obtenida del archivo 'MiColombia.in'
    '''
    respuesta = Respuesta().obtener_respuesta()
    if respuesta:
      self.consola.mostrar(respuesta)
    else:
      self.consola.mostrar_error("Hubo un error obteniendo la respuesta")

  def mostrar_ciudades(self):
    '''
     Muestra los nombres de los vertices o ciudades dentro del mapa
    '''
    print(self.mapa.obtener_nombres_ciudades())

  def asignar_punto_partida(self):
    '''
     Asigna un vertice o ciudad al punto de partida

      Atributes:
        punto_partida (srt): ciudad de partida
        resultado (srt): resultado de agregar el punto de partida
    '''
    punto_partida = self.consola.propiedad('punto partida', 'agregar')
    try:
      resultado = self.mapa.asignar_punto_partida(punto_partida)
      if not resultado:
          self.consola.mostrar_error('No existe una ciudad con esas propiedades.')
    except Exception:
      self.consola.mostrar_error('Hubo un error obteniendo la respuesta')

  def agregar_zona_segura(self):
    '''
     Agrega un vertice o ciudad a la zona segura

      Atributes:
        zona_segura (srt): ciudad de partida agregada a la zona segura
        resultado (srt): resultado de agregar el punto de partida a la zona segura
    '''    
    zona_segura = self.consola.propiedad('zona segura', 'agregar')
    try:
      resultado = self.mapa.agregar_zona_segura(zona_segura)
      if not resultado:
          self.consola.mostrar_error('No existe una zona con esas propiedades.')
    except Exception:
      self.consola.mostrar_error('Hubo un error obteniendo la respuesta')

  def eliminar_zona_segura(self):
    '''
     Elimina un vertice o ciudad de la zona segura

      Atributes:
        zona_segura (srt): 
        resultado (srt): resultado de eliminar el punto de partida de la zona segura
    '''
    zona_segura = self.consola.propiedad('zona segura', 'eliminar')
    try:
      resultado = self.mapa.eliminar_zona_segura(zona_segura)
      if not resultado:
          self.consola.mostrar_error('No existe una zona con esas propiedades.')
    except Exception:
      self.consola.mostrar_error('Hubo un error obteniendo la respuesta')