import setup_dbfunctions
import os
import configparser
import Decorators


@Decorators.function_timer()
def setup():
    path = os.getcwd() + '\\config.ini'
    # print(path)
    print("Getting informations about database. Press enter to set default values. Default values are in (brackets).")
    db_host = input("Enter hostname (localhost):")
    if db_host == "":
        db_host = 'localhost'
    db_user = input("Enter username (postgres):")
    if db_user == "":
        db_user = 'postgres'
    pass
    db_port = input("Enter port (5432):")
    if db_port == "":
        db_port = 5432
    db_pass = input("Enter password [Can not be empty!]: ")
    config = configparser.ConfigParser()
    config['DATABASE'] = {'Hostname': db_host,
                          'Username': db_user,
                          'Port': db_port,
                          'Password': db_pass}
    timer = input("Type False to turn off timer decorator(Default - True): ")
    if timer.lower() != 'false':
        timer = True
    else:
        timer = False
    config['Timer'] = {'Timer': timer}
    print('\nStarting save config file procedure - 0%')
    with open(path, 'w', encoding='UTF-8') as file:
        config.write(file)
    print("Writing config file went successfully - 100%\n")
    db_drop = input("Type 'Yes' to keep your previous database [Press enter for first run]: ")
    if db_drop.lower() != 'yes':
        print('\nStarting database operations - 0%')
        setup_dbfunctions.database_drop(host=db_host, user=db_user, password=db_pass, port=db_port)
        setup_dbfunctions.database_create(host=db_host, user=db_user, password=db_pass, port=db_port)
        setup_dbfunctions.table_accounts_creation(host=db_host, user=db_user, password=db_pass, port=db_port)
        setup_dbfunctions.table_transactions_creation(host=db_host, user=db_user, password=db_pass, port=db_port)
        print('Database and tables created successfully - 100%\n')


if __name__ == '__main__':
    setup()
