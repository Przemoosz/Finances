import psycopg2
from psycopg2 import sql, extensions


def database_drop(*, host, user, password, port):
    try:
        conn = psycopg2.connect(host=host, user=user, password=password, port=port)
        curs = conn.cursor()
        curs.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname='finanse';")
        dblist = curs.fetchall()
        print('Checking if database "finanse" exists - 25%')
        if dblist != [] and dblist[0][0] == 'finanse':

            autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
            conn.set_isolation_level(autocommit)
            curs.execute(sql.SQL("DROP DATABASE finanse"))
            curs.close()
            conn.close()
            print("Droped previous database - 50%")
        else:

            curs.close()
            conn.close()
            print('Database "finanse" never existed before - 50%')
            return False
    except Exception as expectation:
        print('Something went wrong!')
        print(f'Expectation mssage: {expectation}')

        exit()


def database_create(*, host, user, password, port):
    try:
        conn = psycopg2.connect(host=host, user=user, password=password, database="postgres", port=port)
        curs = conn.cursor()
        autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        conn.set_isolation_level(autocommit)
        curs.execute(sql.SQL("CREATE DATABASE finanse"))
        curs.close()
        conn.close()
        print('Creted database "finanse" - 75%')
    except Exception as expectation:
        print('Something went wrong!')
        print(f'Expectation mssage: {expectation}')
        exit()


def table_accounts_creation(*, host, user, password, port):
    with psycopg2.connect(host=host, database='finanse', user=user, password=password, port=port) as conn:
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
            print('Created "accounts" table - 80%')
        pass


def table_transactions_creation(*, host, user, password, port):
    with psycopg2.connect(host=host, database='finanse', user=user, password=password, port=port) as conn:
        with conn.cursor() as curs:
            curs.execute('CREATE TABLE IF NOT EXISTS transactions('
                         'Transaction_No SERIAL PRIMARY KEY,'
                         'Transaction_Name TEXT NOT NULL,'
                         'Value FLOAT(2) NOT NULL,'
                         'Date DATE NOT NULL DEFAULT CURRENT_DATE,'
                         'Account_No INT REFERENCES accounts(No));')
            conn.commit()
            print('Created "transactions" table - 90%')
        pass
    pass
