from flask import Flask, render_template, request
import requests

app = Flask(__name__)
def get_weather(latitude, longitude):
    api_key = 'TayRKLn0trnH8tOQrucqkQsiT4kQSOGQ'  # Your API key
    url = f'https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    print(data)  # Print API response data for debugging
    if response.status_code == 200:
        weather = {
            'latitude': latitude,
            'longitude': longitude,
            'temperature': data['data']['timelines'][0]['intervals'][0]['values']['temperature'],
            'description': data['data']['timelines'][0]['intervals'][0]['values']['weatherCode'],
            # Add more weather data as needed
        }
        print(weather)  # Print weather data for debugging
        return weather
    else:
        print(f'Error: {response.status_code}')
        return None


# def get_weather(latitude, longitude):
#     api_key = 'TayRKLn0trnH8tOQrucqkQsiT4kQSOGQ'  # Your API key
#     url = f'https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={api_key}'
#     response = requests.get(url)
#     data = response.json()
#     if response.status_code == 200:
#         weather = {
#             'latitude': latitude,
#             'longitude': longitude,
#             'temperature': data['data']['timelines'][0]['intervals'][0]['values']['temperature'],
#             'description': data['data']['timelines'][0]['intervals'][0]['values']['weatherCode'],
#             # Add more weather data as needed
#         }
#         return weather
#     else:
#         return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST' and 'latitude' in request.form and 'longitude' in request.form:
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        weather = get_weather(latitude, longitude)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
