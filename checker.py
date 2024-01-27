import pandas as pd
import psycopg2
import datetime

def get_commune_from_geo(df, db_config, table_name):

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    df['commune_name'] = None

    for index, row in df.iterrows():
        lat, lon = row['suggested_latitude'], row['suggested_longitude']
        
        point_geom = f'ST_SetSRID(ST_Point({lon}, {lat}), 4326)'
        
        sql = f"""
        SELECT com_name
        FROM {table_name}
        WHERE ST_Contains(geom, {point_geom});
        """

        cursor.execute(sql)

        result = cursor.fetchone()

        if result:
            df.at[index, 'commune_name'] = result[0]

    cursor.close()
    conn.close()

    return df

def get_district_from_geo(df, db_config, table_name):

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    df['district_name'] = None

    for index, row in df.iterrows():
        lat, lon = row['suggested_latitude'], row['suggested_longitude']
        
        point_geom = f'ST_SetSRID(ST_Point({lon}, {lat}), 4326)'
        
        sql = f"""
        SELECT hrname
        FROM {table_name}
        WHERE ST_Contains(geom, {point_geom});
        """

        cursor.execute(sql)

        result = cursor.fetchone()

        if result:
            df.at[index, 'district_name'] = result[0]

    cursor.close()
    conn.close()

    return df


def get_province_from_geo(df, db_config, table_name):

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    df['province_name'] = None

    for index, row in df.iterrows():
        lat, lon = row['suggested_latitude'], row['suggested_longitude']
        
        point_geom = f'ST_SetSRID(ST_Point({lon}, {lat}), 4326)'
        
        sql = f"""
        SELECT hrname
        FROM {table_name}
        WHERE ST_Contains(geom, {point_geom});
        """

        cursor.execute(sql)

        result = cursor.fetchone()

        if result:
            df.at[index, 'province_name'] = result[0]

    cursor.close()
    conn.close()

    return df


