from pymongo import MongoClient
import pprint
import datetime
import random
client = MongoClient('localhost', 27017)


def getRandomWord(db,definitions):
    upperLimit=definitions.count_documents({})
    return definitions.find().limit(-1).skip(random.randint(0,upperLimit)).next()


def random_word_requester():
    db = client.mongo_db_lab
    definitions=db.definitions
    randomWord = getRandomWord(db,definitions)
    randomWordID=randomWord["_id"]
    currTime=datetime.datetime.isoformat(datetime.datetime.utcnow())
    print("=== RANDOM WORD AND DEFINITION ===")
    print("Word: {}\nDefinition: {}".format(randomWord["word"],randomWord["definition"]))
    if "dates" in randomWord and isinstance (randomWord["dates"],list) : 
        definitions.update_one({"_id": randomWordID},{"$push": {"dates": currTime }})
    else:
        definitions.find_one_and_update({"_id": randomWordID},{"$set": {"dates": [currTime] }})
    #definitions.update_one({"_id": str(randomWordID)},{"$push": randomWord})
    return definitions.find_one({"_id": randomWordID})
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    return


if __name__ == '__main__':
    pprint.pprint(random_word_requester())
