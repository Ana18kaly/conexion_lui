import json

class List:
    def __init__(self):
        self.list = []

    def addToList(self, item):
        self.list.append(item)
    
    def deleteLastItem(self):
        if(len(self.list) >= 0):
            self.list.pop()
        else:
            return "El array está vacío"
        
    def deleteItemByIndex(self, index):
        if 0 <= index < len(self.list):
                self.list.pop(index)
        else:
            print("Índice fuera de rango o lista vacía.")

        
    def editItem(self, index, object):
        self.list[index - 1] = object
        return self.list[index - 1]
        
    def getAllList(self):
        return self.list

    def getListByIndex(self, index):
        return self.list[index - 1]
    
    def showObjects(self):
        for object in self.list:
            print(object)

    def showObject(self, index):
        print(self.list[index - 1])

    def returnDictionary(self):
        if(len(self.list) > 1):
            return [item.__dict__ for item in self.list]
        else :
            return self.list[0].__dict__

    def saveListToJson(self, nameFile):
        listSerializable = self.returnDictionary()

        saveFile = open(nameFile + ".json", "w")
        json.dump(listSerializable, saveFile, indent=4)
        saveFile.close()