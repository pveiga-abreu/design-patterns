'''
Design Pattern Factory
'''
from classes.connection_factory import ConnectionFactory

def main():
    conn = ConnectionFactory().get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM example')

    for record in cursor: print(record)

    conn.close()

if __name__=='__main__':
    main()
