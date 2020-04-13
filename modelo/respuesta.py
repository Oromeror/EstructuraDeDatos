import pickle
class Respuesta:
  '''
    El objeto Respuesta gestiona el archivo de respuesta 'respuesta.out' que se brinda al sobreviviente

  '''
  def obtener_respuesta(self):
    '''
      Obtiene la última respuesta del archivo 'respuesta.out' 

      Atributes:
          respuesta (str): se almacena el registro de la última respuesta dada al sobreviviente
      
      Returns: 
          la última respuesta brindada al sobreviviente
    '''
    try:
      with open('respuesta.out', 'rb') as current_file:
        respuesta = pickle.load(current_file)
        print(respuesta)
        current_file.close()
    except:
      return False
    return respuesta

  def escribir_respuesta(self, respuesta):
    '''
      Escribe la última respuesta del archivo 'respuesta.out' 
      
      Returns: 
          true si se escribió la última respuesta y false en caso contrario 
    '''
    try:
      with open('respuesta.out', 'wb') as current_file:
        if respuesta:
          pickle.dump(f"My little doggy, la zona segura de menos riesgo es {respuesta}", current_file)
        else:
          pickle.dump(f"Lo siento socio.", current_file)
        current_file.close()
      return True
    except:
      return False