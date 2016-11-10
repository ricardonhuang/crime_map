#coding=utf-8
'''
Created on 2016年11月9日

@author: huangning
'''   
import MySQLdb
import datetime


class DBHelper:
    def connect(self, database="crimemap"):
        return MySQLdb.connect(host='192.168.1.237',
                               user='root',
                               passwd='admin',
                               db=database)
    
    def get_all_crimes(self):
        connection = self.connect()
        try:
            query = "SELECT latitude, longitude, date, category,description FROM crimes;"
            cursor = connection.cursor()
            cursor.execute(query)
            named_crimes = []
            for crime in cursor:
                named_crime = {
                    'latitude': crime[0],
                    'longitude': crime[1],
                    'date': datetime.datetime.strftime(crime[2], '%Y-%m-%d'),
                    'category': crime[3],
                    'description': crime[4]
                    }
                named_crimes.append(named_crime)
            return named_crimes
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
        finally:
            connection.close()
            
    def add_crime(self, category, date, latitude, longitude,description):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (category, date, latitude,longitude, description) \
                    VALUES (%s, %s, %s, %s, %s)"
            cursor = connection.cursor()
            cursor.execute(query, (category, date, latitude, longitude,description))
            connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()