from insertor import insert_geojson_data


db_config = {
    "dbname": "marchan_database",
    "user": "votana",
    "password": "votana",
    "host": "localhost"
}

insert_geojson_data(db_config, "province_kh", "transformed_province.geojson")
insert_geojson_data(db_config, "district_kh", "transformed_district.geojson")
