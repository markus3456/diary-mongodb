from pymongo import MongoClient
from bson.objectid import ObjectId
import re

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


def query_content(a):
    
    query = {'content': {'$regex': re.compile(a, re.IGNORECASE)}}
    specific_content_entries = entries_collection.find(query)
    matching_count = entries_collection.count_documents(query)
    for entry in specific_content_entries:
        print(entry)
    print("Number of matching Entries: ", matching_count)

def query_duration(a):
    specific_duration_entries = entries_collection.find({'duration': {'$gte': a}})
    for entry in specific_duration_entries:
        print(entry)
 
#r = print_entries()
#u = update_entry() 
q1 = query_content('piano')
q2 = query_duration(40)


