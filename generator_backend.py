import os
import hashlib
import hmac
import requests
from dotenv import load_dotenv
import datetime
from requestor import api_requestor
import pandas as pd 
from helper import get_geolocation_name

def get_location_info(row):
    return get_geolocation_name(row['suggested_longitude'], row['suggested_latitude'])

print('##' * 50)
print("Loading the data .....")
print('##' * 50)

df = pd.read_csv('dataset/marchant_dataset.csv')

print('##' * 50)
print("Loaded the data .....")
print('##' * 50)


print('##' * 50)
print("Processing data .....")
print('##' * 50)

start = datetime.datetime.now()
print("Start time:", datetime.datetime.now())

df['location_info'] = df.apply(get_location_info, axis=1)

end = datetime.datetime.now()
print("End time:", end)
print("Duration:", end - start)

print('##' * 50)
print("DONE .....")
print('##' * 50)


print('##' * 50)
print("Saving data .....")
print('##' * 50)

df.to_csv('dataset/marchant_data_location_final.csv')

print('##' * 50)
print("DONE .....")
print('##' * 50)
