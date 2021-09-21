import psycopg2
import Decorators
import configparser
from input_functions import DefinedInputs

con = configparser.ConfigParser()
con.read('config.ini')
if con['Timer']['timer'] == 'False':
    timer_mode = False
else:
    timer_mode = True


@Decorators.function_timer(mode=timer_mode)
# Type password to database_exist to check if the database finaces exists
@Decorators.database_exist(password=None)
def acc_table_overview(host=None, user=None, password=None, port=None):
    with psycopg2.connect(host=host, user=user, password=password, database='finanse', port=port) as conn:
        with conn.cursor() as curs:
            # ex = "INSERT INTO accounts(Name,Owner,Currency,Funds) VALUES('Pierwsze','Adam B','PLN',1000);"

            curs.execute('SELECT * FROM accounts;')
            for i in curs.fetchall():
                print(i)
            # print(curs.fetchall())
            # conn.commit()





@Decorators.function_timer(mode=timer_mode)
def create_account(host=None, user=None, password=None, port=None):
    print("Account creator")
    acc_name = input("Account name(Not longer than 255 chars): ")
    acc_owne = input("Account owner (Not longer than 255 chars): ")
    acc_currency = DefinedInputs.currency()
    acc_funds = DefinedInputs.funds()
    command = f"INSERT INTO accounts(name,owner,currency,funds) VALUES ('{acc_name}','{acc_owne}','{acc_currency}',{acc_funds});"
    with psycopg2.connect(host=host, database='finanse', user=user, password=password, port=port) as conn:
        with conn.cursor() as curs:
            curs.execute(command)
            conn.commit()
            pass
        pass
    pass
@Decorators.function_timer(mode=timer_mode)
def create_transaction(host=None, user=None, password=None, port=None):
    print("Transaction creator")
    trs_name=input("Type transaction name(Not longer than 255 chars): ")
    trs_val=DefinedInputs.val()
    with psycopg2.connect(host=host, database='finanse', user=user, password=password, port=port) as conn:
        with conn.cursor() as curs:
            curs.execute('SELECT no,name FROM accounts;')
            print('List of avaible accounts:')
            for i in curs.fetchall():
                print(f'{i[0]}-{i[1]}')
            acc_num=input("Type account number to assign transaction to them: ")

if __name__ == '__main__':
    pass
