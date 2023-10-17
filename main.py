# from flask import Flask, request, jsonify
# import pickle
# import numpy as np

# app = Flask(__name__)

# with open('random_forest_model.pkl', 'rb') as model:
#     live_model_pred = pickle.load(model)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = {
#             "latitude": 52.52,
#             "longitude": 13.419998,
#             "generationtime_ms": 0.5970001220703125,
#             "utc_offset_seconds": 0,
#             "timezone": "GMT",
#             "timezone_abbreviation": "GMT",
#             "elevation": 38.0,
#             "current_weather": {
#                 "temperature": 17.1,
#                 "windspeed": 3.6,
#                 "winddirection": 127,
#                 "weathercode": 1,
#                 "is_day": 1,
#                 "time": "2023-09-24T16:45"
#             },
#             "hourly_units": {
#                 "time": "iso8601",
#                 "temperature_2m": "°C",
#                 "relativehumidity_2m": "%",
#                 "snowfall": "cm",
#                 "cloudcover_mid": "%",
#                 "windspeed_10m": "km/h",
#                 "windspeed_120m": "km/h",
#                 "winddirection_10m": "°",
#                 "winddirection_120m": "°"
#             },
#             "hourly": {
#                 "time": [
#                     # Your time data here...
#                 ],
#                 "temperature_2m": [
#                     # Your temperature data here...
#                 ],
#                 "relativehumidity_2m": [
#                     # Your relative humidity data here...
#                 ],
#                 "snowfall": [
#                     # Your snowfall data here...
#                 ],
#                 "cloudcover_mid": [
#                     # Your cloud cover data here...
#                 ],
#                 "windspeed_10m": [
#                     # Your windspeed at 10m data here...
#                 ],
#                 "windspeed_120m": [
#                     # Your windspeed at 120m data here...
#                 ],
#                 "winddirection_10m": [
#                     # Your wind direction at 10m data here...
#                 ],
#                 "winddirection_120m": [
#                     # Your wind direction at 120m data here...
#                 ]
#             }
#         }
#         latitude = data['latitude']
#         longitude = data['longitude']
#         generation_time_ms = data['generationtime_ms']
#         utc_offset_seconds = data['utc_offset_seconds']
#         timezone = data['timezone']
#         elevation = data['elevation']

#         hourly_data = data['hourly']

#         temperature_2m = hourly_data['temperature_2m']
#         relativehumidity_2m = hourly_data['relativehumidity_2m']
#         snowfall = hourly_data['snowfall']
#         cloudcover_mid = hourly_data['cloudcover_mid']
#         windspeed_10m = hourly_data['windspeed_10m']
#         windspeed_120m = hourly_data['windspeed_120m']
#         winddirection_10m = hourly_data['winddirection_10m']
#         winddirection_120m = hourly_data['winddirection_120m']

#         features = (
#             temperature_2m + relativehumidity_2m + snowfall +
#             cloudcover_mid + windspeed_10m + windspeed_120m +
#             winddirection_10m + winddirection_120m
#         )

#         prediction = live_model_pred.predict([features])

#         response = {
#             'prediction': prediction.tolist()
#         }

#         return jsonify(response)

#     except Exception as e:
#         error_message = str(e)
#         response = {
#             'error': error_message
#         }
#         return jsonify(response), 400  # Return a 400 status code for bad requests

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main':
    app.run()
