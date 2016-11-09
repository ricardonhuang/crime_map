#coding=utf-8
'''
Created on 2016年11月9日

@author: huangning
'''
import MySQLdb

connection = MySQLdb.connect(host="192.168.1.237",
                             user="root",
                             passwd="admin")
try:
    #with connection.cursor() as cursor:
        cursor = connection.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
                    id int NOT NULL AUTO_INCREMENT,
                    latitude FLOAT(10,6),
                    longitude FLOAT(10,6),
                    date DATETIME,
                    category VARCHAR(50),
                    description VARCHAR(1000),
                    updated_at TIMESTAMP,
                    PRIMARY KEY (id)
                )"""
        cursor.execute(sql);
        connection.commit()
finally:
    connection.close()