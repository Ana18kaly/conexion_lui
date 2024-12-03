from database import database, ping
from Alumno import Alumno
import json
import os

class Ialumno:
    def __init__(self, objectAlumno=None):
        """
        Clase para gestionar alumnos utilizando tanto una base de datos (MongoDB) como archivos JSON.

        Parámetros:
            objectAlumno (Alumno): Objeto Alumno para inicializar la interfaz. Si es None, se inicializa desde un archivo JSON.
        """
        # Inicializa la colección de MongoDB
        self.collection = database("example", "alumnos")

        # Bandera para saber si se recibió un objeto Alumno
        self.receiveObject = False
        if objectAlumno is None:
            # Carga los datos de alumnos desde un archivo JSON
            self.alumnos = Alumno().convertJsonToObject("alumno")
        else:
            self.receiveObject = True
            self.alumnos = objectAlumno

        # Verifica la conexión a MongoDB al inicio
        if ping():
            print("Conexión a MongoDB exitosa.")
            self.synchronizeJsonToMongoDB()  # Sincroniza los datos del JSON a MongoDB si es necesario
        else:
            print("No se pudo conectar a MongoDB al inicio. Los datos permanecerán en el archivo JSON.")

    def synchronizeJsonToMongoDB(self):
        """
        Sincroniza los datos desde un archivo JSON hacia MongoDB.
        Solo se sincronizan los registros nuevos (basados en el CURP).
        """
        try:
            json_file = "alumno"  # Nombre del archivo JSON
            if os.path.exists(json_file + ".json"):
                with open(json_file + ".json", "r") as file:
                    alumnos_data = json.load(file)
                    
                    if alumnos_data:
                        print(f"Se encontraron {len(alumnos_data)} alumnos en el archivo JSON. Insertando en MongoDB...")

                        # Insertar cada alumno en MongoDB si no existe
                        for alumno_data in alumnos_data:
                            if not self.collection.find_one({"curp": alumno_data["curp"]}):
                                addAlumno = Alumno.deserializeObject(alumno_data)
                                result = self.collection.insert_one(addAlumno.serializeObject())
                                if result.inserted_id:
                                    print(f"Alumno insertado en MongoDB con ID: {result.inserted_id}")
                                else:
                                    print("Error al insertar el alumno en MongoDB.")
                            else:
                                print(f"El alumno con CURP {alumno_data['curp']} ya existe en la base de datos.")

                        # Limpiar el archivo JSON después de sincronizar
                        open(json_file + ".json", "w").close()
                        print("Datos sincronizados. El archivo JSON ha sido limpiado.")
                    else:
                        print("El archivo JSON está vacío. No se necesita sincronización.")
        except FileNotFoundError:
            print("No se encontró el archivo JSON.")
        except Exception as e:
            print(f"Error al sincronizar datos con MongoDB: {e}")

    def __str__(self):
        """
        Representación en cadena para la clase IAlumno.
        
        Retorna:
            str: Número de alumnos actualmente cargados.
        """
        return f"{len(self.alumnos)} alumnos"

    def agregarAlumno(self):
        """
        Agrega un nuevo alumno solicitando los datos al usuario.
        Los datos se insertan en MongoDB si hay conexión; de lo contrario, se almacenan en JSON.
        """
        print("Iniciando el proceso para agregar un nuevo alumno.")
        nombres = input("Introduce el nombre: ")
        ap_paterno = input("Escribe el primer apellido: ")
        ap_materno = input("Escribe el segundo apellido: ")
        curp = input("Introduce el CURP del estudiante: ")
        matricula = input("Número de matrícula del estudiante: ")

        addAlumno = Alumno(nombres, ap_paterno, ap_materno, curp, matricula)
        self.alumnos.append(addAlumno)

        if ping():
            print("Conexión a MongoDB exitosa. Insertando en la base de datos.")
            if not self.collection.find_one({"curp": curp}):  # Verificar si el alumno ya existe
                result = self.collection.insert_one(addAlumno.serializeObject())
                if result.inserted_id:
                    print(f"Alumno insertado en MongoDB con ID: {result.inserted_id}")
                    self.synchronizeJsonToMongoDB()
                else:
                    print("No se pudo insertar el alumno en MongoDB.")
            else:
                print(f"El alumno con CURP {curp} ya existe en la base de datos.")
        else:
            print("No se pudo conectar a MongoDB. Guardando en el archivo JSON.")
            Alumno().saveObjectToJson(self.alumnos, "alumno")

        print("Proceso de agregar alumno completado.")
        print(self)

    def eliminarAlumno(self):
        """
        Elimina un alumno por índice tras mostrar una lista de los alumnos actuales.
        """
        print(f"Selecciona el número del estudiante a eliminar. Hay {self} disponibles:")
        for idx, alumno in enumerate(self.alumnos, start=1):
            print(f"{idx}. {alumno}")
        
        try:
            indice_eliminar = int(input("Número: ")) - 1
            if 0 <= indice_eliminar < len(self.alumnos):
                self.alumnos.pop(indice_eliminar)
                print("Alumno eliminado exitosamente.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Entrada inválida. Debe ser un número.")

        if not self.receiveObject:
            Alumno().saveObjectToJson(self.alumnos, "alumno")

    def editarAlumno(self):
        """
        Modifica los datos de un alumno existente en la lista.
        """
        print(f"Selecciona el número del estudiante a modificar. Hay {self} disponibles:")
        for idx, alumno in enumerate(self.alumnos, start=1):
            print(f"{idx}. {alumno}")

        try:
            indice_editar = int(input("Número: ")) - 1
            if 0 <= indice_editar < len(self.alumnos):
                nombres = input("Nuevo nombre: ")
                ap_paterno = input("Nuevo primer apellido: ")
                ap_materno = input("Nuevo segundo apellido: ")
                curp = input("Nuevo CURP: ")
                matricula = input("Nueva matrícula: ")

                self.alumnos[indice_editar] = Alumno(nombres, ap_paterno, ap_materno, curp, matricula)
                print("Alumno modificado exitosamente.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Entrada inválida. Debe ser un número.")

        if not self.receiveObject:
            Alumno().saveObjectToJson(self.alumnos, "alumno")

    def mostrarAlumnos(self):
        """
        Muestra la lista de alumnos actuales.
        """
        if not self.alumnos:
            print("No hay estudiantes registrados.")
            return

        print(f"Lista de estudiantes registrados ({self}):")
        for idx, alumno in enumerate(self.alumnos, start=1):
            print(f"{idx}. {alumno}")

    def menu(self):
        while True:  # Aseguramos un ciclo continuo hasta que se elija finalizar
            print("***** SISTEMA DE GESTIÓN DE ESTUDIANTES *****")
            print("Seleccione una opción:")
            print("1. Registrar nuevo estudiante")
            print("2. Modificar datos de estudiante")
            print("3. Dar de baja estudiante")
            print("4. Ver lista de estudiantes")
            print("0. Finalizar\n")
            opcion = input("Opción: ").strip()  # Aseguramos que no haya espacios en blanco

            if opcion == "1":
                self.agregarAlumno()
            elif opcion == "2":
                self.editarAlumno()
            elif opcion == "3":
                self.eliminarAlumno()
            elif opcion == "4":
                self.mostrarAlumnos()
            elif opcion == "0":
                print("Finalizando el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.\n")

if __name__ == "__main__":
    interfaz = IAlumno()
    interfaz.menu()
