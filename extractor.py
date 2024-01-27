import psycopg2
import json

def fetch_geojson_data(db_config, table_name):

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT objectid, level, hrname, hrpcode, hrparent, com_name, com_code, dis_code, pro_code, ST_AsGeoJSON(geom)::json FROM {table_name};"
    cursor.execute(sql)
    rows = cursor.fetchall()

    features = []
    for row in rows:
        feature = {
            "type": "Feature",
            "properties": {
                "OBJECTID": row[0],
                "Level": row[1],
                "HRName": row[2],
                "HRPCode": row[3],
                "HRParent": row[4],
                "COM_NAME": row[5],
                "COM_CODE": row[6],
                "DIS_CODE": row[7],
                "PRO_CODE": row[8],
            },
            "geometry": row[9]
        }
        features.append(feature)
    

    print(feature)

    cursor.close()
    conn.close()


db_config = {
    "dbname": "marchan_database",
    "user": "votana",
    "password": "votana",
    "host": "localhost"
}

#fetch_geojson_data(db_config, "province_kh")
