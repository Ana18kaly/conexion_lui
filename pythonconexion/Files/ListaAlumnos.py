import json
class ListaAlumnos:
    def __init__(self):
        """Inicializa una lista para almacenar alumnos."""
        self.alumnos = []

    def addToList(self, alumno):
        """Agrega un alumno a la lista."""
        self.alumnos.append(alumno)

    def getAllList(self):
        """Devuelve todos los alumnos."""
        return self.alumnos

    def deleteItemByIndex(self, idx):
        """Elimina un alumno por su índice."""
        if 0 <= idx < len(self.alumnos):
            del self.alumnos[idx]
        else:
            print("Índice fuera de rango.")

    def editItem(self, idx, nuevoAlumno):
        """Edita un alumno en la lista por su índice."""
        if 0 <= idx < len(self.alumnos):
            self.alumnos[idx] = nuevoAlumno
        else:
            print("Índice fuera de rango.")

    def showObjects(self):
        """Muestra todos los alumnos en la lista."""
        if not self.alumnos:
            print("No hay alumnos en la lista.")
        else:
            print("Lista de alumnos:")
            for idx, alumno in enumerate(self.alumnos, 1):
                print(f"{idx}. {alumno}")

    def saveListToJson(self, nameFile):
        """Guarda la lista de alumnos en un archivo JSON."""
        try:
            with open(nameFile + ".json", "w") as file:
                json.dump([alumno.returnDictionary() for alumno in self.alumnos], file, indent=4)
            print(f"Lista de alumnos guardada exitosamente en {nameFile}.json")
        except Exception as e:
            print(f"Error al guardar en JSON: {e}")

    def loadListFromJson(self, nameFile):
        """Carga la lista de alumnos desde un archivo JSON."""
        try:
            with open(nameFile + ".json", "r") as file:
                data = json.load(file)
                self.alumnos = [Alumno(**alumno) for alumno in data]
            print(f"Lista de alumnos cargada exitosamente desde {nameFile}.json")
        except FileNotFoundError:
            print(f"El archivo {nameFile}.json no existe.")
        except Exception as e:
            print(f"Error al cargar desde JSON: {e}")