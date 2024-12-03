from pymongo import MongoClient

def database(database_name, collection_name):
    client = MongoClient('mongodb://localhost:27017')  # Cambia la URI si es necesario
    db = client[database_name]
    collection = db[collection_name]
    return collection

def ping():
    try:
        client = MongoClient('mongodb://localhost:27017', serverSelectionTimeoutMS=1000)
        client.admin.command('ping')  # Ping explícito al servidor
        print("Conexión exitosa a MongoDB.")
        return True
    except Exception as e:
        print(f"No se pudo conectar a MongoDB: {e}")
        return False
