import MySQLdb

class ConnectionFactory:
    def get_connection(self):
        return MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='',
            db='test'
        )
