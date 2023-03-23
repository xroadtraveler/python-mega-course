from flask import Flask, render_template, request, send_file
import pandas as pd
from geopy.geocoders import ArcGIS
import datetime as dt


app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
    global filename
    if request.method == 'POST':
        # Get the file from the form
        file = request.files['file']
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file)

        # Check if the DataFrame has an "address" or "Address" column
        if 'address' in df.columns:
            address_col = 'address'
        elif 'Address' in df.columns:
            address_col = 'Address'
        else:
            return render_template("index.html", text="Please make sure you have an address column in your CSV file!")
                    
        # Geocode the addresses using the ArcGIS geocoder
        geolocator = ArcGIS()
        df["locations"]=df[address_col].apply(geolocator.geocode)

        # Extract the latitude and longitude from locations
        df["Latitude"]=df["locations"].apply(lambda x: x.latitude if x != None else None)
        df["Longitude"]=df["locations"].apply(lambda y: y.longitude if y != None else None)

        # Use datetime to generate unique filename for concurrent processing
        filename = dt.datetime.now().strftime("geocoded/%Y-%m-%d-%H-%M-%S-%f" + ".csv")

        # Sends to CSV
        df.to_csv(filename, index=None)

        # Render the updated DataFrame in the HTML table
        return render_template('index.html', text=df.to_html(), btn='download.html')
        
    else:
        return render_template('index.html')


@app.route("/downoad")
def download():
    return send_file(filename, download_name='yourfile.csv', as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)