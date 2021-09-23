import databasefunctions
import os
import configparser
import time

def reset():
    os.system('python3 setup.py')
    time.sleep(3)
    exit()
def main():
    path=os.getcwd()+'\\config.ini'
    #print(os.listdir(os.getcwd()))
    #print('config.ini'  not in os.listdir(os.getcwd()))
    if 'config.ini' not in os.listdir(os.getcwd()):
        exit("Config.ini not found. Start setup.py first to create configuration file!")
    con=configparser.ConfigParser()
    con.read('config.ini')
    db_host=con['DATABASE']['hostname']
    db_user = con['DATABASE']['username']
    try:
        db_port = int(con['DATABASE']['port'])
    except ValueError:
        exit("Can not conver 'port' to intiger! Run setup.py again and type correct port!")
    db_pass = con['DATABASE']['password']
    #databasefunctions.create_account(host=db_host, user=db_user, password=db_pass, port=db_port)
    print("Welcome to finaces management program. Chose what you want to do:")
    while True:
        print("1. Create new account\n"
              "2. Create new transaction\n"
              "3. Overview accout\n"
              "0. Exit\n"
              "")
        inp = input("Type number: ")
        if inp=='1':
            databasefunctions.create_account(host=db_host, user=db_user, password=db_pass, port=db_port)
            pass
        elif inp == '2':
            databasefunctions.create_transaction(host=db_host, user=db_user, password=db_pass, port=db_port)
            pass
        elif inp == '3':
            databasefunctions.account_overview(host=db_host, user=db_user, password=db_pass, port=db_port)
            pass
        elif inp == '0':
            break
        elif inp.lower() == 'reset':
            reset()
        else:
            continue
    pass
if __name__ == '__main__':
    main()
    #run_setup()