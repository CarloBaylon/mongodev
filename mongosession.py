from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import mongoconfig

def create_client():
    try:
        return MongoClient(host = 'localhost', port = 27017)
    except ConnectionFailure:
        print("Connection failed")


client = create_client()