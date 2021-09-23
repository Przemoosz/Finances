import psycopg2
import Decorators
import configparser
from input_functions import DefinedInputs
import os
from datetime import date
'''This is databasefunctions.py which contains all database functions we are using:
    accout_overview - shows info about account and transaction connected to account
    create_accout - creates new account in data base accounts
    create_transaction - creates new transaction and attach them to account
    funds_actualisation - after adding new transaction to account, account fund must be updated. That what this function does.
    '''
if 'config.ini' not in os.listdir(os.getcwd()):
    exit("Config.ini not found. Start setup.py first to create configuration file!")
con = configparser.ConfigParser()
con.read('config.ini')
if con['Timer']['timer'] == 'False':
    timer_mode = False
else:
    timer_mode = True

# Overview accounts
@Decorators.function_timer(mode=timer_mode)
# Type password to database_exist to check every time if the database finaces exists, not recomended to normal use
@Decorators.database_exist(password=None)
def account_overview(host=None, user=None, password=None, port=None):
    with psycopg2.connect(host=host, user=user, password=password, database='finanse', port=port) as conn:
        with conn.cursor() as curs:
            curs.execute('SELECT no,name FROM accounts ORDER BY no ASC;')
            print('List of avaible accounts:')
            for i in curs.fetchall():
                print(f'{i[0]}-{i[1]}')
            curs.execute('SELECT no,name FROM accounts;')
            length = len(curs.fetchall())
            acc_num = DefinedInputs.acc_number(length)
            command = f"SELECT * FROM accounts WHERE no = {acc_num}"
            curs.execute(command)
            tup = curs.fetchone()
            print(f'Name: {tup[1]}\n'
                  f'Owner: {tup[2]}\n'
                  f'Currency: {tup[3]}\n'
                  f'Funds: {tup[4]}\n'
                  f'Creation Date: {tup[5]}\n'
                  f'Actualisation date: {tup[6]}\n')
            print(f"Transactions on accout '{tup[1]}'")
            command = f"SELECT * FROM transactions WHERE account_no = {acc_num};"
            curs.execute(command)
            [print(f'Title: {i[1]}, Value: {i[2]}, Date: {i[3]}') for i in curs.fetchall()]
            print("")


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
    trs_name = input("Type transaction name(Not longer than 255 chars): ")
    trs_val = DefinedInputs.val()
    with psycopg2.connect(host=host, database='finanse', user=user, password=password, port=port) as conn:
        with conn.cursor() as curs:
            curs.execute('SELECT no,name FROM accounts ORDER BY no ASC;')
            print('List of avaible accounts:')
            for i in curs.fetchall():
                print(f'{i[0]}-{i[1]}')
            curs.execute('SELECT no,name FROM accounts;')
            length = len(curs.fetchall())
            acc_num = DefinedInputs.acc_number(length)
            command = f"INSERT INTO transactions(transaction_name,value,account_no) VALUES ('{trs_name}',{trs_val},{acc_num});"
            curs.execute(command)
            conn.commit()
            funds_actualisation(acc_num, trs_val, host=host, user=user, password=password, port=port)


def funds_actualisation(acc_num, value, *, host=None, user=None, password=None, port=None):
    with psycopg2.connect(host=host, database='finanse', user=user, password=password, port=port) as conn:
        with conn.cursor() as curs:
            command = f"SELECT funds FROM accounts WHERE no={acc_num};"
            curs.execute(command)
            funds = curs.fetchall()[0][0]

            funds = funds + value
            command = f"UPDATE accounts SET funds={funds} WHERE no={acc_num};"
            curs.execute(command)
            conn.commit()
            command = f"UPDATE accounts SET actualisation_date='{date.today()}' WHERE no={acc_num};"
            curs.execute(command)
            conn.commit()
            pass
        pass

    pass


if __name__ == '__main__':
    pass
