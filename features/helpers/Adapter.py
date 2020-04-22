from datetime import datetime

import mysql.connector
from mysql import connector

from features.configuration.configuration import Configuration


class Adapter():

    def __getNow__(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

    def __connect__(self, context):
        config = Configuration()
        cnx = mysql.connector.connect(user=context.config.userdata.get('user'), password=context.config.userdata.get('pass'), host=config.getHost(),
                                      database=config.getDBName())
        cnx.autocommit = True
        return cnx

    def __closeConnection__(self, cnx):
        cnx.close()

    def __getExecuteSelectQuery__(self, query, cnx):
        cursor = cnx.cursor()
        try:
            cursor.execute(query)
        except mysql.connector.Error as error:
            print("Failed to select record from headline table {}".format(error))
            return None
        return cursor

    def getRecords(self,context , query):
        try:
            cnx = self.__connect__(context)
            cursor = self.__getExecuteSelectQuery__(query, cnx)
            records = cursor.fetchall()
            self.__closeConnection__(cnx)
        except mysql.connector.Error as error:
            print("Failed to get records from headline table {}".format(error))
        return records

    def insertRecord(self,context, sql):
        cnx = self.__connect__(context)
        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
            self.__closeConnection__(cnx)
            return True
        except Exception as error:
                print("Failed to insert record into Laptop table {}".format(error))
        finally:
            if (cnx.is_connected()):
                cnx.close()
                return False;