import datetime 
from checker import get_commune_from_geo,  get_district_from_geo, get_province_from_geo
import pandas as pd 


df = pd.read_csv("dataset/marchant_dataset.csv", low_memory=False)

db_config = {
    "dbname": "marchan_database",
    "user": "votana",
    "password": "votana",
    "host": "localhost"
}


start = datetime.datetime.now()
print("Start time:", datetime.datetime.now())

commune = get_commune_from_geo(df, db_config, "commune_kh")
district = get_district_from_geo(df, db_config, "district_kh")
province = get_province_from_geo(df, db_config, "province_kh")


end = datetime.datetime.now()
print("End time:", end)
print("Duration:", end - start)

commune.to_csv('dataset/commune.csv')
district.to_csv('dataset/district.csv')
province.to_csv('dataset/province.csv')