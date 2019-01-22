from flask import Flask, request, jsonify, redirect, render_template, send_from_directory
import requests
from flask_cors import CORS
import json
import xml.etree.ElementTree as ET

app = Flask(__name__,template_folder='.') 
CORS(app)
@app.route('/iss')
def iss():
    r =requests.get('http://api.open-notify.org/iss-now.json')

    return r.text

@app.route('/geocode')
def geocode():
    r =requests.get('http://api.geonames.org/extendedFindNearby?lat='+request.args.get('lat')+'&lng='+request.args.get('lng')+'&username=akshay745632199')
    print(r.text)
    return r.text

if __name__ == "__main__":
    app.run(port=5000)



def show(elem):
    print(elem.tag)
    gnl = []
    for child in elem.findall('*'):
        gnl.append(child)
    d = {}
    
    if len(gnl)==1:
        if gnl[0].tag == 'ocean':
            d['type']='ocean'
            d['name'] = gnl[0].find('name').text
        else:
            d['type']='unknown'
    else:
        
        d['type']='land'
        d['name'] = gnl[-1].find('name').text
        d['country']=gnl[-1].find('countryName').text
    return d

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('.', path)
@app.route('/combine')
def combine():
    r =requests.get('http://api.open-notify.org/iss-now.json')
    latlng = json.loads(r.text)
    lat, lng = latlng['iss_position']['latitude'], latlng['iss_position']['longitude']
    print(lat, lng)
    # r2 = requests.get('http://api.geonames.org/extendedFindNearby?lat='+lat+'&lng='+lng+'&username=akshay745632199')
    # print(r2.text)
    # tree = ET.fromstring(r2.text)
    temp = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <geonames>
    <geoname>
    <toponymName>Earth</toponymName>
    <name>Earth</name>
    <lat>0</lat>
    <lng>0</lng>
    <geonameId>6295630</geonameId>
    <countryCode/>
    <countryName/>
    <fcl>L</fcl>
    <fcode>AREA</fcode>
    </geoname>
    <geoname>
    <toponymName>Europe</toponymName>
    <name>Europe</name>
    <lat>48.69096</lat>
    <lng>9.14062</lng>
    <geonameId>6255148</geonameId>
    <countryCode/>
    <countryName/>
    <fcl>L</fcl>
    <fcode>CONT</fcode>
    </geoname>
    <geoname>
    <toponymName>Switzerland</toponymName>
    <name>Switzerland</name>
    <lat>47.00016</lat>
    <lng>8.01427</lng>
    <geonameId>2658434</geonameId>
    <countryCode>CH</countryCode>
    <countryName>Switzerland</countryName>
    <fcl>A</fcl>
    <fcode>PCLI</fcode>
    </geoname>
    <geoname>
    <toponymName>Kanton St. Gallen</toponymName>
    <name>Saint Gallen</name>
    <lat>47.25</lat>
    <lng>9.25</lng>
    <geonameId>2658821</geonameId>
    <countryCode>CH</countryCode>
    <countryName>Switzerland</countryName>
    <fcl>A</fcl>
    <fcode>ADM1</fcode>
    </geoname>
    <geoname>
    <toponymName>Wahlkreis Toggenburg</toponymName>
    <name>Wahlkreis Toggenburg</name>
    <lat>47.29453</lat>
    <lng>9.17283</lng>
    <geonameId>7285001</geonameId>
    <countryCode>CH</countryCode>
    <countryName>Switzerland</countryName>
    <fcl>A</fcl>
    <fcode>ADM2</fcode>
    </geoname>
    <geoname>
    <toponymName>Mosnang</toponymName>
    <name>Mosnang</name>
    <lat>47.35008</lat>
    <lng>9.00901</lng>
    <geonameId>7286562</geonameId>
    <countryCode>CH</countryCode>
    <countryName>Switzerland</countryName>
    <fcl>A</fcl>
    <fcode>ADM3</fcode>
    </geoname>
    <geoname>
    <toponymName>Atzmännig</toponymName>
    <name>Atzmännig</name>
    <lat>47.2854</lat>
    <lng>8.99704</lng>
    <geonameId>6559633</geonameId>
    <countryCode>CH</countryCode>
    <countryName>Switzerland</countryName>
    <fcl>P</fcl>
    <fcode>PPL</fcode>
    </geoname>
    <geoname>
    <toponymName>Chrüzegg</toponymName>
    <name>Chrüzegg</name>
    <lat>47.2985</lat>
    <lng>9.01488</lng>
    <geonameId>7910950</geonameId>
    <countryCode>CH</countryCode>
    <countryName>Switzerland</countryName>
    <fcl>P</fcl>
    <fcode>PPLX</fcode>
    </geoname>
    </geonames>
    '''
    tree = ET.fromstring(temp)
    
    d = show(tree)
    
    d['lat'] = lat
    d['lng'] = lng

    print(d)
    return jsonify(d)

