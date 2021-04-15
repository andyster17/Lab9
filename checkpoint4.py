from pymongo import MongoClient
import pprint
client = MongoClient('localhost', 27017)

"""Fetch all records
Fetch one record
Fetch a specific record
Fetch a record by object id
Insert a new record"""


if __name__ == '__main__':
    db = client.mongo_db_lab
    definitions=db.definitions
    print("===== FINDING ALL RECORDS =====")
    for definition in definitions.find():
        pprint.pprint(definition)
    print("===== FINDING ONE RECORD =====")
    pprint.pprint(definitions.find_one())
    print("===== FINDING A SPECIFIC RECORD FOR THE WORD:BLOW OFF =====")
    pprint.pprint(definitions.find_one({"word":"Blow Off"}))

    print("===== INSERTING A NEW RECORD =====")
    newRecord={"definition":"A class about open source software","word":"OSS"}
    resultID =definitions.insert_one(newRecord).inserted_id
    print(resultID)
    print("==== FINDING A RECORD BY OBJECT ID =====")
    print("finding newly inserted record")
    pprint.pprint(definitions.find_one({"_id":resultID}))