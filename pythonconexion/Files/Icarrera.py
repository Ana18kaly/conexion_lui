from database import database
from Carrera import Carrera
from IGrupo import IGrupo
class Icarrera():
    def __init__(self, objectCarreras = None):
        self.receiveObject = False
        if(objectCarreras == None):
            self.carreras = Carrera().convertJsonToObject("carrera")
        else:
            self.receiveObject = True
            self.carreras = objectCarreras

    def __str__(self):
        if(self.receiveObject):
            return f"{len(self.carreras.getAllList())} carreras"
        
    def mostrarCarreras(self):
        self.carreras.showObjects()
    
    def agregarCarrera(self):
        print("Escriba el nombre de la carrera")
        nombre = input()
        print("Escriba el clave de la carrera")
        clave = input()

        carrera = Carrera(nombre, clave)
        self.carreras.addToList(carrera)


        interfazGrupo = IGrupo(carrera.grupos)
        interfazGrupo.menu()

        if(self.receiveObject):
            database = database("3clases", "carrera")
            database.insert_one(carrera.returnDictionary())
    
    def eliminarCarrera(self):

        if(len(self.carreras.getAllList()) > 0):
            print("Actualmente cuenta con estas carreras")
            self.mostrarCarreras()
            print("Cuál quiere eliminar")
            index = int(input())
            self.carreras.deleteItemByIndex(index)
            return
        
        print("No cuenta con carreras agregadas")
    
    def editarCarrera(self):
        if(len(self.carreras.getAllList()) > 0):
            print("Actualmente cuenta con estos grupos:")
            self.mostrarCarreras()
            print("¿Cuál grupo quiere editar?")
            index = input()

            print("Escriba el nuevo nombre de la carrera")
            nombre = input()
            print("Escriba la nueva clave de la carrera")
            clave = input()

            carrera = Carrera(nombre, clave)
            self.carreras.editItem(index, carrera)

    def modificarGrupoCarrera(self):
        if(len(self.carreras.getAllList()) > 0):
            print("Elige el grupo al que quieres agregar el alumno:")
            self.mostrarCarreras()
            print("Elija la carrera")
            indexCarrera = int(input())
            carrera = self.carreras.getListByIndex(indexCarrera)

            interfazGrupo = IGrupo(carrera.grupos)
            interfazGrupo.menu()
            return
        print("Actualmente no cuenta con carreras")

    def menu(self):
        print("==================== CARRERAS ====================")
        print("Elija la acción que desea hacer:")
        print("1. Agregar carrera")
        print("2. Editar carrera")
        print("3. Eliminar carrera")
        print("4. Mostrar carreras")
        print("5. Agregar alumnos a carrera")
        print("-1. Salir\n")
        opcion = int(input())

        if(opcion == 1):
            self.agregarCarrera()
            self.menu()
        elif(opcion == 2):
            self.editarCarrera()
            self.menu()
        elif(opcion == 3):
            self.eliminarCarrera()
            self.menu()
        elif(opcion == 4):
            self.mostrarCarreras()
            self.menu()
        elif(opcion == 5):
            self.modificarGrupoCarrera()
            self.menu()
        elif(opcion == -1):
            return
        else:
            print("Opción no encontrada")
            print("Para salir presione -1")
            self.menu()

if __name__ == "__main__":
    carrera = Carrera()
    interfazCarrera = ICarrera(carrera)
    interfazCarrera.menu()