from pymongo import MongoClient

def access_mdb_local_collection (database, collection):

    """ Conects to a collection inside a DataBase host in my local Server

    :database: str : database where the the collection is stored
    :collection: str: the collection to connect to.

    """

    # 1. Connect to my local Server
    client = MongoClient("localhost:27017")
    
    # 2. Access a DataBase:
    db = client[database]

    # 3. Acces a collection inside the given DataBase
    c = db.get_collection(collection)

    # 4. Return collection
    return c
