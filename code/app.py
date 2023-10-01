from pydoc import doc
from flask import Flask, jsonify
import json
from pymongo import MongoClient
from flask_cors import CORS


#mongodb
mongo = MongoClient(port=27017) 
db = mongo.met
healthandgreenspacedata = db['healthandgreenspacedata']

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

@app.route("/api/health-green-data")
def health_green_data():
    cursor = healthandgreenspacedata.find({})
    documents ={}
    pymongo_cursor = db.healthandgreenspacedata.find({}, {'_id': False})
    all_data = list(pymongo_cursor)
    print(all_data)
    documents['data'] = all_data
    documents = jsonify(documents)
    return(documents)

if __name__ == "__main__":
    app.run(debug=True)