from flask import Flask, render_template, request
from backend_weather import retrieving_weather_data_api
from pymongo import MongoClient
import os

app = Flask(__name__)

# Retrieve MongoDB URI components from environment variables
mongo_username = os.getenv('MONGODB_USERNAME', 'root')
mongo_password = os.getenv('MONGODB_PASSWORD', 'password')
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = os.getenv('MONGO_PORT', '27017')

# Construct the MongoDB URI
# mongo_uri = f'mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/'
client = MongoClient(f'mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/')
# client = MongoClient(mongo_uri)


# Access your MongoDB database and collection
db = client['weather_history']
collection = db['searches']

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        location = request.form["location"]
        weather_data = retrieving_weather_data_api(location)
        if not weather_data:
            return render_template("error.html")

        # Save search to MongoDB
        # search_record = {"location": location, "weather_data": weather_data}
        db.searches.insert_one({"location": location, "weather_data": weather_data})
        
        return render_template("weather.html", days_list=weather_data, location=location)

    return render_template("weather.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
