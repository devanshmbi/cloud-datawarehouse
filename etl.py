import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

""" This function will load the staging tables staging_events and staging_songs """
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


""" This function will load other tables using staging_events and staging_songs """
def insert_tables(cur, conn):
    for query in insert_table_queries:
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
    
    """ Executing Copy command to load tables staging_events and staging_songs  """
    load_staging_tables(cur, conn)
    print(" Inserted Data into tables staging_events and staging_songs ")
    
    """ Executing Insert queries """
    insert_tables(cur, conn)
    print("Inserted records into all the tables")
    
    """ Closing connections """
    conn.close()


if __name__ == "__main__":
    main()