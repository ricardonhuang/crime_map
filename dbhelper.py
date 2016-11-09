#coding=utf-8
'''
Created on 2016年11月9日

@author: huangning
'''   
import MySQLdb



class DBHelper:
    def connect(self, database="crimemap"):
        return MySQLdb.connect(host='192.168.1.237',
                               user='root',
                               passwd='admin',
                               db=database)
    
    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()
            
            
    def add_input(self, data):
        connection = self.connect()
        try:
            # The following introduces a deliberate security flaw.
            #See section on SQL injection below
            query = "INSERT INTO crimes (description) VALUES('%s');" % (data)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
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