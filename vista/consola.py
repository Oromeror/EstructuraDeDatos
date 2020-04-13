import os
import sys

from time import sleep

class Consola:
    '''
    El objeto Consola gestiona la vista del mapa que verá el sobreviviente

    '''
    def __init__(self):
      '''
        Inicializa el objeto Consola 
        
      '''
      if self.get_plataforma() == 'Windows':
        self.borrado_consola = lambda: os.system('cls')
      else:
        self.borrado_consola = lambda: os.system('clear')
      self.iniciar_consola()
    
    def iniciar_consola(self):
      '''
      Inicia el menú a mostrar al sobreviviente

      '''
      print('Bienvenido')
      sleep(0.5)
      input('Presione cualquier tecla para leer el mapa')

    def obtener_opcion(self):
      '''
      Obtiene la opción elegida por el sobreviviente
      
      '''
      try:
          return int(input('Opcion: '))
      except:
          return None
        
    def enviar_opcion_menu(self):
      '''
      Obtiene la opción elegida por el sobreviviente en el menú
      
      '''
      self.borrado_consola()
      print("Seleccione lo que desea hacer con el grafo: ")
      self.mostrar_opciones_menu()
      return self.obtener_opcion()

    def mostrar(self, elemento):
      '''
      Se utiliza para mostrar un elemento recibido por instanciamiento
      
      '''
      self.borrado_consola()
      print(elemento)
      input('Presione une tecla para continuar.')

    def mostrar_opciones_menu(self):
      menu = '''
          1. Añadir camino.
          2. Guardar camino.
          3. Mostrar camino.
          4. Eliminar camino.
          5. Obtener camino más corto.
          6. Mostrar ultima respuesta.
          7. Asignar punto de partida.
          8. Mostrar punto de partida.
          9. Asignar zona segura.
          10. Mostrar zona segura.
          11. Eliminar zona segura.
          12. Salir.
      '''
      print(menu)

    def mostrar_error(self, error):
      '''
      Se utiliza para mostrar un error genérico

      '''
      self.borrado_consola()
      print('Error: {}'.format(error))
      input("Presione una tecla para continuar...")

    
    def propiedad(self, objeto, accion):
      self.borrado_consola()
      return input('Escriba el nombre del {} que quiere {}: '.format(objeto, accion))

    def get_plataforma(self):
      '''
      Se utiliza para validar desde que sistema operativo se esta ejecutando la aplicación

      '''
      plataformas = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
      }
      if sys.platform not in plataformas:
          return sys.platform
      return plataformas[sys.platform]
