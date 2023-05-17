
""" Database has study space information
1)  Building name 2) Building code 3) Building Floor 4)Closeest room number
    5) Rating is stored is stored in the database
+---------+----------+----------+----------+---------+
  Name      Code      Floor      Room       Rating
  ===================================================
  Engineering  EB      1          80         1
  building
+---------+----------+----------+----------+---------+
  
"""
from datetime import date
from .Model import Model
import sqlite3

DB_FILE = 'entries.db'   #database file

class model(Model):
    def __init__(self):     #constructor
        connection = sqlite3.connect(DB_FILE)
        """if database does not exist it will create one"""
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from studyspace")
        except sqlite3.OperationalError:
            cursor.execute("create table studyspace (name text, code text, floor int, room int, rating int)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, code, floor, room, rating
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM studyspace")
        return cursor.fetchall()

    def insert(self, name, code, floor, room, rating):
        """
        Inserts entry into database
        :param name: String
        :param code: String
        :param floor: Int
        :param room: Int
        :param rating: Int
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'code':code, 'floor':floor, 'room':room, 'rating':rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into studyspace (name, code, floor, room, rating) VALUES (:name, :code, :floor, :room, :rating)", params)

        connection.commit()
        cursor.close()
        return True

    def remove(self, name, code, floor, room, rating):
        """
        Gets all rows from the database
        Each row contains: name, code, floor, room, rating
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        command_remove = "DELETE FROM studyspace WHERE name=\"" + name + "\" AND code=\"" +floor +"\" AND room=\""+room+ "\" rating=\""+rating+"\""
        cursor.execute(command_remove)
        cursor.commit()
        cursor.close()
        return True