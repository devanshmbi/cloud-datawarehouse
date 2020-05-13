import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

""" This function will drop all the tables if exists any """
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

""" This function will create respective tables for our project"""
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ Read configurations from dwh.cfg """
    config = configparser.ConfigParser()
    print("Read configurations from the configuration file")
    config.read('dwh.cfg')
    
    """ Reading hostname, databasename, user and password to connect to database """
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".\
                            format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    print("Connected to Redshift ")
    
    """ Executing function drop_tables to drop tables before creating """
    drop_tables(cur, conn)
    print("Droped existing tables from sparkifydb")
    
    """ Executing function create_tables to create tables as per star schema """
    create_tables(cur, conn)
    print("Created new tables into sparkifydb")
    
    """ Closing connection """
    conn.close()


if __name__ == "__main__":
    main()