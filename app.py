from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime, timedelta
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Configuration
#client = MongoClient('mongodb://mongodb:27017/')
client = MongoClient('mongodb://localhost:27017/')
db = client['diary']
entries_collection = db['entries']


# Function to create a new entry
def create_entry( content, duration):
    timestamp = datetime.now()
    entry = {'content': content, 'duration': duration, 'timestamp': timestamp}
    result = entries_collection.insert_one(entry)
    return result.inserted_id

# Function to retrieve all entries
def get_all_entries():
    entries = entries_collection.find().sort('timestamp', -1)
    return entries

# Function to retrieve a specific entry by ID
def get_entry_by_id(entry_id):
    entry = entries_collection.find_one({'_id': ObjectId(entry_id)})
    return entry

# Function to update a specific entry by ID
def update_entry(entry_id, content, duration):
    timestamp = datetime.now()
    result = entries_collection.update_one(
        {'_id': ObjectId(entry_id)},
        {'$set': {'content': content, 'duration': duration, 'timestamp': timestamp}}
    )
    return result.modified_count > 0

# Function to delete a specific entry by ID
def delete_entry(entry_id):
    result = entries_collection.delete_one({'_id': ObjectId(entry_id)})
    return result.deleted_count > 0




# Routes
@app.route('/')
def index():
    entries = get_all_entries()
    return render_template('index.html', entries=entries)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    content = request.form.get('content')
    duration = request.form.get('duration')
    entry_id = create_entry(content, duration)
    return redirect(url_for('index'))

@app.route('/edit_entry/<entry_id>')
def edit_entry(entry_id):
    entry = get_entry_by_id(entry_id)
    return render_template('edit.html', entry=entry)

@app.route('/update_entry/<entry_id>', methods=['POST'])
def update_entry_route(entry_id):
    content = request.form.get('content')
    duration = request.form.get('duration')
    if update_entry(entry_id, content, duration):
        return redirect(url_for('index'))
    else:
        return "Failed to update entry."

@app.route('/delete_entry/<entry_id>')
def delete_entry_route(entry_id):
    if delete_entry(entry_id):
        return redirect(url_for('index'))
    else:
        return "Failed to delete entry."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



# @app.route('/')
# def index():
    
    
#     today = datetime.combine(datetime.utcnow().date(), datetime.min.time())
#     end_of_day = today + timedelta(days=1)

#  #   entries = entries_collection.find().sort('timestamp', -1)
#     entries = entries_collection.find({
#     'timestamp': {'$gte': today, '$lt': end_of_day}
#     })
#     return render_template('index.html', entries=entries)

# # @app.route('/add_entry', methods=['POST'])
# # def add_entry():
# #     content = request.form.get('content')
# #     timestamp = datetime.now()
# #     entry = {'content': content, 'timestamp': timestamp}
# #     entries_collection.insert_one(entry)
# #     return redirect(url_for('index'))


# @app.route('/add_entry', methods=['POST'])
# def add_entry():
#     content = request.form.get('content')
#     duration = request.form.get('duration')  # Added line to retrieve duration
#     timestamp = datetime.now()
    
#     # Save the entry to MongoDB
#     entry = {'content': content, 'duration': duration, 'timestamp': timestamp}
#     entries_collection.insert_one(entry)

#     return redirect(url_for('index'))

