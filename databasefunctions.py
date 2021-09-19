import psycopg2
import Decorators
timer_mode=True     # Set to False to hide info about execution time of functions
@Decorators.function_timer(mode=timer_mode)
def table_creation(password):
    with psycopg2.connect(host="localhost",database='finanse',user='postgres',password=password,port=5432) as conn:
        with conn.cursor() as curs:
            curs.execute('CREATE TABLE IF NOT EXISTS accounts('
                         'No SERIAL PRIMARY KEY,'
                         'Name VARCHAR(255) NOT NULL,'
                         'Owner VARCHAR(255) NOT NULL,'
                         'Currency VARCHAR(3) NOT NULL,'
                         'Funds FLOAT(2) NOT NULL,'
                         'CreationDate DATE NOT NULL DEFAULT CURRENT_DATE,'
                         'ActualisationDate DATE);')
            conn.commit()
            # curs.execute('ALTER SEQUENCE accounts_No_seq RESTART WITH 1 INCREMENT BY 1;')
            # conn.commit()
        pass
@Decorators.function_timer(mode=timer_mode)
def drop_table(password):
    with psycopg2.connect(host="localhost",user='postgres',password=password,database='finanse',port=5432) as conn:
        with conn.cursor() as curs:
            curs.execute('DROP TABLE accounts;')
@Decorators.function_timer(mode=timer_mode)
def acc_table_overview(password):
    with psycopg2.connect(host="localhost",user='postgres',password=password,database='finanse',port=5432) as conn:
        with conn.cursor() as curs:
            ex="INSERT INTO accounts(Name,Owner,Currency,Funds) VALUES('Pierwsze','Adam B','PLN',1000);"
            curs.execute(ex)
            conn.commit()
            #print(curs.fetchall())