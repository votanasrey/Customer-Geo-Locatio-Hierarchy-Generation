 CREATE TABLE commune_kh (
    id SERIAL PRIMARY KEY,
    objectid INTEGER,
    level DOUBLE PRECISION,
    hrname VARCHAR(255),
    hrpcode VARCHAR(20),
    hrparent VARCHAR(20),
    com_name VARCHAR(255),
    com_code INTEGER,
    dis_code INTEGER,
    pro_code INTEGER,
    geom GEOMETRY(MultiPolygon, 4326)
);

CREATE TABLE district_kh (
    id SERIAL PRIMARY KEY,
    objectid INTEGER,
    level DOUBLE PRECISION,
    hrname VARCHAR(255),
    hrpcode VARCHAR(20),
    hrparent VARCHAR(20),
    com_name VARCHAR(255),
    com_code INTEGER,
    dis_code INTEGER,
    pro_code INTEGER,
    geom GEOMETRY(MultiPolygon, 4326)
);

 CREATE TABLE province_kh (
    id SERIAL PRIMARY KEY,
    objectid INTEGER,
    level DOUBLE PRECISION,
    hrname VARCHAR(255),
    hrpcode VARCHAR(20),
    hrparent VARCHAR(20),
    com_name VARCHAR(255),
    com_code INTEGER,
    dis_code INTEGER,
    pro_code INTEGER,
    geom GEOMETRY(MultiPolygon, 4326)
);