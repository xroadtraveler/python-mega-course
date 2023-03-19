from flask import Flask, render_template, request, send_file
import pandas as pd
from werkzeug.utils import secure_filename
from geopy.geocoders import ArcGIS 


app=Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']

        if file:
            df = pd.read_csv(file)
            if 'address' in df.columns:
                address_col = 'address'
            elif 'Address' in df.columns:
                address_col = 'Address'
            else:
                return 'Error: Please make sure you have an address column in your CSV file!'
            geolocator = ArcGIS(user_agent='my_app')
            df["Coordinates"]=df[address_col].apply(geolocator.geocode)
            df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
            df["Longitude"]=df["Coordinates"].apply(lambda y: y.longitude if y != None else None)
            df.to_csv('Lat-Long_Address.csv', index=False)
            return df.to_json(orient='records')
        else:
            'No file selected'

    return render_template("index.html")


@app.route("/downoad")
def download():
    return send_file("Lat-Long_Address.csv", as_attachment=True)



if __name__ == '__main__':
    app.debug=True
    app.run()