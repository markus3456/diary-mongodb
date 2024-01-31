from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime, timedelta

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient('mongodb://mongodb:27017/')
db = client['diary']
entries_collection = db['entries']

# Routes
@app.route('/')
def index():
    
    
    today = datetime.combine(datetime.utcnow().date(), datetime.min.time())
    end_of_day = today + timedelta(days=1)

 #   entries = entries_collection.find().sort('timestamp', -1)
    entries = entries_collection.find({
    'timestamp': {'$gte': today, '$lt': end_of_day}
    })
    return render_template('index.html', entries=entries)

# @app.route('/add_entry', methods=['POST'])
# def add_entry():
#     content = request.form.get('content')
#     timestamp = datetime.now()
#     entry = {'content': content, 'timestamp': timestamp}
#     entries_collection.insert_one(entry)
#     return redirect(url_for('index'))


@app.route('/add_entry', methods=['POST'])
def add_entry():
    content = request.form.get('content')
    duration = request.form.get('duration')  # Added line to retrieve duration
    timestamp = datetime.now()
    
    # Save the entry to MongoDB
    entry = {'content': content, 'duration': duration, 'timestamp': timestamp}
    entries_collection.insert_one(entry)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)