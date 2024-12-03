import json
from Grupo import Grupo
from Alumno import Alumno
from List import List
class Carrera(List):
   
    def __init__(self, nombre = None, clave = None):
        self.isObject = False
        if(nombre != None and clave != None):
            self.nombre = nombre
            self.clave = clave
            self.grupos = Grupo()
            self.isObject = True
        else:
            super().__init__()

    def __str__(self):
        if(self.isObject): 
            return 'Nombre: ' + self.nombre + '\nClave: ' + self.clave + '\nTiene: ' + str(len(self.grupos.getAllList())) + ' grupo(s)\n'
        else:
            return 'Tiene: ' + str(len(self.getAllList())) + ' alumno(s)'
        
    def returnDictionary(self):
        if(self.isObject):
            return {
                "nombre": self.nombre,
                "clave": self.clave,
                "grupos": self.grupos.returnDictionary(),
            }
        else:
            return [ c.returnDictionary() for c in self.list ]
        
    def convertJsonToObject(self, nameFile):
        if(not self.isObject):
            readGrupoJson = open(nameFile+".json", "r")
            writeGrupoJson = json.load(readGrupoJson)
            # print(writeCarreraJson[0]["alumnos"])
            for carrera in writeGrupoJson:
                carreraObject = Carrera(carrera["nombre"], carrera["clave"])
                if(carrera["grupos"]):
                    for grupo in carrera["grupos"]:
                        grupoObject = Grupo(grupo["seccion"], grupo["grado"])

                        if(grupo["alumnos"]):
                            for alumno in grupo["alumnos"]:
                                alumnoObject = Alumno(alumno["nombres"], alumno["apellidoPaterno"], alumno["apellidoMaterno"], alumno["curp"], alumno["reticula"])
                                grupoObject.alumnos.addToList(alumnoObject)

                        carreraObject.grupos.addToList(grupoObject)
                self.addToList(carreraObject)
        return self



if __name__ == "__main__":
        
    # Declaración de los objetos de la clase Alumno
    # alumno1 = Alumno("Luis Fernando", "Robles", "Ibarra", "ROIL010", "22170132")
    # alumno2 = Alumno("Uriel Fernando", "Montier", "Olivar", "URIFE14", "32442129")
    # alumno3 = Alumno("Saul Canelo", "Casterona", "Nuñez", "SAUNE190", "9759201")

    # grupo1 = Grupo("A", "7")
    # grupo1.alumnos.addToList(alumno1)
    # grupo1.alumnos.addToList(alumno2)
    # grupo1.alumnos.addToList(alumno3)

    # grupoArray = Grupo()
    # grupoArray.addToList(grupo1)

    # carrera1 = Carrera("Desarrollo de software", "1")
    # carrera1.grupos.addToList(grupo1)

    # carreraArray = Carrera()
    # carreraArray.addToList(carrera1)
    # carreraArray.saveListToJson("carrera")

    carrera = Carrera()
    carreraFromJson = carrera.convertJsonToObject("carrera")
    print(carrera.returnDictionary())