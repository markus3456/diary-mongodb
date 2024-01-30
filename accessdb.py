from pymongo import MongoClient

# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['diary']
entries_collection = db['entries']

# Retrieve all entries
entries = entries_collection.find()

# Iterate through the entries
for entry in entries:
    print(entry)