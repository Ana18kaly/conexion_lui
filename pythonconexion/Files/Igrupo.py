from database import database
from IAlumno import IAlumno
from Alumno import Alumno
from Grupo import Grupo
class Igrupo():
    def __init__(self, objectGrupo = None):
        self.receiveObject = False
        if(objectGrupo == None):
            self.grupos = Grupo().convertJsonToObject("grupo")
        else:
            self.receiveObject = True
            self.grupos = objectGrupo

    def __str__(self):
        return f"{len(self.grupos.getAllList())} grupos"
    
    def agregarGrupo(self):
        print("Ingresa la sección del grupo:")
        seccion = input()
        print("Ingresa el grado del grupo:")
        grado = input()

        grupo = Grupo(seccion, grado)
        self.grupos.addToList(grupo)

        interfazAlumno = IAlumno(grupo.alumnos)
        interfazAlumno.menu()
        self.menu()

        if(not self.receiveObject):
            self.grupos.saveListToJson("grupo")

        if(self.receiveObject):
            db = database("admin", "test_collection")
            db.insert_one(grupo.returnDictionary())

    def mostrarGrupos(self):
        if(len(self.grupos.list) < 1):
            print("Actualmente no cuentas con grupos en la lista")
            self.menu()
            return
        print(f"Actualmente cuentas con {self} los cuales son:")
        self.grupos.showObjects()

        if(not self.receiveObject):
            self.grupos.saveListToJson("grupo")
    
    def eliminarGrupo(self):
        print("¿Qué grupo quieres eliminar? Acutalmente cuentas con estos")
        self.mostrarGrupos()
        indice = int(input())

        self.grupos.deleteItemByIndex(indice)

        print("Tu lista de grupos quedó así")
        self.mostrarGrupos()

        if(not self.receiveObject):
            self.grupos.saveListToJson("grupo")

    def editarGrupo(self):
        print("¿Qué grupo quieres editar? Actualmente cuentas con estos grupos")
        self.mostrarGrupos()
        print("Escribe el índice:")
        indice = int(input())
        print("Ingresa la sección del grupo:")
        seccion = input()
        print("Ingresa el grado del grupo:")
        grado = input()

        grupo = Grupo(seccion, grado)

        self.grupos.editItem(indice, grupo)

        if(not self.receiveObject):
            self.grupos.saveListToJson("grupo")

    def modificarAlumnosDelGrupo(self):
        if(len(self.grupos.getAllList()) > 0):
            print("Elige el grupo al que quieres agregar el alumno:")
            self.mostrarGrupos()
            indexGrupo = int(input())
            grupo = self.grupos.getListByIndex(indexGrupo)

            iAlumno = IAlumno(grupo.alumnos)
            iAlumno.menu()
            self.menu()
            return
        print("Actualmente no cuentas con grupos")

    def menu(self):
        print("==================== GRUPOS ====================")
        print("Elija la acción que desea hacer:")
        print("1. Agregar grupo")
        print("2. Editar grupo")
        print("3. Eliminar grupo")
        print("4. Mostrar grupo")
        print("5. Agregar alumnos al grupo")
        print("-1. Salir\n")
        opcion = int(input())

        if(opcion == 1):
            self.agregarGrupo()
            self.menu()
        elif(opcion == 2):
            self.editarGrupo()
            self.menu()
        elif(opcion == 3):
            self.eliminarGrupo()
            self.menu()
        elif(opcion == 4):
            self.mostrarGrupos()
            self.menu()
        elif(opcion == 5):
            self.modificarAlumnosDelGrupo()
        elif(opcion == -1):
            return
        else:
            print("Opción no encontrada")
            print("Para salir presione -1")
            self.menu()

    
if __name__ == "__main__":
    grupo = Grupo()
    InterfazGrupo = IGrupo(grupo)
    InterfazGrupo.menu()
