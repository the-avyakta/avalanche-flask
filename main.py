from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('random_forest_model.pkl', 'rb') as model:
    live_model_pred = pickle.load(model)

@app.route('/', methods=['POST'])
def predict():
    try:
        # data = request.json

        data= {
            {"latitude":52.52,"longitude":13.419998,"generationtime_ms":0.5970001220703125,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":38.0,"current_weather":{"temperature":17.1,"windspeed":3.6,"winddirection":127,"weathercode":1,"is_day":1,"time":"2023-09-24T16:45"},"hourly_units":{"time":"iso8601","temperature_2m":"°C","relativehumidity_2m":"%","snowfall":"cm","cloudcover_mid":"%","windspeed_10m":"km/h","windspeed_120m":"km/h","winddirection_10m":"°","winddirection_120m":"°"},"hourly":{"time":["2023-09-24T00:00","2023-09-24T01:00","2023-09-24T02:00","2023-09-24T03:00","2023-09-24T04:00","2023-09-24T05:00","2023-09-24T06:00","2023-09-24T07:00","2023-09-24T08:00","2023-09-24T09:00","2023-09-24T10:00","2023-09-24T11:00","2023-09-24T12:00","2023-09-24T13:00","2023-09-24T14:00","2023-09-24T15:00","2023-09-24T16:00","2023-09-24T17:00","2023-09-24T18:00","2023-09-24T19:00","2023-09-24T20:00","2023-09-24T21:00","2023-09-24T22:00","2023-09-24T23:00","2023-09-25T00:00","2023-09-25T01:00","2023-09-25T02:00","2023-09-25T03:00","2023-09-25T04:00","2023-09-25T05:00","2023-09-25T06:00","2023-09-25T07:00","2023-09-25T08:00","2023-09-25T09:00","2023-09-25T10:00","2023-09-25T11:00","2023-09-25T12:00","2023-09-25T13:00","2023-09-25T14:00","2023-09-25T15:00","2023-09-25T16:00","2023-09-25T17:00","2023-09-25T18:00","2023-09-25T19:00","2023-09-25T20:00","2023-09-25T21:00","2023-09-25T22:00","2023-09-25T23:00","2023-09-26T00:00","2023-09-26T01:00","2023-09-26T02:00","2023-09-26T03:00","2023-09-26T04:00","2023-09-26T05:00","2023-09-26T06:00","2023-09-26T07:00","2023-09-26T08:00","2023-09-26T09:00","2023-09-26T10:00","2023-09-26T11:00","2023-09-26T12:00","2023-09-26T13:00","2023-09-26T14:00","2023-09-26T15:00","2023-09-26T16:00","2023-09-26T17:00","2023-09-26T18:00","2023-09-26T19:00","2023-09-26T20:00","2023-09-26T21:00","2023-09-26T22:00","2023-09-26T23:00","2023-09-27T00:00","2023-09-27T01:00","2023-09-27T02:00","2023-09-27T03:00","2023-09-27T04:00","2023-09-27T05:00","2023-09-27T06:00","2023-09-27T07:00","2023-09-27T08:00","2023-09-27T09:00","2023-09-27T10:00","2023-09-27T11:00","2023-09-27T12:00","2023-09-27T13:00","2023-09-27T14:00","2023-09-27T15:00","2023-09-27T16:00","2023-09-27T17:00","2023-09-27T18:00","2023-09-27T19:00","2023-09-27T20:00","2023-09-27T21:00","2023-09-27T22:00","2023-09-27T23:00","2023-09-28T00:00","2023-09-28T01:00","2023-09-28T02:00","2023-09-28T03:00","2023-09-28T04:00","2023-09-28T05:00","2023-09-28T06:00","2023-09-28T07:00","2023-09-28T08:00","2023-09-28T09:00","2023-09-28T10:00","2023-09-28T11:00","2023-09-28T12:00","2023-09-28T13:00","2023-09-28T14:00","2023-09-28T15:00","2023-09-28T16:00","2023-09-28T17:00","2023-09-28T18:00","2023-09-28T19:00","2023-09-28T20:00","2023-09-28T21:00","2023-09-28T22:00","2023-09-28T23:00","2023-09-29T00:00","2023-09-29T01:00","2023-09-29T02:00","2023-09-29T03:00","2023-09-29T04:00","2023-09-29T05:00","2023-09-29T06:00","2023-09-29T07:00","2023-09-29T08:00","2023-09-29T09:00","2023-09-29T10:00","2023-09-29T11:00","2023-09-29T12:00","2023-09-29T13:00","2023-09-29T14:00","2023-09-29T15:00","2023-09-29T16:00","2023-09-29T17:00","2023-09-29T18:00","2023-09-29T19:00","2023-09-29T20:00","2023-09-29T21:00","2023-09-29T22:00","2023-09-29T23:00","2023-09-30T00:00","2023-09-30T01:00","2023-09-30T02:00","2023-09-30T03:00","2023-09-30T04:00","2023-09-30T05:00","2023-09-30T06:00","2023-09-30T07:00","2023-09-30T08:00","2023-09-30T09:00","2023-09-30T10:00","2023-09-30T11:00","2023-09-30T12:00","2023-09-30T13:00","2023-09-30T14:00","2023-09-30T15:00","2023-09-30T16:00","2023-09-30T17:00","2023-09-30T18:00","2023-09-30T19:00","2023-09-30T20:00","2023-09-30T21:00","2023-09-30T22:00","2023-09-30T23:00"],"temperature_2m":[11.6,11.2,10.8,10.6,10.5,10.7,12.0,13.0,13.6,14.5,16.0,17.2,18.3,18.8,18.8,18.8,18.1,16.8,15.3,13.9,13.0,12.3,11.7,11.2,10.8,10.2,9.8,9.7,9.5,9.4,9.7,11.5,13.9,16.0,17.7,19.2,20.0,20.3,20.5,20.2,19.5,18.0,16.7,15.6,14.8,14.4,14.0,13.7,13.4,13.1,12.8,12.5,12.3,12.1,12.4,13.9,15.8,17.7,19.8,21.4,22.6,23.2,23.5,23.5,23.0,21.8,20.9,20.3,19.7,18.9,18.2,17.5,17.1,16.8,16.7,16.8,16.6,16.3,16.3,17.4,19.0,20.6,21.9,23.1,24.0,24.8,25.1,24.9,24.4,23.1,21.5,20.7,20.0,19.4,18.7,18.1,17.5,17.0,16.6,16.3,16.1,16.0,16.2,16.8,17.9,19.0,20.3,21.7,22.9,23.5,23.9,23.9,23.3,22.5,21.6,20.8,20.1,19.4,18.9,18.5,18.1,17.6,17.0,16.6,16.4,16.3,16.4,16.8,17.3,17.7,17.8,17.7,17.7,17.7,17.5,17.4,17.3,17.1,17.0,16.8,16.5,16.1,15.6,14.9,14.4,14.0,13.7,13.5,13.6,13.9,14.2,14.7,15.3,16.0,16.7,17.5,18.0,18.3,18.3,18.0,17.2,16.0,14.9,14.1,13.4,12.8,12.2,11.6],"relativehumidity_2m":[85,87,89,93,95,95,94,87,84,76,69,63,55,51,50,48,54,64,70,79,85,86,86,85,86,88,91,94,95,95,93,85,75,65,60,55,53,53,53,55,60,70,77,83,88,91,93,94,95,95,96,96,96,97,97,92,85,79,73,67,64,62,61,62,64,71,77,80,83,87,91,94,94,95,95,95,95,95,96,92,84,78,72,65,63,59,52,55,58,65,72,77,81,85,87,88,89,90,90,90,90,91,89,85,79,73,67,61,57,56,56,58,62,68,73,75,75,75,76,78,80,82,85,87,88,88,88,86,84,83,85,89,92,90,91,92,93,94,94,93,92,91,92,94,95,96,97,97,97,96,94,90,85,80,74,67,62,58,55,55,59,65,71,75,78,81,84,87],"snowfall":[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],"cloudcover_mid":[0,27,32,34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17,33,50,49,49,48,55,61,68,79,89,100,100,100,100,93,85,78,68,58,48,32,16,0,33,66,99,98,97,96,97,99,100,100,100,100,100,100,100,97,93,90,82,74,66,57,48,39,45,50,56,57,58,59,58,57,56,37,19,0,8,16,24,16,8,0,0,0,0,0,0],"windspeed_10m":[6.0,5.9,5.4,5.5,5.4,5.8,7.8,6.9,6.9,4.3,5.1,3.4,2.9,2.4,3.2,2.9,5.8,3.2,5.2,6.8,5.3,5.5,5.8,6.3,6.4,5.6,6.1,6.3,6.0,5.5,6.5,6.7,8.4,8.4,8.4,9.0,9.0,7.0,7.9,9.4,7.1,4.3,4.4,5.0,5.4,4.8,3.4,3.6,4.7,3.6,4.3,4.7,4.7,4.1,4.7,6.4,6.5,6.3,6.1,6.2,8.9,9.0,9.3,8.9,8.7,6.3,7.0,7.3,6.9,6.7,6.6,6.1,4.8,3.3,2.3,2.0,2.6,2.5,2.3,2.8,3.2,2.5,2.2,0.5,3.3,2.3,4.1,4.3,2.6,4.0,5.0,5.5,6.0,6.4,6.6,6.9,7.0,6.6,6.4,6.2,6.5,6.4,6.6,6.5,6.7,6.9,6.7,6.4,6.1,6.4,6.9,6.6,5.1,3.4,2.5,2.6,2.8,2.5,1.6,1.3,2.5,3.3,3.6,3.7,3.4,3.4,3.1,2.6,2.3,2.6,2.4,1.8,1.8,4.0,3.3,2.5,0.5,2.8,4.8,6.0,7.1,8.0,8.3,8.0,7.2,6.5,5.5,5.2,5.9,7.2,8.3,8.8,9.0,9.2,9.8,10.9,11.4,11.4,10.9,10.3,8.8,7.2,6.1,6.1,6.1,6.2,5.5,4.5],"windspeed_120m":[24.1,24.5,22.0,19.9,19.4,20.3,11.1,11.1,9.5,5.6,6.6,4.2,3.7,2.7,3.6,6.5,10.0,8.2,16.9,20.9,17.6,18.2,21.4,22.1,22.7,21.1,22.4,22.9,25.1,25.0,25.4,24.0,13.2,14.1,14.4,12.8,11.9,11.8,10.9,11.5,14.8,16.4,16.6,15.8,14.8,14.8,14.6,12.8,13.7,9.8,6.4,8.2,11.5,16.0,18.2,16.6,8.2,7.3,7.6,9.0,10.9,15.3,16.2,19.6,21.1,23.5,27.4,30.9,28.6,29.0,28.4,26.7,23.7,19.6,14.6,11.5,8.9,6.6,5.5,4.4,6.0,3.0,2.5,0.5,4.8,3.3,6.0,7.1,6.1,10.9,20.5,23.2,25.4,27.6,28.9,29.7,30.1,30.1,29.5,29.7,30.9,32.3,31.8,26.5,19.0,13.2,10.8,9.9,10.2,11.2,13.2,13.8,12.3,10.7,10.2,11.0,12.8,13.0,8.9,4.0,6.8,10.3,13.5,15.1,14.5,13.0,11.7,9.1,6.0,4.4,4.3,5.0,5.5,6.8,6.8,6.1,3.3,6.2,11.4,16.2,21.1,24.9,25.6,24.6,23.6,23.4,23.2,23.1,23.5,24.1,24.1,22.5,19.8,18.3,18.7,20.0,21.1,21.4,21.3,21.7,22.9,24.6,25.9,27.1,28.4,28.7,27.1,24.1],"winddirection_10m":[245,259,262,259,250,266,292,298,309,318,309,328,30,63,90,120,158,117,106,115,118,113,112,114,117,117,118,121,123,122,124,126,130,137,140,157,151,145,129,133,135,138,125,111,110,117,108,90,99,84,95,99,90,75,90,106,109,114,118,111,137,151,144,117,128,114,102,110,118,126,131,135,138,139,141,135,124,135,141,130,153,172,270,225,131,162,165,156,146,95,111,113,123,128,135,141,145,151,153,159,161,164,167,180,196,208,216,223,225,227,223,225,231,252,278,304,310,315,297,214,188,186,186,191,198,212,216,196,162,146,153,169,191,207,186,172,225,320,318,303,285,275,275,275,276,270,259,254,259,267,275,279,286,291,294,297,298,298,297,295,289,276,267,267,273,280,281,284],"winddirection_120m":[261,270,275,274,269,277,295,299,307,315,311,329,29,67,90,124,159,142,124,132,133,129,131,134,138,143,143,143,145,147,142,140,135,142,158,169,166,157,153,139,137,147,156,153,139,139,147,148,150,152,137,113,104,113,117,114,105,101,95,90,99,150,143,148,133,126,115,122,132,145,156,164,166,174,189,212,207,221,203,171,163,166,262,225,132,167,163,156,152,117,124,132,142,151,157,163,168,174,180,186,192,197,200,202,205,209,217,224,228,228,225,227,238,258,280,302,320,326,320,270,212,209,214,218,228,242,252,252,237,215,204,201,203,198,183,180,221,291,298,291,284,280,281,282,282,280,276,274,276,280,284,286,289,292,295,298,300,299,298,297,292,288,286,289,294,298,303,309]}}
        }
        latitude = data['latitude']
        longitude = data['longitude']
        generation_time_ms = data['generationtime_ms']
        utc_offset_seconds = data['utc_offset_seconds']
        timezone = data['timezone']
        elevation = data['elevation']
        
        hourly_data = data['hourly']
        
        temperature_2m = hourly_data['temperature_2m']
        relativehumidity_2m = hourly_data['relativehumidity_2m']
        snowfall = hourly_data['snowfall']
        cloudcover_mid = hourly_data['cloudcover_mid']
        windspeed_10m = hourly_data['windspeed_10m']
        windspeed_120m = hourly_data['windspeed_120m']
        winddirection_10m = hourly_data['winddirection_10m']
        winddirection_120m = hourly_data['winddirection_120m']

        features = (
            temperature_2m + relativehumidity_2m + snowfall + 
            cloudcover_mid + windspeed_10m + windspeed_120m + 
            winddirection_10m + winddirection_120m
        )

        prediction = live_model_pred.predict([features])

    
        response = {
            'prediction': prediction.tolist() 
        }
        
        return jsonify(response)

    except Exception as e:
        error_message = str(e)
        response = {
            'error': error_message
        }
        return jsonify(response), 400  # Return a 400 status code for bad requests

if __name__ == '__main__':
    app.run(debug=True)
