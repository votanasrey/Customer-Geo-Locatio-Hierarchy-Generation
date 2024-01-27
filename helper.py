import os
import hashlib
import hmac
import requests
from dotenv import load_dotenv
import datetime
from shapely.geometry import shape, Point, MultiPolygon, Polygon
import json

def generate_hash():

        API_SECRET = os.environ.get("API_SECRET")
        API_KEY = os.environ.get("API_KEY")
        now = datetime.datetime.now()
        x_reqtime = int(now.timestamp())

        API_SECRET = bytes(API_SECRET, 'utf-8')
        message = bytes(API_KEY + str(x_reqtime), 'utf-8')
        generated_hash = hmac.new(API_SECRET, message, hashlib.sha256).hexdigest()
        print(generated_hash)
        return generated_hash

def get_commune_name(longitude, latitude):
    with open('transformed_commune.geojson', 'r') as f:
        geojson_data = json.load(f)    

    point = Point([longitude, latitude])       

    for feature in geojson_data['features']:
        geometry = feature['geometry']
        properties = feature['properties']    
    
        multipolygon = shape(geometry)
        if point.within(multipolygon):
            data = properties['HRName']    

            return data
    return None

def get_district_name(longitude, latitude):
    with open('transformed_district.geojson', 'r') as f:
        geojson_data = json.load(f)    

    point = Point([longitude, latitude])       

    for feature in geojson_data['features']:
        geometry = feature['geometry']
        properties = feature['properties']    
    
        multipolygon = shape(geometry)
        if point.within(multipolygon):
            data = properties['HRName']    

            return data
    return None

def get_province_name(longitude, latitude):
    with open('transformed_province.geojson', 'r') as f:
        geojson_data = json.load(f)    

    point = Point([longitude, latitude])       

    for feature in geojson_data['features']:
        geometry = feature['geometry']
        properties = feature['properties']    
    
        multipolygon = shape(geometry)
        if point.within(multipolygon):
            data = properties['HRName']    

            return data
    return None

def main(longitude, latitude): 
    commune = get_commune_name(longitude, latitude)
    district = get_district_name(longitude, latitude)
    province = get_province_name(longitude, latitude)
    return commune, district, province

def get_geo_location(longitude: float, latitude: float, file_name: str):

    with open(f'{file_name}', 'r') as f:
        geojson_data = json.load(f)    

    point = Point([longitude, latitude])  
    
    for feature in geojson_data['features']:
        geometry = feature['geometry']
        properties = feature['properties']    
    
        multipolygon = shape(geometry)
        if point.within(multipolygon):
            data = properties['HRName']   
            return data
    return None



def get_geolocation_name(longitude, latitude):

    geo_data = {'commune': {'file_name': 'transformed_commune.geojson'},
            'district': {'file_name': 'transformed_district.geojson'},
            'province': {'file_name': 'transformed_province.geojson'}} 
    for admin_level in geo_data:

        location = get_geo_location(longitude, latitude, geo_data[admin_level]['file_name'])
        geo_data[admin_level]['location'] = location

    
    output = {'commune': geo_data['commune']['location'],
              'district': geo_data['district']['location'],
              'province': geo_data['province']['location']}
    return output

