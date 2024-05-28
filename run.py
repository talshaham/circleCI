from flask import Flask, render_template, request
from backend_weather import retrieving_weather_data_api

app = Flask(__name__)  # import instance from class Flask


@app.route("/", methods=['POST', 'GET'])  # decorating hello function in the HTML route
def home():
    if request.method == 'POST':
        location = request.form["location"]  # go to html and request argument name location
        weather_data = retrieving_weather_data_api(location)
        if not weather_data:
            return render_template("error.html")
        return render_template("weather.html", days_list=weather_data, location=location)  # sending argument  to html file
    return render_template("weather.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

# request is for requests: GET, POST
# render_template - allowing me to render html content to the browser
# flask & jinja allowing to write html code inside pycharm
