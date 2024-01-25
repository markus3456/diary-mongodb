from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient('mongodb://mongodb:27017/')
db = client['diary']
entries_collection = db['entries']

# Routes
@app.route('/')
def index():
    entries = entries_collection.find().sort('timestamp', -1)
    return render_template('index.html', entries=entries)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    content = request.form.get('content')
    timestamp = datetime.now()
    entry = {'content': content, 'timestamp': timestamp}
    entries_collection.insert_one(entry)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)