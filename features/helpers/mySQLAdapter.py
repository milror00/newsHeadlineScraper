import mysql.connector

from features.configuration.configuration import Configuration


def connect():
    config = Configuration()
    cnx = mysql.connector.connect(user=config.getUsername(), password=config.getPassword(), host=config.getHost(),
                                  database=config.getDBName())
    return cnx


def closeConnection(cnx):
    cnx.close()


def getRecords(cursor):
    try:
        records = cursor.fetchall()
    except Exception as e:
        print(e)
        return None
    return records


def getExecuteSelectQuery(query, cnx):
    cursor = cnx.cursor()
    try:
        cursor.execute(sql_select_Query)
    except Exception as e:
        print(e)
        return None
    return cursor


try:
    cnx = connect()
    sql_select_Query = "select * from test"
    cursor = getExecuteSelectQuery(sql_select_Query, cnx)
    if cursor != None:
        getRowCount(cursor)
    closeConnection(cnx)
except Exception as e:
    print(e)
