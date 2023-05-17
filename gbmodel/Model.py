
"""
Main python class
"""

class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, name, code, floor, room, rating):
        """
        Inserts entry into database
        :param name: String
        :param code: String
        :param floor: Int
        :param room: Int
        :param rating:Int
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

    def remove(self, name, code, floor, room, rating):
        """
        matches the entries and deletes the entry
        """
        pass