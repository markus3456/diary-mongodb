from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['diary']
entries_collection = db['entries']

# Functions
# Retrieve all entries
def print_entries():
    entries = entries_collection.find()

    # Iterate through the entries
    for entry in entries:
        print(entry)

def update_entry():
    query = {"_id": ObjectId('65c222e7a615df32f31f6ea1') }
    change_to = {"$set": { "content": "update is working" }}
    entries_collection.update_one(query, change_to)

    id = {"_id": ObjectId('65c222e7a615df32f31f6ea1') }
    entries = entries_collection.find(id)
    for entry in entries:
        print(entry)
#c
#r = print_entries()
u = update_entry() 

