from pymongo import database
from mongosession import client


test_client = client

test_data = {
    "test": "Hello",
    "test2": "goodbye"
}
mydb = test_client["testdb"]
mycol = mydb["testcol"]

f = mycol.insert_one(test_data)
print(mycol.find_one()["test"])
