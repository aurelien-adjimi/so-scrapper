from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/"
    
    client = MongoClient(CONNECTION_STRING)
    
    return client['so-scrapper']

def clear_collection():
    db = get_database()
    collection = db["questions"]
    collection.delete_many({}) 
    print("Existing data cleared from MongoDB")

def save_to_mongo(data):
    db = get_database()
    collection = db["questions"]
    clear_collection()
    collection.insert_many(data)
    print("Data successfully saved to MongoDB")

if __name__ == "__main__":
    dbname = get_database()
