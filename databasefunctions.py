import psycopg2
import Decorators
import configparser
import os
con=configparser.ConfigParser()
con.read('config.ini')
if con['Timer']['timer'] == 'False':
    timer_mode=False
else:
    timer_mode=True

@Decorators.function_timer(mode=timer_mode)
# Type password to database_exist to check if the database finaces exists
@Decorators.database_exist(password=None)
def table_accounts_creation(password):
    with psycopg2.connect(host="localhost", database='finanse', user='postgres', password=password, port=5432) as conn:
        with conn.cursor() as curs:
            curs.execute('CREATE TABLE IF NOT EXISTS accounts('
                         'No SERIAL PRIMARY KEY,'
                         'Name VARCHAR(255) NOT NULL,'
                         'Owner VARCHAR(255) NOT NULL,'
                         'Currency VARCHAR(3) NOT NULL,'
                         'Funds FLOAT(2) NOT NULL,'
                         'Creation_Date DATE NOT NULL DEFAULT CURRENT_DATE,'
                         'Actualisation_Date DATE);')
            conn.commit()
            # curs.execute('ALTER SEQUENCE accounts_No_seq RESTART WITH 1 INCREMENT BY 1;')
            # conn.commit()
        pass


@Decorators.function_timer(mode=timer_mode)
def drop_table(*,password=None,table=None):
    with psycopg2.connect(host="localhost", user='postgres', password=password, database='finanse', port=5432) as conn:
        with conn.cursor() as curs:
            ex=f'DROP TABLE {table};'
            curs.execute(ex)


@Decorators.function_timer(mode=timer_mode)
def acc_table_overview(host=None, user=None, password=None, port=None):
    with psycopg2.connect(host=host, user=user, password=password, database='finanse', port=port) as conn:
        with conn.cursor() as curs:
            #ex = "INSERT INTO accounts(Name,Owner,Currency,Funds) VALUES('Pierwsze','Adam B','PLN',1000);"

            curs.execute('SELECT * FROM accounts;')
            for i in curs.fetchall():
                print(i)
            #print(curs.fetchall())
            #conn.commit()
@Decorators.function_timer(mode=timer_mode)
def table_transactions_creation(password):
    with psycopg2.connect(host="localhost", database='finanse', user='postgres', password=password, port=5432) as conn:
        with conn.cursor() as curs:
            curs.execute('CREATE TABLE IF NOT EXISTS transactions('
                         'Transaction_No SERIAL PRIMARY KEY,'
                         'Transaction_Name TEXT NOT NULL,'
                         'Value FLOAT(2) NOT NULL,'
                         'Date DATE NOT NULL DEFAULT CURRENT_DATE,'
                         'Account_No INT REFERENCES accounts(No));')
            conn.commit()
            # curs.execute('ALTER SEQUENCE accounts_No_seq RESTART WITH 1 INCREMENT BY 1;')
            # conn.commit()
        pass
    pass
@Decorators.function_timer(mode=timer_mode)
def example_tables(password):
    
    pass

if __name__ == '__main__':
    config()
