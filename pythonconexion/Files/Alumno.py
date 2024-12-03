import json
import sys
sys.path.append('C:/ruta/del/directorio')
from alumno import Alumno


class Alumno:
    def __init__(self, nombres="", apellidoPaterno="", apellidoMaterno="", curp="", matricula=""):
        """
        Inicializa un objeto Alumno con atributos para nombres, apellidos, CURP y matrícula.
        
        Parámetros:
            nombres (str): Nombres del alumno.
            apellidoPaterno (str): Apellido paterno del alumno.
            apellidoMaterno (str): Apellido materno del alumno.
            curp (str): CURP del alumno.
            matricula (str): Matrícula del alumno.
        """
        self.nombres = nombres
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.curp = curp
        self.matricula = matricula

    def __str__(self):
        """
        Devuelve una representación en forma de string del objeto Alumno.
        
        Retorna:
            str: Información del alumno en formato legible.
        """
        return (f"{self.nombres} {self.apellidoPaterno} {self.apellidoMaterno} "
                f"(CURP: {self.curp}, Matrícula: {self.matricula})")

    def serializeObject(self):
        """
        Convierte el objeto Alumno en un diccionario, útil para la serialización a JSON.
        
        Retorna:
            dict: Diccionario con los datos del alumno.
        """
        return {
            "nombres": self.nombres,
            "apellidoPaterno": self.apellidoPaterno,
            "apellidoMaterno": self.apellidoMaterno,
            "curp": self.curp,
            "matricula": self.matricula,
        }

    @classmethod
    def deserializeObject(cls, data):
        """
        Crea un objeto Alumno a partir de un diccionario (útil para deserializar datos de JSON).
        
        Parámetros:
            data (dict): Diccionario con los datos del alumno.
        
        Retorna:
            Alumno: Un nuevo objeto Alumno creado a partir del diccionario.
        """
        return cls(
            nombres=data.get("nombres", ""),
            apellidoPaterno=data.get("apellidoPaterno", ""),
            apellidoMaterno=data.get("apellidoMaterno", ""),
            curp=data.get("curp", ""),
            matricula=data.get("matricula", "")
        )

    def convertJsonToObject(self, json_file):
        """
        Lee un archivo JSON y convierte los datos en una lista de objetos Alumno.
        
        Parámetros:
            json_file (str): Nombre del archivo JSON (sin la extensión .json).
        
        Retorna:
            list: Lista de objetos Alumno creados a partir del JSON, o lista vacía si ocurre un error.
        """
        try:
            with open(f"{json_file}.json", "r") as file:
                data = json.load(file)
                return [Alumno.deserializeObject(alumno) for alumno in data]
        except FileNotFoundError:
            print(f"No se encontró el archivo {json_file}.json.")
            return []
        except Exception as e:
            print(f"Error al cargar datos desde JSON: {e}")
            return []

    def saveObjectToJson(self, alumnos, json_file):
        """
        Guarda una lista de objetos Alumno en un archivo JSON.
        
        Parámetros:
            alumnos (list): Lista de objetos Alumno.
            json_file (str): Nombre del archivo JSON donde se guardarán los datos (sin la extensión .json).
        """
        try:
            with open(f"{json_file}.json", "w") as file:
                json.dump([alumno.serializeObject() for alumno in alumnos], file, indent=4)
                print(f"Datos guardados exitosamente en {json_file}.json")
        except Exception as e:
            print(f"Error al guardar datos en JSON: {e}")
