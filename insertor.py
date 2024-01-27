import json
import psycopg2
from psycopg2 import extras

def insert_geojson_data(db_config, table_name, geojson_file):

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    with open(geojson_file, 'r') as file:
        data = json.load(file)

    sql = f"""
    INSERT INTO {table_name} (
        objectid, level, hrname, hrpcode, hrparent, com_name, com_code, dis_code, pro_code, geom
    ) VALUES %s;
    """

    insert_list = [
        (
            feature['properties'].get('OBJECTID'),
            feature['properties'].get('Level'),
            feature['properties'].get('HRName'),
            feature['properties'].get('HRPCode'),
            feature['properties'].get('HRParent'),
            feature['properties'].get('COM_NAME'),
            feature['properties'].get('COM_CODE'),
            feature['properties'].get('DIS_CODE'),
            feature['properties'].get('PRO_CODE'),
            json.dumps(feature['geometry'])  
        )
        for feature in data['features']
    ]

    extras.execute_values(
        cursor, sql, insert_list, template=None, page_size=100
    )

    conn.commit()
    cursor.close()
    conn.close()

db_config = {
    "dbname": "marchan_database",
    "user": "votana",
    "password": "votana",
    "host": "localhost"
}

