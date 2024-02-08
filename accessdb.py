from pymongo import MongoClient
from bson.objectid import ObjectId
import re
import logging
import time
from datetime import datetime, timedelta
import random

# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['diary']
entries_collection = db['entries']


logging.basicConfig(filename='query_performance.log', level=logging.INFO)




# Functions
# Retrieve all entries
def print_entries():
    entries = entries_collection.find()
    count = entries_collection.count_documents({})
    #count = entries_collection.count_documents(entries)


    # Iterate through the entries
    for entry in entries:
        print(entry)
    print("Number of Entries: " , count )


def update_entry():
    query = {"_id": ObjectId('65c222e7a615df32f31f6ea1') }
    change_to = {"$set": { "content": "update is working" }}
    entries_collection.update_one(query, change_to)

    id = {"_id": ObjectId('65c222e7a615df32f31f6ea1') }
    entries = entries_collection.find(id)
    for entry in entries:
        print(entry)


def query_content(a):
    start_time = time.time()
    query = {'content': {'$regex': re.compile(a, re.IGNORECASE)}}
    specific_content_entries = entries_collection.find(query)
    matching_count = entries_collection.count_documents(query)
    for entry in specific_content_entries:
        print(entry)
    print("Number of matching Entries: ", matching_count)
    end_time = time.time()
    logging.info(f"Execution time perform find query /: {end_time - start_time} seconds")

def query_duration(a):
    specific_duration_entries = entries_collection.find({'duration': {'$gte': a}})
    for entry in specific_duration_entries:
        print(entry)

def query_indexing():
    indexes = entries_collection.list_indexes()
    for index in indexes:
        print(index)
 
def drop_indexing():
    # Drop the index on the 'timestamp' field
    entries_collection.drop_index('timestamp_1')

    # Drop the index on the 'duration' field
    entries_collection.drop_index('duration_1')



def create_entry():
    start_time = time.time()

    timestamp = datetime.now()
    random_content = ['build app','Played the piano','Cooked dinner','build sandcastle','baked cake','read a book','wrote my diary','asked for vaccation']
    random_duration = ['15','67','23','30','20','80', '78','25']
    
    n = 1000


    for entry in range(1,n,1):
        a = random.choice(random_content)
        b = random.choice(random_duration)
        entry = {'content': a, 'duration': b, 'timestamp': timestamp}
        result = entries_collection.insert_one(entry)

    end_time = time.time()
    logging.info(f"Execution time for create {n} Entries /: {end_time - start_time} seconds")


#cr = create_entry()


#r = print_entries()
#u = update_entry() 
q1 = query_content('piano')
#q2 = query_duration(40)
#d1 = drop_indexing()
i1 = query_indexing()
