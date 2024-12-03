import json
from Alumno import Alumno
from List import List
class Grupo(List):
    def __init__(self, seccion = None, grado = None):
        self.isObject = False
        if(seccion != None and grado != None):
            self.seccion = seccion
            self.grado = grado
            self.alumnos = Alumno()
            self.isObject = True
        else:
            super().__init__()

    def __str__(self):
        if(self.isObject):
            return 'Sección: ' + self.seccion + '\nGrado: ' + self.grado + '\nTiene: ' + str(len(self.alumnos.getAllList())) + ' alumnos\n'
        else:
            return 'Tiene: ' + str(len(self.getAllList())) + ' grupos(s)'
    
    def returnDictionary(self):
        if(self.isObject):
            return {
                "seccion": self.seccion,
                "grado": self.grado,
                "alumnos": self.alumnos.returnDictionary(),
            }
        else:
            return [ g.returnDictionary() for g in self.list ]
        
    def convertJsonToObject(self, nameFile):
        if(not self.isObject):
            readGrupoJson = open(nameFile+".json", "r")
            writeGrupoJson = json.load(readGrupoJson)
            # print(writeCarreraJson[0]["alumnos"])
           
            for grupo in writeGrupoJson:
                grupoObject = Grupo(grupo["seccion"], grupo["grado"])

                if(grupo["alumnos"]):
                    for alumno in grupo["alumnos"]:
                        alumnoObject = Alumno(alumno["nombres"], alumno["apellidoPaterno"], alumno["apellidoMaterno"], alumno["curp"], alumno["matricula"])
                        grupoObject.alumnos.addToList(alumnoObject)
                self.addToList(grupoObject)
        return self

           


if __name__ == "__main__":
     


    print("-------------")
    object = Grupo()
    arrayGruposFromJson = object.convertJsonToObject("grupo")
    print(object.returnDictionary())
